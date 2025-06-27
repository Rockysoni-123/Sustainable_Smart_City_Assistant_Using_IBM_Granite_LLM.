# granite_llm.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def main():
    # 1. Choose model: pick a Granite code model
    model_name = "ibm-granite/granite-8b-code-instruct-128k"

    # 2. Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # or "cpu"
        torch_dtype=torch.float16  # if using GPU
    )
    model.eval()

    # 3. Prepare your prompt
    prompt = """\
# Question:
Write a Python function called 'first_repeated' that takes a string and returns the first character that appears more than once.
# Answer:
"""

    # 4. Tokenize and generate
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        temperature=0.2,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )

    # 5. Decode and display
    generated = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)
    print("Generated code:\n", generated)

if __name__ == "__main__":
    main()
