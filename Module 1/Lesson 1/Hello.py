print("🤖 Hey! I'm your friendly AI chatbot.\n")

name = input("What's your name? 😊 ")
print(f"\nNice to meet you, {name}! 👋")

mood = input("How are you feeling today? (good / bad / okay): ").lower()

if mood in ["good", "great", "awesome", "happy"]:
    print("That's amazing! 🌟 Love that energy!")
elif mood in ["bad", "sad", "tired", "not good"]:
    print("I'm sorry to hear that 💙 Hope things get better soon.")
elif mood in ["okay", "fine", "meh"]:
    print("Totally understandable 😌 Some days are just 'okay'.")
else:
    print("Thanks for sharing — emotions can be complicated 💭")

activity = input("\nWhat are you up to right now? ")
print(f"Oh nice! {activity} sounds interesting 😄")

hobby = input("\nWhat's something you enjoy doing in your free time? ")
print(f"{hobby}? That sounds fun! 🎉")


like_chat = input("\nDo you like chatting with AI bots? (yes / no): ").lower()

if like_chat == "yes":
    print("Yay! 🤖 I'm happy you enjoy chatting with me!")
elif like_chat == "no":
    print("That's okay! Thanks for giving me a chance 😊")
else:
    print("Interesting answer! 😄")

print(f"\nIt was really nice talking to you, {name}! 💬")
print("Take care and have a great day! 👋😊")