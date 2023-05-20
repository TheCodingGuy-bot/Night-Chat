# Import necessary libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests

# Function to download large files in chunks
def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename

# Load MPT-7B-Chat model and tokenizer
model_name = "mosaicml/mpt-7b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

# Function to generate response using MPT-7B-Chat model
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

# Download the large file
url = "https://example.com/large_file.tar.gz"
download_file(url)

# Main function to run OpenAssistant with integrated MPT-7B-Chat model
def main():
    print("Welcome to Night-Chat!")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input)
        print("Assistant: ", response)

if __name__ == "__main__":
    main()
