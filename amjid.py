# todo_app.py

class ToDoApp:
    def __init__(self):
        # Initialize an empty list to hold todos
        self.todos = []

    def add_todo(self, title, date):
        """Add a new todo with title and date"""
        todo_item = {"title": title, "date": date}
        self.todos.append(todo_item)
        print(f'To-Do "{title}" added successfully.')

    def show_todos(self):
        """Print all To-Do items"""
        if not self.todos:
            print("No To-Do items found.")
        else:
            print("To-Do List:")
            for idx, todo in enumerate(self.todos, start=1):
                print(f"{idx}. Title: {todo['title']}, Date: {todo['date']}")

    def delete_todo(self, title):
        """Delete a todo item by title"""
        for todo in self.todos:
            if todo['title'] == title:
                self.todos.remove(todo)
                print(f'To-Do "{title}" deleted successfully.')
                return
        print(f'To-Do "{title}" not found.')

    def delete_all_todos(self):
        """Delete all todo items"""
        self.todos.clear()
        print("All To-Do items have been deleted.")


def main():
    app = ToDoApp()

    while True:
        print("
--- To-Do List Application ---")
        print("1. Add To-Do")
        print("2. Show To-Do List")
        print("3. Delete a To-Do")
        print("4. Delete All To-Dos")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter To-Do title: ")
            date = input("Enter To-Do date (e.g., 2025-09-21): ")
            app.add_todo(title, date)
        elif choice == "2":
            app.show_todos()
        elif choice == "3":
            title = input("Enter To-Do title to delete: ")
            app.delete_todo(title)
        elif choice == "4":
            confirm = input("Are you sure you want to delete all To-Dos? (y/n): ")
            if confirm.lower() == 'y':
                app.delete_all_todos()
            else:
                print("Operation canceled.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()