import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class Task:
    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        self.id = self._generate_id()
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def _generate_id(self) -> str:
        return str(int(datetime.now().timestamp() * 1000))
    
    def mark_completed(self):
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        task = cls(data['title'], data.get('description', ''), data.get('priority', 'medium'))
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        task.completed_at = data.get('completed_at')
        return task

class TaskTracker:
    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> Task:
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def complete_task(self, task_id: str) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id: str) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                return True
        return False
    
    def list_incomplete_tasks(self) -> List[Task]:
        return [task for task in self.tasks if not task.completed]
    
    def list_all_tasks(self) -> List[Task]:
        return self.tasks
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_tasks(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError):
                self.tasks = []
        else:
            self.tasks = []

def display_tasks(tasks: List[Task], title: str = "Tasks"):
    if not tasks:
        print(f"\n{title}: No tasks found.")
        return
    
    print(f"\n{title}:")
    print("-" * 80)
    print(f"{'ID':<12} {'Status':<10} {'Priority':<8} {'Title':<30} {'Description':<20}")
    print("-" * 80)
    
    for task in tasks:
        status = "✓" if task.completed else "○"
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task.priority, "🟡")
        title_truncated = task.title[:27] + "..." if len(task.title) > 30 else task.title
        desc_truncated = task.description[:17] + "..." if len(task.description) > 20 else task.description
        
        print(f"{task.id:<12} {status:<10} {priority_icon:<8} {title_truncated:<30} {desc_truncated:<20}")

def main():
    tracker = TaskTracker()
    
    print("🎯 Welcome to Task Tracker Agent!")
    print("=" * 50)
    
    while True:
        print("\n📋 Available Commands:")
        print("1. add <title> [description] [priority] - Add a new task")
        print("2. complete <task_id> - Mark task as completed")
        print("3. list - Show incomplete tasks")
        print("4. list all - Show all tasks")
        print("5. delete <task_id> - Delete a task")
        print("6. help - Show this help message")
        print("7. quit - Exit the application")
        
        try:
            command = input("\n🤖 Enter command: ").strip().lower()
            
            if command == "quit" or command == "exit":
                print("👋 Goodbye! Your tasks have been saved.")
                break
            
            elif command == "help":
                continue
            
            elif command.startswith("add "):
                parts = command[4:].split(" ", 2)
                title = parts[0]
                description = parts[1] if len(parts) > 1 else ""
                priority = parts[2] if len(parts) > 2 else "medium"
                
                if priority not in ["high", "medium", "low"]:
                    priority = "medium"
                
                task = tracker.add_task(title, description, priority)
                print(f"✅ Task added successfully! ID: {task.id}")
            
            elif command.startswith("complete "):
                task_id = command[9:].strip()
                if tracker.complete_task(task_id):
                    print(f"✅ Task {task_id} marked as completed!")
                else:
                    print(f"❌ Task {task_id} not found.")
            
            elif command == "list":
                incomplete_tasks = tracker.list_incomplete_tasks()
                display_tasks(incomplete_tasks, "Incomplete Tasks")
            
            elif command == "list all":
                all_tasks = tracker.list_all_tasks()
                display_tasks(all_tasks, "All Tasks")
            
            elif command.startswith("delete "):
                task_id = command[7:].strip()
                if tracker.delete_task(task_id):
                    print(f"🗑️ Task {task_id} deleted successfully!")
                else:
                    print(f"❌ Task {task_id} not found.")
            
            else:
                print("❌ Invalid command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye! Your tasks have been saved.")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
