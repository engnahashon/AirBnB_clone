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
        else:
            try:
                new_base = models.class_dict[argv]
            except KeyError:
                print("** class doesn't exist **")
            new_object = new_base()
            new_object.save()
            print(new_object.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
