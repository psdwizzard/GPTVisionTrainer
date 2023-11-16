<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>GPTVisionTrainer</h1>

<h3>Description</h3>
<p>This Python project is designed to prepare training data for Stable Diffusion models by generating detailed descriptions of images using OpenAI's GPT Vision API. It's ideal for those looking to enhance their machine learning models, particularly in the realm of image processing and generation. The script allows for the addition of custom prompts to each description, providing a unique way to tailor the dataset to specific training needs.</p>

<h3>Features</h3>
<ul>
    <li><strong>Stable Diffusion Training Data Preparation</strong>: Automates the generation of descriptive texts for images, tailored for training Stable Diffusion models.</li>
    <li><strong>Custom Prompt Integration</strong>: Enables the addition of custom prompts to image descriptions, offering personalized context or thematic focus.</li>
    <li><strong>File Management</strong>: Saves each image's description as a text file with the corresponding image name, ensuring organized data management.</li>
    <li><strong>Secure API Key Handling</strong>: The script prompts for the OpenAI API key during runtime and saves it locally for future use. Note: The API key is stored in plain text, so ensure its security.</li>
</ul>

<h3>Technologies Used</h3>
<ul>
    <li><strong>Python</strong>: Built with Python, leveraging its capabilities for seamless file handling and API interactions.</li>
    <li><strong>OpenAI's GPT API</strong>: Utilizes OpenAI's GPT API for accurate and context-rich image descriptions.</li>
</ul>

<h3>How to Use</h3>
<ol>
    <li>Clone the repository to your local machine.</li>
    <li>Install the required Python package. Run the following command in your terminal: <br>
    <code>pip install requests</code></li>
    <li>Run the script. It will prompt you for the OpenAI API key, which will be saved locally for subsequent uses. (Warning: The API key is stored in plain text. Ensure to secure the file where it is saved.)</li>
    <li>Specify the path to the folder containing the images you wish to process.</li>
    <li>The script will generate and save descriptions, with your custom prompt, for each image as text files in the same folder.</li>
</ol>

<h3>Contribution</h3>
<p>Your contributions are welcome! Feel free to suggest improvements, whether it's in enhancing the script's efficiency, adding more sophisticated error handling, or proposing new features. Fork the repository, make your changes, and submit a pull request.</p>

<h3>License</h3>
<p>This project is open-sourced under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>

</body>
</html>
