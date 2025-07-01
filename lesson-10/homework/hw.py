1. ToDo List Application

# Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date  # string format e.g. '2025-07-01'
        self.status = False  # False means Incomplete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status_str = "✅ Completed" if self.status else "❌ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue: {self.due_date}\nStatus: {status_str}"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("✅ Task added successfully.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task index.")

    def list_all_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        for i, task in enumerate(self.tasks):
            print(f"\n--- Task #{i} ---")
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.status]
        if not incomplete:
            print("🎉 All tasks are complete!")
            return
        for i, task in enumerate(incomplete):
            print(f"\n--- Incomplete Task #{i} ---")
            print(task)

def display_menu():
    print("\n📋 ToDo List Menu:")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. List All Tasks")
    print("4. List Incomplete Tasks")
    print("5. Exit")

def main():
    todo = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == "2":
            todo.list_all_tasks()
            try:
                index = int(input("Enter task number to mark as complete: "))
                todo.mark_task_complete(index)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# 📋 ToDo List Menu:
# 1. Add Task
# 2. Mark Task as Complete
# 3. List All Tasks
# 4. List Incomplete Tasks
# 5. Exit
# Enter your choice (1-5): 1
# Enter task title: Finish project
# Enter task description: Complete the ToDoList app
# Enter due date (YYYY-MM-DD): 2025-07-01
# ✅ Task added successfully.


# 2. Simple Blog System


# Define Post Class:
# Create a Post class with attributes like title, content, and author.
# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
# Create instances of posts and test the functionality of your Blog system.

from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date_created = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"\n📌 Title: {self.title}\n📝 Content: {self.content}\n✍️ Author: {self.author}\n📅 Posted on: {self.date_created.strftime('%Y-%m-%d %H:%M:%S')}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("✅ Post added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("📭 No blog posts available.")
            return
        for i, post in enumerate(self.posts):
            print(f"\n--- Post #{i} ---")
            print(post)

    def list_posts_by_author(self, author_name):
        filtered = [post for post in self.posts if post.author.lower() == author_name.lower()]
        if not filtered:
            print(f"❌ No posts found by author: {author_name}")
            return
        for post in filtered:
            print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            deleted = self.posts.pop(index)
            print(f"🗑 Post '{deleted.title}' deleted.")
        else:
            print("❌ Invalid index.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
            print("✏️ Post updated successfully.")
        else:
            print("❌ Invalid index.")

    def display_latest_posts(self, count=3):
        latest = sorted(self.posts, key=lambda p: p.date_created, reverse=True)[:count]
        if not latest:
            print("📭 No posts to display.")
            return
        print(f"🕒 Latest {len(latest)} post(s):")
        for post in latest:
            print(post)

def show_menu():
    print("\n📘 Blog System Menu:")
    print("1. Add Post")
    print("2. List All Posts")
    print("3. List Posts by Author")
    print("4. Delete a Post")
    print("5. Edit a Post")
    print("6. Show Latest Posts")
    print("7. Exit")

def main():
    blog = Blog()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            try:
                index = int(input("Enter the index of the post to delete: "))
                blog.delete_post(index)
            except ValueError:
                print("❌ Please enter a valid number.")


        elif choice == "5":
            blog.list_all_posts()
            try:
                index = int(input("Enter the index of the post to edit: "))
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                blog.edit_post(index, new_title, new_content)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "6":
            blog.display_latest_posts()

        elif choice == "7":
            print("👋 Exiting Blog System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
