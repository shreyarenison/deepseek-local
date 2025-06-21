@echo off
echo Downloading model if not already present...
python download_model.py

echo.
echo Running DeepSeek Model...
set /p prompt=Enter your question: 
llama.cpp\build\bin\Release\llama-cli.exe -m "models\deepseek\deepseek-coder-1.3b-instruct.Q4_K_M.gguf" -p "%prompt%"
