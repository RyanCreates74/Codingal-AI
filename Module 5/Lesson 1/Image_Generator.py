from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from Config import HF_API_KEY
from colorama import Fore, init, Style

init()

MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5", # Fallback 2
]

client = InferenceClient(api_key=HF_API_KEY)
print(Fore.BLUE + f"Primary model: {MODELS[0]}")
print(Fore.RED + "Type 'quit' to exit\n")

while True:
    prompt = input(Fore.BLUE + "Enter prompt: ").strip()
    if prompt.lower() in ["quit", "exit", "q"]:
        break
    if not prompt:
        continue

    print(Fore.YELLOW + "Generating...")
    image = None

    for model in MODELS:
        try:
            image = client.text_to_image(prompt, model=model)
            break
        except Exception:
            print(Fore.RED + f"   Executing next...")
            continue

    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(Fore.GREEN + f"✓ Saved: {filename}")
        image.show()
        print()
    else:
        print(Fore.RED + "Error: All models failed. Please check your API key.\n")

print(Fore.BLUE + "Goodbye")