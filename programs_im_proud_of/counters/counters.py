"""
Plans:

Make a program that can create counters for you.

What the user should be able to do:

* Create new counters;
* Edit counter names;
* Add or subtract values from a counter;
* Delete a counter;
* Save the counters;

How should it be done?

* Using lists and/or dictionaries.

TODO:

* Treat inputs;
* Test with all sorts of inputs;
* Limit character length for counter names;
* Allow only integers;

MAYBE:

* Option to order the counters in alfabetical order (A to Z or Z to A);
* Option to order characters by values (lowest or highest);
"""
from time import sleep
from os import system
from os.path import exists


class Counter:
    
    def __init__(self):
    
        self.counters = []
        
        if exists('counters.txt'):
            self.import_counters()
        else:
            with open('counters.txt', 'w') as f:
                pass
        
    def menu(self):
        """Present a menu to the user."""
        
        sleep(1)
        
        self.save()
        
        self.display_counters()
        
        print("[1] Create new counter;")
        print("[2] Edit counter;")
        print("[3] Delete counter;")
        print("[4] Exit program.")
        user_choice = self.treat_input(
            min_val=1, 
            max_val=4
        )
        
        functions = (
            self.create, 
            self.edit, 
            self.delete,
            self.exit_program
        )
        functions[user_choice - 1]()
    
    def treat_input(self, min_val, max_val):
        """Treat the input from the caller function"""
        
        allowed_values = [str(x) for x in range(min_val, max_val + 1)]
        
        while True:
            user_choice = input()
            if user_choice not in allowed_values:
                self.display_counters()
                print("You have to choose a valid number.")
                continue
            else:
                return int(user_choice)
    
    def display_counters(self):
        """Display the counters."""
        
        # Clear screen from all text
        system("cls||clear")
        
        if self.counter_exists():
            print("Counter\t\t\t\t\t\tMinutes")
            for c, v in enumerate(self.counters):
                print(f"[{c+1}] {v[0]:<44s}{str(v[1]):<6s}")
        else:
            print("You have no counters yet.")
        
        print("\n\n")
    
    def create(self):
        """Create a new counter using user input."""
        
        self.display_counters()
        
        counter_name = input("Type the name of the counter: ")
        counter_name = self.treat_char_limit(counter_name)
        
        print("Starting number: ", end="")
        num = self.treat_numbers()
        
        self.counters.append([counter_name, num])
        self.menu()
    
    def treat_char_limit(self, counter_name):
        """Limit how many characters can go into a string."""
        
        while len(counter_name) > 42:
            self.display_counters()
            print("Counter name is too long. "
            "It should be 42 characters maximum.")
            print()
            print("Asterisks show characters that exceeded the limit:")
            print(counter_name[:42], end="")
            print("*"*(len(counter_name) - 42))
            print()
            counter_name = input("Type the name of the counter: ")
        
        return counter_name
            
    def treat_numbers(self):
        """Force the user to enter a valid number."""
        
        while(True):
            num = input()
            if num.isnumeric():
                break
            else:
                self.display_counters()
                print("You have to enter a valid number, "
                "using digits from 0 to 9.")
        
        return int(num)
        
    def increment(self):
        """Increment an existing counter."""
        
        if self.counter_exists():
            self.display_counters()
            print("Enter the number of the counter you "
            "would like to increment: ")
            chosen_counter = self.treat_input(
                min_val=1, 
                max_val=len(self.counters)
            )
            
            print("Enter the amount or 0 to cancel: ", end="")
            chosen_amount = self.treat_numbers()
            
            if chosen_amount != 0:
                self.counters[chosen_counter - 1][1] += chosen_amount
                print("Counter updated successfully!")
        else:
            print("You have no counters yet.")
        
        self.menu()
    
    def decrement(self):
        """Decrement an existing counter."""
        
        if self.counter_exists():
            self.display_counters()
            print("Enter the number of the counter you "
            "would like to decrement: ")
            chosen_counter = self.treat_input(
                min_val=1, 
                max_val=len(self.counters)
            )
            
            print("Enter the amount or 0 to cancel: ", end="")
            chosen_amount = self.treat_numbers()
            
            if chosen_amount != 0:
                # Preventing the counter from having a negative value
                if chosen_amount > self.counters[chosen_counter - 1][1]:
                    self.counters[chosen_counter - 1][1] = 0
                else:
                    self.counters[chosen_counter - 1][1] -= chosen_amount
                
                print("Counter updated successfully!")
        else:
            print("You have no counters yet.")
        
        self.menu()
    
    def edit(self):
        """Edit an existing counter."""
        
        sleep(1)
        
        self.display_counters()
        
        print("[1] Increment;")
        print("[2] Decrement;")
        print("[3] Edit counter name;")
        print("[4] Move counter position;")
        print("[5] Cancel.")
        user_choice = self.treat_input(
            min_val=1, 
            max_val=5
        )
        
        functions = (
            self.increment, 
            self.decrement,
            self.edit_name,
            self.move_counter,
            self.menu
        )
        
        functions[user_choice - 1]()
    
    def edit_name(self):
        """Edit the name of a counter"""
        
        if self.counter_exists():
            self.display_counters()
            print("Enter the number of the counter you "
                  "would like to edit: ")
            chosen_counter = self.treat_input(
                min_val=1, 
                max_val=len(self.counters)
            )
            
            new_name = input("Enter the new name or enter 0 to cancel: ")
            new_name = self.treat_char_limit(new_name)
            if new_name != '0':
                self.counters[chosen_counter - 1][0] = new_name
                print("Counter updated successfully!")
        else:
            print("You have no counters yet.")
        
        self.menu()
    
    def move_counter(self):
        """Swap counters"""
        
        if self.counter_exists():
            self.display_counters()
            print("Enter the number of the counter you "
            "would like to move: ")
            chosen_counter = self.treat_input(
                min_val=1, 
                max_val=len(self.counters)
            )
            
            print("Enter the new position or 0 to cancel: ", end="")
            new_position = self.treat_input(
                min_val=1, 
                max_val=len(self.counters)
            )
            
            if new_position != 0:
                temp = self.counters[new_position - 1]
                self.counters[new_position - 1] = self.counters[chosen_counter - 1]
                self.counters[chosen_counter - 1] = temp
                print("Counter updated successfully!")
        else:
            print("You have no counters yet.")
        
        self.menu()
        
    def delete(self):
        """Delete an existing counter."""
        
        if self.counter_exists():
            self.display_counters()
            print("Enter the number of the counter you "
            "would like to delete or 0 to cancel: ")
            chosen_counter = self.treat_input(
                min_val=0, 
                max_val=len(self.counters)
            )
            
            if chosen_counter != 0:
                self.counters.pop(chosen_counter - 1)
                print("Counter deleted successfully!")
        else:
            print("You have no counters yet.")
        
        self.menu()
    
    def save(self):
        """Save all counters to a .md file."""
        
        if self.counter_exists():
            with open("counters.txt", 'w') as f:
                for items in self.counters:
                    f.write(f"{items[0]},{items[1]}\n")
        
    def import_counters(self):
        """Import all counters from the counters.txt file"""
        
        with open("counters.txt", 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                
                data1, data2 = line.strip('\n').split(',')
                self.counters.append([data1, int(data2)])
    
    def exit_program(self):
        """Call no functions and allow the program to end."""
        return None
    
    def counter_exists(self):
        """Check if there are any counters inside the counters list."""
        return True if self.counters else False


if __name__ == "__main__":
    c = Counter()
    c.menu()
    print("Exited successfully!")