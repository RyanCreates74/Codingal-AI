import requests
import sys
import time
from colorama import Fore, Style, init
init(autoreset=True)

history = []
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(Fore.RED + "Did you know? ")
        history.append(fact_data['text'])
        type_text(fact_data['text'])
        print(Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Failed to fetch fact")

while True:
    user_input = input(Fore.YELLOW + "Press enter to get a random technology fact, 'h' to see history or press 'q' to quit the program: ")
    if user_input.lower() == 'q':
        break
    elif user_input.lower() == 'h':
        if history:
            print(history)
            break
    get_random_technology_fact()