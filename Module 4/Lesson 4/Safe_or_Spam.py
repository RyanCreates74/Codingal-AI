import requests
from Config import HF_API_KEY

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

LABELS = ["Safe", "Spam"]

def ask_hf(text: str):
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": LABELS}
    }

    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")

    return r.json()

def normalize_preds(preds):
    # Handles both HF response formats

    # Case 1: list of dicts
    if isinstance(preds, list):
        labels = [p["label"] for p in preds]
        scores = [p["score"] for p in preds]
        return labels, scores

    # Case 2: dict with labels/scores
    elif isinstance(preds, dict):
        return preds["labels"], preds["scores"]

    else:
        raise ValueError("Unknown prediction format")

def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(text: str, preds):
    labels, scores = normalize_preds(preds)

    print("\n" + "=" * 60)
    print("🛡️ Spam Detection Classifier")
    print("=" * 60)
    print("Text:", text)

    top_label = labels[0]
    top_score = scores[0]

    print(f"\nPrediction: {top_label}")
    print(f"Confidence: {round(top_score * 100, 1)}% [{bar(top_score)}]")

    print("\nAll scores:")
    for label, score in zip(labels, scores):
        print(f"- {label:<5} {round(score * 100, 1)}% [{bar(score)}]")

    print("=" * 60)

def main():
    print("Welcome! Type a message and I'll classify it as Safe or Spam.")
    print("Type 'exit' to stop.\n")

    while True:
        text = input("Message: ").strip()

        if text.lower() == "exit":
            print("Bye! 👋")
            break

        if not text:
            print("Please type something.\n")
            continue

        try:
            preds = ask_hf(text)

            if isinstance(preds, (list, dict)):
                show(text, preds)
            else:
                print("Unexpected response:", preds)

        except Exception as e:
            print("\n⚠️ Error occurred:")
            print("Reason:", e)
            print("Tip: Check API key and internet connection.\n")

if __name__ == "__main__":
    main()