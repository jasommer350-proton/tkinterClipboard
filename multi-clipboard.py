import tkinter as tk
from tkinter import messagebox
from multiClipboardList import MultiClipboardList

# Store clipboard values 
clipboard_list = MultiClipboardList()

def save_clipboard():
    name = entry.get()

    if clipboard_list.item_exists(name):
        messagebox.showwarning("Warning", "Name already exists")
        return
    elif len(clipboard_list) > 2:
        if messagebox.askyesno("At multi-clipboard limit of 5","At limit of what can be saved, do you want to remove the oldest item?"):
            clipboard_list.delete_last_item()
        else:
            messagebox.showinfo("Make a change", "Before adding another remove one of your choice.")
            return
    
    clipboard_list.add_item(name,root.clipboard_get())
    
    update_list() 
    
    #clears the entry input
    entry.delete(0, "end")

def get_clipboard(name):
    if clipboard_list.item_exists(name):
        root.clipboard_clear() 
        root.clipboard_append(clipboard_list.get_item_by_name(name))
    else:
        messagebox.showwarning("Not found", "No clipboard saved with name " + name)

def update_list():
    listbox.delete(0, listbox.size()-1)
    for item in clipboard_list:
        listbox.insert(1,item.name)

def delete_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        deletedItem = listbox.get(index)
        listbox.delete(index)
        clipboard_list.delete_item_by_name(deletedItem)

def update_entry(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        data = listbox.get(index)
        entry.delete(0, "end")
        entry.insert(0, data)


root = tk.Tk()

label = tk.Label(text="Name:")
label.pack()

entry = tk.Entry(root) 
entry.pack()

listbox = tk.Listbox(root)
listbox.pack()
listbox.bind('<Delete>', delete_selected)
listbox.bind("<<ListboxSelect>>", update_entry)

save_button = tk.Button(text="Save Clipboard", command=save_clipboard)
save_button.pack()

get_button = tk.Button(text="Get Clipboard", 
                    command=lambda: get_clipboard(entry.get()))  
get_button.pack()

delete_btn = tk.Button(root, text="Delete", command=delete_selected)
delete_btn.pack()

def main():
    root.mainloop()
    
if __name__ == "__main__":
    main()