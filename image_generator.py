from openai import OpenAI
import requests 

client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="skincare",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# post image


url = f"https://api.medium.com/v1/images"
token = "2b3516557518bf6300a05fe1748b8d84cb81bc5d2a9b2800f923bef4f1708f1dd"

post_data = {
        "url": image_url
    }

headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "multipart/form-data; boundary=FormBoundaryXYZ",
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
    }

response = requests.post(url, headers=headers, json=post_data)
if response.status_code == 201:
        post_details = response.json()
        print("Draft Post Created Successfully:")
        print("Post Details:")
        print(post_details)
else:
        print("Failed to create draft post. Status code:", response.status_code)
        print("Response:", response.text)

