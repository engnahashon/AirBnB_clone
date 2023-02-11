#!/usr/bin/python3
"""AirBnB Console"""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
 
    def empty_line(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """To exit the program"""
        print()
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel"""
        if not argv:
            print("** class name missing **")
            return
        try:
            new_base = models.class_dict[argv]
            new_object = new_base()
            new_object.save()
            print(new_object.id)
        except KeyError:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        argv = line.split()
        if len(argv) == 0:
            print("** class name missing **")
            return
        if argv[0] not in models.class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        try:
            key = argv[0] + "." + argv[1]
            obj = models.storage.all()[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
