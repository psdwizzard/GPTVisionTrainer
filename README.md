# GPTVisionTrainer
This Python project is designed to prepare training data for Stable Diffusion models by generating detailed descriptions of images using OpenAI's GPT Vision API.
This Python project is designed to prepare training data for Stable Diffusion models by generating detailed descriptions of images using OpenAI's GPT Vision API. It's ideal for those looking to enhance their machine learning models, particularly in the realm of image processing and generation. The script allows for the addition of custom prompts to each description, providing a unique way to tailor the dataset to specific training needs.

Features
Stable Diffusion Training Data Preparation: Automates the generation of descriptive texts for images, tailored for training Stable Diffusion models.
Custom Prompt Integration: Enables the addition of custom prompts to image descriptions, offering personalized context or thematic focus.
File Management: Saves each image's description as a text file with the corresponding image name, ensuring organized data management.
Secure API Key Handling: The script prompts for the OpenAI API key during runtime and saves it locally for future use. Note: The API key is stored in plain text, so ensure its security.
Technologies Used
Python: Built with Python, leveraging its capabilities for seamless file handling and API interactions.
OpenAI's GPT API: Utilizes OpenAI's GPT API for accurate and context-rich image descriptions.
How to Use
Clone the repository to your local machine.
Install the required Python package. Run the following command in your terminal:
Copy code
pip install requests
Run the script. It will prompt you for the OpenAI API key, which will be saved locally for subsequent uses. (Warning: The API key is stored in plain text. Ensure to secure the file where it is saved.)
Specify the path to the folder containing the images you wish to process.
The script will generate and save descriptions, with your custom prompt, for each image as text files in the same folder.
Contribution
Your contributions are welcome! Feel free to suggest improvements, whether it's in enhancing the script's efficiency, adding more sophisticated error handling, or proposing new features. Fork the repository, make your changes, and submit a pull request.

License
This project is open-sourced under the MIT License.

This revised description now better aligns with your project's focus on Stable Diffusion training data preparation and highlights the new functionalities and warnings regarding API key storage. Feel free to further tailor it to match your project's specifics.
