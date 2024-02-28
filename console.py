#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
import json
import re
import models
# from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '

    def my_errors(self, line, num_of_args):
        """Displays error messages to user

        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments

        Description:
            Displays output to the use based on
            the input commands.

        """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0

    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

    def do_quit(self, line):
        """Handles the 'quit' command

        Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d

         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def do_create(self, line):
        """Creates a new instance of @cls_name class,
        and prints the new instance's ID.

        Args:
            line(args): Arguments to enter with command: <class name>
            Example: 'create User'

        """
        if (self.my_errors(line, 1) == 1):
            return
        args = line.split(" ")

        """
        args[0] contains class name, create new instance
        of that class updates 'updated_at' attribute,
        and saves into JSON file
        """
        obj = eval(args[0])()
        obj.save()

        print(obj.id)

    def do_show(self, line):
        """Prints a string representation of an instance.

        Args:
            line(line): to enter with command <class name> <id>
            Example: 'show User 1234-1234-1234'

        """
        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(d[key])
if __name__ == '__main__':
    HBNBCommand().cmdloop()
