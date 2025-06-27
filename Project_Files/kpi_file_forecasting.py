# kpi_file_forecasting.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
import torch


def load_kpi_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n[INFO] KPI Data Loaded:\n")
        print(df.head())
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load KPI data: {e}")
        return None

def forecast_kpi_with_llm(df, model_name="ibm-granite/granite-8b-code-instruct-128k"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    model.eval()

    # Convert KPI rows to prompt string
    prompt = "Analyze the following KPI data for trends and forecast insights:\n\n"
    prompt += df.head(5).to_string(index=False)  # Include only first 5 rows to fit token limits
    prompt += "\n\nBased on the above data, what are the key insights and future trends?"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.5,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)
    print("\n🔍 Forecast/Analysis from Granite LLM:\n")
    print(result)

def main():
    file_path = "data/city_kpis.csv"  # Modify if your CSV file is elsewhere
    df = load_kpi_data(file_path)
    if df is not None:
        forecast_kpi_with_llm(df)

if __name__ == "__main__":
    main()