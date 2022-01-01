#!/usr/bin/python3
""" entry point of the command interpreter """


import cmd
from models import storage
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
        """
            EOF signal to exit the program
        """

        print("")
        return True

    def do_quit(self, argv):
        """
            When executed, exits the console
        """

        return True

    def emptyline(self):
        """
            Command to executed when empty line + <ENTER> key
        """

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

    def do_show(self, argv):
        """
            Prints the string representation of an instance
            based on the class name and id
        """

        args = check_args(argv)

        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key].__str__())

    def do_destroy(self, argv):
        """
            Deletes an instance based on the class name and id
        """

        args = check_args(argv)

        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, argv):
        """
            Prints all string representation of all instances based
            or not on the class name
        """

        arg_list = argv.split()

        if len(arg_list) == 0:
            print([obj.__str__() for obj in storage.all().items()])
        elif arg_list[0] in CLASSES:
            for obj in storage.all().items():
                print(vars(obj))
                print("class names ", obj.__class__.__name__)
            print([obj.__str__() for obj in storage.all().items() if obj.__class__.__name__ == arg_list[0]])
        else:
            print("** class doesn't exist **")



if __name__ == "__main__":
    HBNBCommand().cmdloop()
