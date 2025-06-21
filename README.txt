DeepSeek Coder 1.3B - Local Setup (Offline)

This project lets you run the DeepSeek Coder model locally on your Windows PC using llama.cpp. No GPU needed. Works completely offline after setup.

---------------------------------------
Project Structure
---------------------------------------

deepseek_local_project/
├── llama.cpp/                (contains built llama.cpp files)
├── models/
│   └── deepseek/             (this is where the model file will go)
├── run.bat                   (double-click to start the model)
├── download_model.py         (optional script to download the model)
└── README.txt                

---------------------------------------
System Requirements
---------------------------------------

- Windows 10 or 11 (64-bit)
- Python 3.8 or higher
- Internet connection (for setup only)
- Basic CPU with AVX2 (most modern PCs have this)

---------------------------------------
Step 1: Install Python and Tools
---------------------------------------

1. Download and install Python from: https://www.python.org
2. Open Command Prompt and run:
   pip install huggingface_hub

3. Then login to Hugging Face:
   huggingface-cli login
   (You'll need a free account and token from: https://huggingface.co/settings/tokens)

---------------------------------------
Step 2: Download the Model File
---------------------------------------

Option A (Recommended):
Run this command:
   python download_model.py

Option B (Manual):
Run this command:
   huggingface-cli download TheBloke/deepseek-coder-1.3b-instruct-GGUF deepseek-coder-1.3b-instruct.Q4_K_M.gguf --local-dir ./models/deepseek

After download, your model file should be here:
   models/deepseek/deepseek-coder-1.3b-instruct.Q4_K_M.gguf

---------------------------------------
Step 3: Run the Model
---------------------------------------

Double-click the `run.bat` file
OR
Open Command Prompt and run:
   cd llama.cpp\build\bin\Release
   llama-cli.exe -m "..\..\..\models\deepseek\deepseek-coder-1.3b-instruct.Q4_K_M.gguf" -i

This will start the chatbot in your terminal.

---------------------------------------
Examples of What to Ask
---------------------------------------

- Explain recursion in Python.
- Write a function to reverse a string in JavaScript.
- What is the difference between list and tuple in Python?

To exit, press Ctrl + C.

---------------------------------------
Important Note
---------------------------------------

Do not share the model (.gguf) file. Each user must download it from Hugging Face due to licensing rules.

---------------------------------------
For offline and personal use only.
