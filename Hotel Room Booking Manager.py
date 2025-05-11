import json
import os
import tkinter as tk
from tkinter import messagebox

# Folder and file setup
DATA_FOLDER = "data"
BOOKINGS_FILE = os.path.join(DATA_FOLDER, "hotel_bookings.json")

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Room data (12 rooms now)
rooms = {
    "101": {"type": "Single", "price": 100},
    "102": {"type": "Double", "price": 150},
    "103": {"type": "Single", "price": 100},
    "104": {"type": "Double", "price": 150},
    "105": {"type": "Suite", "price": 250},
    "106": {"type": "Suite", "price": 250},
    "201": {"type": "Single", "price": 100},
    "202": {"type": "Double", "price": 150},
    "203": {"type": "Single", "price": 100},
    "204": {"type": "Double", "price": 150},
    "205": {"type": "Suite", "price": 250},
    "206": {"type": "Suite", "price": 250}
}

# Load bookings from JSON file
def load_bookings():
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save bookings to file
def save_bookings(bookings):
    with open(BOOKINGS_FILE, "w") as file:
        json.dump(bookings, file, indent=4)

# Show available rooms
def get_available_rooms():
    bookings = load_bookings()
    available = []
    for room_no, details in rooms.items():
        if room_no not in bookings:
            available.append(f"{room_no} - {details['type']} - ${details['price']}")
    return available

def update_available_listbox():
    available_listbox.delete(0, tk.END)
    for room in get_available_rooms():
        available_listbox.insert(tk.END, room)

# Book a room
def book_room():
    room_no = room_entry.get().strip()
    guest = name_entry.get().strip()
    try:
        days = int(days_entry.get().strip())
        if days <= 0:
            raise ValueError("Days must be positive.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number of days.")
        return

    if room_no not in rooms:
        messagebox.showerror("Error", "Room does not exist.")
        return

    bookings = load_bookings()
    if room_no in bookings:
        messagebox.showwarning("Unavailable", "Room already booked.")
        return

    total = rooms[room_no]['price'] * days
    bookings[room_no] = {"guest": guest, "days": days, "total": total}
    save_bookings(bookings)  # Save the booking to the file immediately
    messagebox.showinfo("Booked", f"Room {room_no} booked for {guest}.\nTotal: ${total}")
    update_available_listbox()

# View bookings
def view_bookings():
    bookings = load_bookings()
    if not bookings:
        messagebox.showinfo("Bookings", "No current bookings.")
        return
    info = ""
    for room_no, data in bookings.items():
        info += f"Room {room_no} - Guest: {data['guest']} - Days: {data['days']} - Total: ${data['total']}\n"
    messagebox.showinfo("Current Bookings", info)

# Checkout (remove booking from file)
def checkout_room():
    room_no = room_entry.get().strip()
    bookings = load_bookings()
    
    if room_no in bookings:
        del bookings[room_no]  # Remove the booking
        save_bookings(bookings)  # Save the updated bookings list
        messagebox.showinfo("Checked Out", f"Room {room_no} is now available.")
        update_available_listbox()
        clear_fields()  # Clear the fields after checkout
    else:
        messagebox.showwarning("Error", "Room not booked or doesn't exist.")

# Delete a booking (remove booking from the file)
def delete_booking():
    room_no = room_entry.get().strip()
    bookings = load_bookings()
    
    if room_no in bookings:
        del bookings[room_no]  # Remove the booking from the file
        save_bookings(bookings)  # Save the updated bookings list
        messagebox.showinfo("Deleted", f"Booking for room {room_no} has been deleted.")
        update_available_listbox()
        clear_fields()  # Clear the fields after deletion
    else:
        messagebox.showwarning("Error", "Room not booked or doesn't exist.")

# Clear all input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Hotel Room Booking Manager")
root.geometry("500x600")
root.configure(bg="#e6f7ff")  # light blue background

title_label = tk.Label(root, text="Hotel Room Booking Manager", font=("Helvetica", 18, "bold"), fg="green", bg="#e6f7ff")
title_label.pack(pady=10)

# Guest name
tk.Label(root, text="Guest Name:", bg="#e6f7ff", fg="blue").pack()
name_entry = tk.Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=5)

# Room number
tk.Label(root, text="Room Number:", bg="#e6f7ff", fg="blue").pack()
room_entry = tk.Entry(root, font=("Helvetica", 12))
room_entry.pack(pady=5)

# Number of days
tk.Label(root, text="Number of Days:", bg="#e6f7ff", fg="blue").pack()
days_entry = tk.Entry(root, font=("Helvetica", 12))
days_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#e6f7ff")
button_frame.pack(pady=15)

book_btn = tk.Button(button_frame, text="Book Room", command=book_room, bg="green", fg="white", width=15)
book_btn.grid(row=0, column=0, padx=5, pady=5)

checkout_btn = tk.Button(button_frame, text="Checkout Room", command=checkout_room, bg="red", fg="white", width=15)
checkout_btn.grid(row=0, column=1, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Booking", command=delete_booking, bg="orange", fg="white", width=15)
delete_btn.grid(row=1, column=0, columnspan=2, pady=10)

clear_btn = tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="#555555", fg="white", width=15)
clear_btn.grid(row=2, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View Current Bookings", command=view_bookings, bg="blue", fg="white", width=35)
view_btn.pack(pady=10)

# Available rooms
tk.Label(root, text="Available Rooms", font=("Helvetica", 14), fg="green", bg="#e6f7ff").pack(pady=5)
available_listbox = tk.Listbox(root, height=8, width=40, font=("Helvetica", 12))
available_listbox.pack()

# Load initial available rooms
update_available_listbox()

root.mainloop()