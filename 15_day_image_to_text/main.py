import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


output = query("sam.png")
print(output)
print(output[0]["generated_text"])
