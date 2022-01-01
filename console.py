#!/usr/bin/python3
""" entry point of the command interpreter """


import cmd
import shlex

from models.base_model import BaseModel

### an array of classes in the system
CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]

def check_args(args):
    """
        checks if args is valid

        Parameters
        ----------
            args: str
                the string containing the arguments passed to a command

        Return
        ------
            Error message if args is None or not a valid class, else the arguments
    """

    arg_list = args.split()

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list

class HBNBCommand(cmd.Cmd):
    """
        The class that implements the console for the
        AirBnB clone web application
    """

    prompt = "(hbnb) "

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_create(self, argv):
        """
            reates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id
        """

        args = check_args(argv)
        if args:
            newObj = eval(args[0])()
            newObj.save()
            print(newObj.id)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
