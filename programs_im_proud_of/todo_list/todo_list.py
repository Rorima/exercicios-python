"""
To do list:

Make a program in which you can type the name
of activities and you can check them.

You should be able to:

* Create new list items;
* Edit list items;
* Delete list items;
* Check list items;
* Order list items (by checked or in alphabetical order);
* Check all or uncheck all;
* Store your to do list

The program is probably finished. Test it a few more times and use it.
"""
import json
from os import system
from os.path import exists
from time import sleep

class ToDoList:

    def __init__(self):
        
        self.todo_list = {"items": []}
        self.all_checked = False
        
        if exists("list.json"):
            if not self.file_empty():
                self.import_list()
            else: 
                self.save_list()
        
        self.menu()
    
    def menu(self):
        """Present a menu to the user"""
        
        sleep(1)
        
        self.save_list()
        
        self.display_list()
        
        print("[1] Check/uncheck an item;")
        print("[2] Add a new item;")
        print("[3] Edit an item;")
        print("[4] Move item;")
        print("[5] Delete an item;")
        print("[6] Check/uncheck all;")
        print("[7] Exit program.")
        
        functions = (
            self.check_uncheck_item,
            self.add_item,
            self.edit_item,
            self.move_item,
            self.delete_item,
            self.check_uncheck_all,
            self.exit_program
        )
        
        option = self.treat_number_input(max_val=len(functions))
        
        functions[option]()
    
    def treat_number_input(self, max_val):
        """Treat the input from the caller function."""
        
        allowed_values = [str(x) for x in range(1, max_val+1)]
        
        while True:
            value = input(">>> ")
            
            if value not in allowed_values:
                self.display_list()
                
                print("You have to choose a valid number.")
                continue
            else:
                return int(value) - 1
    
    def display_list(self):
        """Display all items"""
        
        system("cls||clear")
        
        if self.todo_list["items"]:
            for counter, item in enumerate(self.todo_list["items"]):
                check_mark = "*" if item["checked"] else " "
                print(f"[{counter+1}] [{check_mark}] {item['name']}")
        else:
            print("You have no items in your todo list.")
        
        print("\n")
    
    def check_uncheck_item(self):        
        """Check or uncheck an item."""
        
        if self.todo_list["items"]:
            
            print("Enter the item would you like to check/uncheck: ")
            
            item_count = len(self.todo_list["items"])
            option = self.treat_number_input(max_val=item_count)
            
            if self.todo_list["items"][option]["checked"]:
                self.todo_list["items"][option]["checked"] = False
            else:
                self.todo_list["items"][option]["checked"] = True
        else:
            print("You have no items in your todo list.")
            
        self.menu()
    
    def add_item(self):
        """Add a new item to the todo_list getting data from the user."""
        
        self.display_list()
        
        print("Type the name of the new item: ")
        name = input(">>> ")
        
        self.todo_list["items"].append({"name": name, "checked": False})
        
        self.menu()
    
    def edit_item(self):
        """Edit the name of an item."""
        
        if self.todo_list["items"]:
            self.display_list()
            
            print("Enter the number of the item you want to change: ")
            item_count = len(self.todo_list["items"])
            option = self.treat_number_input(max_val=item_count)
            
            self.display_list()
            
            print("Enter the new name: ")
            new_name = input(">>> ")
            
            self.todo_list["items"][option]["name"] = new_name
        else:
            print("You have no items in your todo list.")
            
        self.menu()
    
    def move_item(self):
        """Swap items."""
        
        if self.todo_list["items"]:
            self.display_list()
            
            print("Enter the number of the item you want to move: ")
            item_count = len(self.todo_list["items"])
            pos = self.treat_number_input(max_val=item_count)
            
            print("Enter the new position: ")
            new_pos = self.treat_number_input(max_val=item_count)
            
            temporary = self.todo_list["items"][new_pos]
            self.todo_list["items"][new_pos] = self.todo_list["items"][pos]
            self.todo_list["items"][pos] = temporary
        else:
            print("You have no items in your todo list.")
            
        self.menu()
    
    def delete_item(self):
        """Delete an item."""
        
        if self.todo_list["items"]:
            self.display_list()
            
            print("Enter the number of the item you want to delete: ")
            item_count = len(self.todo_list["items"])
            option = self.treat_number_input(max_val=item_count)
            
            self.todo_list["items"].pop(option)
        else:
            print("You have no items in your todo list.")
            
        self.menu()
    
    def check_uncheck_all(self):
        """Check or uncheck all items."""
        
        self.display_list()
        
        print("Are you sure you want to check/uncheck all items?")
        print("[1] Yes;")
        print("[2] No;")
        answer = input(">>> ")
        
        if answer == "1":
            for i in range(len(self.todo_list["items"])):
                self.todo_list["items"][i]["checked"] = self.all_checked
        
        self.all_checked = False if self.all_checked else True
        
        self.menu()
    
    def save_list(self):
        """Save all items to a json file."""
        
        with open('list.json', 'w') as f:
            json.dump(self.todo_list, f, indent=2)
        
    def import_list(self):
        """Import items from a json file."""
        
        with open('list.json', 'r') as f:
            self.todo_list = json.load(f)
    
    def file_empty(self):
        """Check if the file is empty."""
        
        with open("list.json", 'r') as f:
            something = f.readline()
        
        return False if something else True
    
    def exit_program(self):
        """Call no function so that the program can end."""
        
        print("The program was executed successfully!")


if __name__ == "__main__":
    todo_list = ToDoList()
