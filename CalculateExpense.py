data = {
    "1": {"description": "Lunch", "amount": 250, "category": "Food"},
    "2": {"description": "Dinner", "amount": 300, "category": "Food"},
    "3": {"description": "Petrol", "amount": 500, "category": "Travel"},
    "4": {"description": "Bus", "amount": 100, "category": "Travel"},
    "5": {"description": "Book", "amount": 400, "category": "Education"}
}


for exp_id, details in data.items():
    if details["category"] == "Food":
        food_amount = details.get("amount", 0)
        
