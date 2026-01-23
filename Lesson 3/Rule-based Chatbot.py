import re
import random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)


destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

weather_samples = ["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "windy 🌬️"]

city_timezones = {
    "tokyo": 9,
    "paris": 1,
    "new york": -5
}

# Simple memory
memory = {
    "name": None,
    "last_destination": None
}


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def print_bot(text, color=Fore.CYAN):
    print(color + "TravelBot: " + text)


def recommend():
    while True:
        print_bot("Do you prefer beaches, mountains, or cities?")
        choice = normalize(input(Fore.YELLOW + "You: "))

        for key in destinations:
            if key in choice:
                suggestion = random.choice(destinations[key])
                memory["last_destination"] = suggestion
                print_bot(f"How about {suggestion}?", Fore.GREEN)
                answer = normalize(input(Fore.YELLOW + "You (yes/no): "))

                if "yes" in answer:
                    print_bot(f"Amazing! Enjoy {suggestion}! ✈️", Fore.GREEN)
                    return
                elif "no" in answer:
                    print_bot("Okay, let me try again...", Fore.RED)
                    break
                else:
                    print_bot("Please answer yes or no.", Fore.RED)
                    break
        else:
            print_bot("I don't recognize that destination type.", Fore.RED)
            show_help()
            return

def packing_tips():
    print_bot("Where are you traveling?")
    location = input(Fore.YELLOW + "You: ")
    print_bot("How many days?")
    days = input(Fore.YELLOW + "You: ")

    print_bot(f"Packing tips for {days} days in {location}:", Fore.GREEN)
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers and adapters")
    print(Fore.GREEN + "- Check the weather forecast")

def tell_joke():
    print_bot(random.choice(jokes), Fore.YELLOW)

def weather_info():
    print_bot("Which city?")
    city = normalize(input(Fore.YELLOW + "You: "))
    print_bot(f"The weather in {city.title()} is {random.choice(weather_samples)}.", Fore.GREEN)

def local_time():
    print_bot("Which city?")
    city = normalize(input(Fore.YELLOW + "You: "))

    if city in city_timezones:
        hour = (datetime.utcnow().hour + city_timezones[city]) % 24
        print_bot(f"Local time in {city.title()} is {hour}:00.", Fore.GREEN)
    else:
        print_bot("Sorry, I don't have time data for that city.", Fore.RED)

def recall_memory():
    if memory["last_destination"]:
        print_bot(f"Last place I suggested was {memory['last_destination']}.", Fore.GREEN)
    else:
        print_bot("I don't remember any destinations yet.", Fore.RED)


def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Recommend travel destinations")
    print(Fore.GREEN + "- Give packing tips")
    print(Fore.GREEN + "- Share weather info")
    print(Fore.GREEN + "- Tell local time in cities")
    print(Fore.GREEN + "- Tell a joke")
    print(Fore.GREEN + "- Remember your last destination")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to quit\n")


def chat():
    print_bot("Hello! I'm TravelBot ✈️")
    memory["name"] = input(Fore.YELLOW + "Your name: ")
    print_bot(f"Nice to meet you, {memory['name']}!", Fore.GREEN)

    show_help()

    while True:
        user_input = normalize(input(Fore.YELLOW + f"{memory['name']}: "))

        if re.search(r"recommend|suggest|travel", user_input):
            recommend()
        elif re.search(r"pack", user_input):
            packing_tips()
        elif re.search(r"joke|funny", user_input):
            tell_joke()
        elif re.search(r"weather", user_input):
            weather_info()
        elif re.search(r"time|clock", user_input):
            local_time()
        elif re.search(r"remember|memory", user_input):
            recall_memory()
        elif re.search(r"help", user_input):
            show_help()
        elif re.search(r"exit|bye|quit", user_input):
            print_bot("Safe travels! Goodbye 👋")
            break
        else:
            print_bot("I didn't quite get that. Try 'help'.", Fore.RED)



if __name__ == "__main__":
    chat()