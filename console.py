#!/usr/bin/python3

"""The HBnB console"""

import cmd
import json
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


c_list = ['BaseModel', 'User', 'State', 'Place', 'Review', 'City', 'Amenity']


class HBNBCommand(cmd.Cmd):
    """
    The HolbertonBnB command interpreter
    Attributes:
        prompt (str): The command prompt
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""

        return True

    def do_emptyline(self):
        """Do nothing when an empty line is entered"""

        pass

    def do_create(self, arg):
        """
        Usage: creates a new instance of class BaseModel and print its id.
        """

        if not arg:
            print("** class name missing **")
            return
        if arg not in c_list:
            print("** class doesn't exist **")
            return
        if arg == 'BaseModel':
            x = BaseModel()
        if arg == 'User':
            x = User()
        if arg == 'Place':
            x = PLace()
        if arg == 'State':
            x = State()
        if arg == 'City':
            x = City()
        if arg == 'Amenity':
            x = Amenity()
        if arg == 'Review':
            x = Review()
        x.save()
        print(x.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and `id`
        """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in c_list:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        x = models.storage.all()

        for i in x.keys():
            f = i.split('.')
            if (f[1] == args[1]) and (f[0] == args[0]):
                print(x[i])
                return
        print("** no instance found **")
        return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and `id` and
        saves the change into the JSON file
        """

        if not arg:
            print("** class name missing **")
            return
        if args[0] not in c_list:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        args = arg.split(' ')
        x = models.storage.all()

        for i in x.keys():
            f = i.split('.')

            if (f[1] == args[1]) and (f[0] == args[0]):
                x.pop(i)
                models.storage.save()
                return
        print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """

        lst = []
        x = models.storage.all()
        args = arg.split(' ')

        if args[0] in lst or len(arg) == 0:
            for i in x.keys():
                f = i.split('.')

                if f == 'BaseModel' and arg == 'BaseModel':
                    lst.append(x[i].__str__())
                elif f == 'User' and arg == 'User':
                    lst.append(x[i].__str__())
                else:
                    lst.append(x[i].__str__())
            print(lst)
        else:
            print("** class name missing **")
            return

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """

        args = arg.split(' ')

        if not arg:
            print("** class name missing **")
            return
        if args[0] not in c_list:
            print("** class doesn't exist **")
            return
        x = models.storage.all()
        update = 0

        for i in x.keys():
            k = i.split('.')

            if k[1] == args[1]:
                update = 1
                f = i

        if update == 0:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        args = arg[0] + ' ' + args[1] + ' ' + args[2] + ' ' + args[3]
        args = args.split(' ')
        k = x[f].__dict__
        p = args[3].split('\'')
        k[args[2]] = p[1]
        x[f].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
