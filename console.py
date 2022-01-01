#!/usr/bin/python3
""" entry point of the command interpreter """


import cmd

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
