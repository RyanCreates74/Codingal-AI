import requests
def get_random_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    if response.status_code == 200:
        # print(f"Full JSON Response: {response.json()}")
        fact_data = response.json()
        return fact_data['fact']
    
print("Hi, welcome to the cat fact generator!")
    
while True:
    option = input("Press enter if you would like to receive a fact, or 'q' to quit the programme: ")
    if option.lower() == 'q':
        break
    else:
        print(get_random_fact())