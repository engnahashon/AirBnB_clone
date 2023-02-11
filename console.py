#!/usr/bin/python3
"""AirBnB Console"""
import cmd
import models
import re


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def emptyline(self):
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
        """Prints the string representation of an instance
    based on the class name and id"""
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
        """Prints all string representation of all instances
    based or not on the class name"""
        if "all()" in line:
            print("Found {}".format(line[:-5].strip))
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
        """Deletes an instance based on the class name
            and id and saves the change into the JSON file"""
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

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return
        else:
            line = line.split(' ')
            for i in range(len(line)):
                line[i] = line[i].strip("\"'\"{\"}:\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                setattr(obj, attr, val)
                                obj.save()
                                if len(line) >= 5:
                                    loop_dict(line, obj)
            else:
                print("** class doesn't exist **")

    def default(self, line):
        if re.search(r"\.all\(\)\s*$", line):
            class_name = line[:-6].strip()
            return self.do_all(class_name)

        elif re.search(r"\.show\s*\(", line):
            class_name, class_id = re.split(r"\.show\(", line)
            return self.do_show(class_name + " " + class_id[1:-2])

        elif re.search(r"\.destroy\s*\(", line):
            class_name, class_id = re.split(r"\.destroy\(", line)
            return self.do_destroy(class_name + " " + class_id[1:-2])

        else:
            print("** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
