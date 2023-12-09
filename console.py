#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    # TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    def default(self, line):
        """Handle unrecognized commands."""
        print(f"Unrecognized command: {line}. Type 'help' for assistance.\n")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            print([
                str(obj) for key, obj in objects.items()
                if key.startswith(args[0] + '.')
            ])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.CLASSES:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]

        # Store the previous updated_at value
        # prev_updated_at = obj.updated_at

        # Simplify attribute handling (without explicit checks)
        setattr(obj, attribute, value)

        # Always update the updated_at attribute
        # obj.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
