import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self,root):
        self.root =root
        self.root.title("To-Do-List-App")
        self.root.configure(bg="beige") 

        self.menu = tk.Menu(root,bg="black",fg="white")
        self.root.config(menu=self.menu)

        self.tasks = []
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(padx=10, pady=5, fill=tk.X)

        self.add_button = HoverButton(root,text="Add The Task",command=self.add_task, relief=tk.RIDGE,bg="blue",fg="white",borderwidth=3,padx=10,pady=8,activebackground="darkblue", cursor="hand2", width=100)
        self.add_button.pack(padx=10, pady=(20, 5)) 
        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.mark_done_button = HoverButton(root, text="Mark As Done", command=self.mark_task_done, relief=tk.RIDGE, bg="green", fg="white", borderwidth=3, padx=10, pady=8, activebackground="darkgreen", cursor="hand2", width=100)
        self.mark_done_button.pack(padx=10, pady=5)

        self.remove_button = HoverButton(root, text="Remove The Task", command=self.remove_task, relief=tk.RIDGE, bg="red", fg="white", borderwidth=3, padx=10, pady=8, activebackground="darkred", cursor="hand2", width=100)
        self.remove_button.pack(padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"description": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def mark_task_done(self):
        selected_index =self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"]=True
            self.update_task_list()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task_info in self.tasks:
            status = "Done" if task_info["completed"] else "Not Done"
            self.task_listbox.insert(tk.END, f"[{status}] {task_info['description']}")

class HoverButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.default_bg = self["bg"]
        self.bind("<Enter>",self.on_enter)
        self.bind("<Leave>",self.on_leave)
    
    def on_enter(self, event):
        self["bg"] = "lightgray"
    
    def on_leave(self,event):
        self["bg"]=self.default_bg
            

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()