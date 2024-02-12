import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
import pytz

def get_time(city):
    cities = {
        "Karachi": "Asia/Karachi",
        "Delhi": "Asia/Kolkata",
        "Toronto": "America/Toronto"
    }

    timezone = pytz.timezone(cities[city])
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time in {city}: {formatted_time}")

def main():
    root = tk.Tk()
    root.withdraw()

    city = simpledialog.askstring("Input", "Choose a city (Karachi, Delhi, Toronto):", parent=root)

    if city not in ["Karachi", "Delhi", "Toronto"]:
        print("Invalid city entered.")
        return

    get_time(city)

if __name__ == "__main__":
    main()
