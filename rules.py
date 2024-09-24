# rules.py

def latest_financial_index(data):
    # Example implementation: return the latest financial index
    return data["financial_indices"][-1]  # Assuming financial_indices is a list in the data

def calculate_profit(data):
    # Example implementation: calculate profit
    revenue = data.get("revenue", 0)
    expenses = data.get("expenses", 0)
    return revenue - expenses

def evaluate_financial_health(data):
    # Example implementation: simple health check
    profit = calculate_profit(data)
    if profit > 0:
        return "Healthy"
    return "Unhealthy"
