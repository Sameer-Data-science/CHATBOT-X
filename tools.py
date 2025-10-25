import json
from datetime import datetime

def get_menu(category=None):
    with open("menu.json", "r") as f:
        menu = json.load(f)

    if category:
        category = category.title()
        if category in menu:
            return f"{category}: " + ", ".join(menu[category])
        else:
            return "Sorry, that category isn't available."
    else:
        return "Menu categories: Starters, Main Course, Desserts, Drinks."

def book_table(name, time, people):
    try:
        datetime.strptime(time, "%H:%M")
        return f"✅ Table booked for {people} people under {name} at {time}."
    except:
        return "⚠️ Please provide time in 24-hour HH:MM format (e.g., 19:30 for 7:30 PM)."