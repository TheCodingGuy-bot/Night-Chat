# Import necessary libraries
from transformers import AutoModelForCausalLM, AutoTokenizer

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

# Main function to run OpenAssistant with integrated MPT-7B-Chat model
def main():
    print("Welcome to the MPT-7B-Chat integrated OpenAssistant!")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input)
        print("Assistant: ", response)

if __name__ == "__main__":
    main()
