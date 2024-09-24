# model.py
import json
from rules import latest_financial_index, calculate_profit, evaluate_financial_health

def analyze_financial_data(data):
    results = {
        "latest_financial_index": latest_financial_index(data),
        "profit": calculate_profit(data),
        "financial_health": evaluate_financial_health(data),
    }
    return json.dumps(results)

if __name__ == "__main__":
    with open('data.json', 'r') as file:
        data = json.load(file)
    results = analyze_financial_data(data)
    print(results)
