#!/usr/bin/python3

"""The HBnB console"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    braces = re.search(r'\[(.*?)\]', arg)

    if curly_braces is None:
        if braces is None:
            return [i.strip(',') for i in split(arg)]
        else:
            lexer = split(arg[:braces.span()[0]])
            retl = [i.strip(',') for i in lexer]
            retl.append(braces.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(',') for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    The HolbertonBnB command interpreter
    Attributes:
        prompt (str): The command prompt
    """

    prompt = '(hbnb) '
    __c_list = {
        'BaseModel',
        'User',
        'State',
        'Place',
        'Review',
        'City',
        'Amenity'
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def do_emptyline(self, arg):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Usage: creates a new instance of class BaseModel and print its id.
        """
        argl = parse(arg)

        if not argl:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__c_list:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and `id`
        """
        argl = parse(arg)
        o_dict = storage.all()

        if not argl:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__c_list:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in o_dict:
            print("** no instance found **")
        else:
            print(o_dict[f"{argl[0]}.{argl[1]}"])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and `id` and
        saves the change into the JSON file
        """
        argl = parse(arg)
        o_dict = storage.all()

        if not argl:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__c_list:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in o_dict.keys():
            print("** no instance found **")
        else:
            del o_dict[f"{argl[0]}.{argl[1]}"]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """
        argl = parse(arg)

        if len(argl) > 0 and argl[0] not in HBNBCommand.__c_list:
            print("** class doesn't exist **")
        else:
            ol = []

            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    ol.append(obj.__str__())
                elif len(argl) == 0:
                    ol.append(obj.__str__())
            print(ol)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        argl = parse(arg)
        o_dict = storage.all()

        if not argl:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__c_list:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if f"{argl[0]}.{argl[1]}" not in o_dict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = o_dict[f"{argl[0]}.{argl[1]}"]

            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = (argl[3])
        elif type(eval(argl[2])) == dict:
            obj = o_dict[f"{argl[0]}.{argl[1]}"]
            for k, v in eval(argl[2]).items():
                if (
                    k in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[k]) in {str, int, float}
                ):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""

        argl = parse(arg)
        count = 0
        for v in storage.all().values():
            if argl[0] == v.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavioour of cmd module when input is invalid"""

        a_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'count': self.do_count,
                'update': self.do_update
                }

        match = re.search(r'\.', arg)

        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r'\((.*?)\)', argl[1])

            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in a_dict.keys():
                    call = f"{argl[0]} {command[1]}"
                    return a_dict[command[0]](call)
        print(f"*** Unknown syntax: {arg}")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
