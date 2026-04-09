import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from Config import HF_API_KEY

MODELS = [
    "ByteDance/SDXL-Lightning",
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-xl-base-1.0",
]

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Accept": "image/png"}

def generate_image_from_text(prompt):
    payload, last_err = {"inputs": prompt}, None
    for model in MODELS:
        url = f"https://router.huggingface.co/hf-inference/models/{model}"

        for _ in range(3):
            r = requests.post(url, headers=HEADERS, json=payload, timeout=120)
            ct = (r.headers.get("content-type") or "").lower()

            if r.status_code == 503 and "application/json" in ct:
                try:
                    wait_s = int(r.json().get("estimated_time", 5))
                except Exception:
                    wait_s = 5
                time.sleep(wait_s + 1)
                continue
            
            if r.status_code == 200 and "application/json" not in ct:
                try:
                    return Image.open(BytesIO(r.content)).convert("RGB")
                except Exception as e:
                    last_err = f"Request failed with status code 200: Could not decode image bytes: {e}"
                    break
            
            try:
                body = r.json() if "application/json" in ct else r.text
            except Exception:
                body = r.text()
            last_err = f"Request failed with status code {r.status_code}: {body}"
            break

    raise Exception(last_err or "Request failed with status code 500: Uknown error")

def Daytime(image):
    image = ImageEnhance.Brightness(image).enhance(1.5)
    image = ImageEnhance.Contrast(image).enhance(1.1)
    return image.filter(ImageFilter.GaussianBlur(radius=2))
def Nightime(image):
    mage = ImageEnhance.Brightness(image).enhance(0.8)
    image = ImageEnhance.Contrast(image).enhance(1.4)
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image from text and applies post-processing effects.")
    print("Type 'exit' to quit anytime.\n")

    while True:
        user_input = input("Enter a prompt for the image (or 'exit' to quit): \n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating Image...")
            image = generate_image_from_text(user_input)
            q = input("Would you like your image to have a daytime or nightime mood?").lower()
            print(f"Applying post-processing effects for {q} mood\n")
            if q == 'daytime':
                processed_image = Daytime(image)
                processed_image.show()
            elif q == 'nightime':
                processed_image = Nightime(image)
                processed_image.show()

            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")

            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error has occured: {e}\n")
    
if __name__ == "__main__":
    main()