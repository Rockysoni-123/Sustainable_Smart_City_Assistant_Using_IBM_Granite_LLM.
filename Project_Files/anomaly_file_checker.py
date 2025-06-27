# anomaly_file_checker.py

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "ibm-granite/granite-8b-code-instruct-128k"

def load_kpi_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("[INFO] KPI data loaded successfully.")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load KPI file: {e}")
        return None

def find_anomalies(df):
    """Simple anomaly detection using Z-score or thresholding (for numeric KPIs)."""
    print("\n🔍 Detected numerical anomalies:")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        col_mean = df[col].mean()
        col_std = df[col].std()
        threshold = 2.5  # Simple z-score threshold
        df['z_score'] = (df[col] - col_mean) / col_std
        anomalies = df[abs(df['z_score']) > threshold]
        if not anomalies.empty:
            print(f"\n🚨 Anomaly in '{col}':")
            print(anomalies[[col, 'z_score']])
    df.drop(columns='z_score', inplace=True, errors='ignore')

def explain_anomalies_with_llm(df, model_name=MODEL_NAME):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    model.eval()

    # Use a snapshot of the data as context
    prompt = "Given this city KPI data, identify any unusual patterns or anomalies:\n\n"
    prompt += df.head(6).to_string(index=False)
    prompt += "\n\nExplain any anomalies and suggest sustainability actions."

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.6,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)
    print("\n🧠 Granite LLM Insight:\n")
    print(result)

def main():
    file_path = "data/city_kpis.csv"
    df = load_kpi_data(file_path)
    if df is not None:
        find_anomalies(df)
        explain_anomalies_with_llm(df)

if __name__ == "__main__":
    main()
