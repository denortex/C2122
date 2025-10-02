class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Виконано" if self.completed else "❌ Не виконано"
        return f"{self.title} | {self.description} | Дедлайн: {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [t for t in self.tasks if t.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def show_tasks(self):
        if not self.tasks:
            print("Немає завдань.")
        for task in self.tasks:
            print(task)

tm = TaskManager()
tm.add_task(Task("Лабораторна", "Зробити завдання з Python", "05.10.2025"))
tm.add_task(Task("Прибрати", "Пропилососити кімнату", "03.10.2025"))

tm.show_tasks()
tm.mark_task_completed("Лабораторна")
print("\nПісля виконання:")
tm.show_tasks()
