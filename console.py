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

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        argv = line.split()
        instances = models.storage.all()
        if len(argv) == 0:
            output = []
            for obj in instances.values():
                output.append(str(obj))
            print(output)
        else:
            if argv[0] not in models.class_dict.keys():
                print("** class doesn't exist **")
                return
            else:
                output = []
                for obj in instances.values():
                    if type(obj).__name__ == argv[0]:
                        output.append(str(obj))
                print(output)

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id and saves the change into the JSON file"""
        if not argv:
            print("** class name missing **")
            return
        else:
            line = argv.split()
            if line[0] in models.class_dict:
                try:
                   key = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **") 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
