import random
import time

greetings = [
    "Hello, magnificent human!",
    "Hey hey! Ready to take over the codeverse?",
    "Nyx says hi! 🐾",
    "Coding powers... ACTIVATED!",
    "You're doing amazing, sweetie 💻✨",
    "Don't forget to hydrate!",
    "Beep bop! Python says you're awesome."
]

def show_greeting():
    print("✨ Fun Greeting Generator ✨")
    time.sleep(1)
    print(random.choice(greetings))
    print("\n--- End of Transmission ---")

if __name__ == "__main__":
    show_greeting()
