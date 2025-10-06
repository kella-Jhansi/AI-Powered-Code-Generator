# 🤖 AI-Powered Code Generator

This project is an AI-powered tool that generates programming code (Python, JavaScript, or C++) from natural language prompts using a pre-trained Generative AI model (`Salesforce/codegen-350M-mono`) from Hugging Face Transformers.  

It provides a simple **web interface** using **Gradio** where users can describe their coding task, select a programming language, and get the generated code instantly.

---

## 🧠 Features
- Generate Python, JavaScript, or C++ code from natural language prompts.
- Simple web interface with **Gradio**.
- Interactive and easy to use.
- Can be extended to more programming languages or larger models.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** `transformers`, `torch`, `gradio`
- **Model:** `Salesforce/codegen-350M-mono`
- **Frontend:** Gradio (for web interface)

---

## 📂 Folder Structure

AI_Powered_Code_Generator/
│
├── ai_code_generator.py # Main project script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── assets/ # Optional folder for screenshots or images

## ⚡ Prerequisites

- Python 3.8 or higher installed
- Internet connection (to download model from Hugging Face)


## 💻 Installation & Setup

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/AI_Powered_Code_Generator.git
cd AI_Powered_Code_Generator
(Optional) Create a virtual environment:


python -m venv genai_env
# Windows
genai_env\Scripts\activate
# Linux / Mac
source genai_env/bin/activate
Install dependencies:

pip install -r requirements.txt
If you don’t have requirements.txt, install manually:

pip install transformers torch gradio
🚀 How to Run the Project
Open terminal inside the project folder.

Run the Python script:


python ai_code_generator.py
You will see a message like:


Running on local URL: http://127.0.0.1:7860
Open the URL in your browser to access the AI Code Generator UI.

📝 Example Usage
Prompt: Write a Python program to find factorial

Language: Python

Generated Code: Will display the Python code for factorial.

Prompt: Create a JavaScript function to reverse a string

Language: JavaScript

Generated Code: Will display the JavaScript function code.

Prompt: Write a C++ program for Fibonacci sequence

Language: C++

Generated Code: Will display the C++ program.

📌 Notes
The first time you run the project, the model will download (~1GB), which may take a few minutes.

For better performance, you can switch to a larger model like Salesforce/codegen-2B-mono if your system has enough resources.

Make sure your VS Code terminal is using the correct Python environment where gradio, torch, and transformers are installed.

📦 Optional: Saving Generated Code Automatically
You can modify ai_code_generator.py to save generated code into a folder like generated_codes/ with filenames based on language and timestamp.



