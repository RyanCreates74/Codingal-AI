print('Hi, I am an AI chatbot, what is your name?')
name = input()
print('Nice to meet you', name)
print('Are you feeling good/bad today', name, '?')
mood = input().lower()
if mood == 'good':
    print("Nice to hear that! Have a great day")
elif mood == 'bad':
    print("Sorry to hear that, hope your day improves.")
else:
    print("I know it can be hard to put feelings into words!")

print(f"It was nice meeting you {name}, see you soon!")