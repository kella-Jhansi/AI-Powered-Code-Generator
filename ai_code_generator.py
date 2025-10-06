from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load CodeGen model
model_name = "Salesforce/codegen-350M-mono"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate code only
def generate_code(prompt, language):
    # Prompt explicitly instructs model to generate only code
    full_prompt = f"# Write ONLY {language} code for the following task. Do NOT provide output or explanations.\n# Task: {prompt}\n"
    
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.7,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    clean_code = code.replace(full_prompt, "").strip()
    return clean_code

# Gradio interface
interface = gr.Interface(
    fn=generate_code,
    inputs=[
        gr.Textbox(
            label="Describe Your Code Task",
            placeholder="Example: Write a function to calculate factorial"
        ),
        gr.Dropdown(
            choices=["Python", "C++", "JavaScript"],
            label="Select Programming Language"
        )
    ],
    outputs=gr.Code(label="Generated Code"),
    title="🤖 AI Code Generator",
    description="Enter a task, and get the code in Python, C++, or JavaScript. Only code will be generated, no outputs."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
