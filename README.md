# Hotel Room Booking Manager

## Description

The **Hotel Room Booking Manager** is a simple Python-based application that allows a user to manage hotel room bookings using a graphical interface. The application provides features such as:

- Booking rooms for guests.
- Checking out rooms and making them available.
- Viewing all current bookings.
- Deleting bookings if necessary.
- Managing room availability.

The data is stored in a **JSON file**, which is read and written every time the user interacts with the system. This ensures that bookings are saved even after the application is closed and reopened.

## Features

- **Book a Room**: Allows users to book available rooms by entering the guest name, room number, and the number of days.
- **View Current Bookings**: Displays a list of all the current bookings.
- **Checkout Room**: Users can check out by removing a room's booking, making it available again.
- **Delete Booking**: Allows for the deletion of a room's booking, freeing up the room for future reservations.
- **Clear Fields**: Clears input fields after a booking or checkout operation.

## Libraries Used

- **Tkinter**: A built-in Python library for creating graphical user interfaces (GUIs). It's used here to create the window, input fields, buttons, and display the room bookings.
- **JSON**: A built-in Python library for working with JSON data. It's used to save and load the hotel bookings to and from a `.json` file.

## Requirements

To run this project, you need Python installed on your machine. The following libraries should be available by default in any standard Python installation:

- **tkinter**
- **json**
- **os**
