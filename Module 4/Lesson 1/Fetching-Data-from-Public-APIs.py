import requests
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        # print(f"Full JSON Response: {response.json()}")
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"

    else:
        return "Failed to retrieve joke"
    
def main():
    print("Welcome to the random joke generator!")
    
    while True:
        joke = get_random_joke()
        print(joke)
        user_input = input("Press enter to get a new joke, or type 'q' or 'exit' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()