import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    update_listbox()
    clear_fields()

def update_contact():
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    contact = contacts[index]

    contact['name'] = name_entry.get()
    contact['phone'] = phone_entry.get()
    contact['email'] = email_entry.get()
    contact['address'] = address_entry.get()

    save_contacts(contacts)
    update_listbox()
    clear_fields()

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    del contacts[index]
    save_contacts(contacts)
    update_listbox()
    clear_fields()

def on_select(event):
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    address_entry.insert(0, contact["address"])

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone:")
    if not query:
        return
    result = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"]]
    listbox.delete(0, tk.END)
    for c in result:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

def update_listbox():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
contacts = load_contacts()

root = tk.Tk()
root.title("Contact Manager")


tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="e")

name_entry = tk.Entry(root, width=30)
phone_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
address_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add", width=12, command=add_contact).grid(row=4, column=0, pady=10)
tk.Button(root, text="Update", width=12, command=update_contact).grid(row=4, column=1)
tk.Button(root, text="Delete", width=12, command=delete_contact).grid(row=5, column=0)
tk.Button(root, text="Search", width=12, command=search_contact).grid(row=5, column=1)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

update_listbox()
root.mainloop()
