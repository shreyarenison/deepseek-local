from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="TheBloke/deepseek-coder-1.3b-instruct-GGUF",
    filename="deepseek-coder-1.3b-instruct.Q4_K_M.gguf",
    local_dir="models/deepseek",
    repo_type="model"
)

print("Model downloaded to:", file_path)
