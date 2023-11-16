import os
import base64
import requests

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_image_description(image_path, api_key):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "can you give me a 2 sentence description of this image content, but not style? do not include parts like Digital Art Style of a The image depicts a"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 100
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

def process_images(folder_path, api_key, prefix=""):
    for image_file in os.listdir(folder_path):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, image_file)
            api_response = get_image_description(image_path, api_key)

            # Check if 'choices' key is in the response and if it contains items
            if 'choices' in api_response and api_response['choices']:
                description = api_response['choices'][0]['message']['content']
            else:
                # If not, there might be an error message in the response
                error_message = api_response.get('error', {}).get('message', 'No description available due to an error.')
                description = f"Error: {error_message}"
                print(description)

            full_description = f"{prefix} {description}"
            text_file_name = os.path.splitext(image_file)[0] + ".txt"
            text_file_path = os.path.join(folder_path, text_file_name)
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(full_description)


def main():
    api_key_file = 'api_key.txt'
    folder_path = os.getcwd()
    
    # Check if the API key file exists and read from it
    if os.path.exists(api_key_file):
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
        print("Using remembered API key.")
    else:
        api_key = input("What is your API key? ")
        remember_key = input("Do you want to remember the API key for next time? (yes/no): ").lower()
        if remember_key == 'yes':
            with open(api_key_file, 'w') as file:
                file.write(api_key)

    prefix_text = input("What Prefix Text do you want? ")
    image_location = input("Are your images in the folder where this Python script is? (yes/no): ").lower()

    if image_location != 'yes':
        folder_path = input("Where are your images? Provide the full path: ")

    process_images(folder_path, api_key, prefix_text)

if __name__ == "__main__":
    main()
