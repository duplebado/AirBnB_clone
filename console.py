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
            print([obj.__str__() for obj in storage.all().values()])
        elif arg_list[0] in CLASSES:
            print([obj.__str__() for obj in storage.all().values() if obj.__class__.__name__ == arg_list[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, argv):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute
        """
        args = check_args(argv)

        if len(args) == 2:
            print("** attribute name missing **")
        if args[2] == "id" or args[2] == "created_at" or args[2] == "updated_at":
            pass
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            
            if args[2] in type(obj).__dict__:
                v_type = type(obj.__class__.__dict__[args[2]])
                setattr(obj, args[2], v_type(args[3]))
            else:
                setattr(obj, args[2], args[3])

            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
