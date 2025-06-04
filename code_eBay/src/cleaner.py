import re

def extract_price(price_str):
    # Extract all numbers (including decimals)
    numbers = re.findall(r"\d+\.\d+|\d+", price_str)
    if not numbers:
        return None  # no numbers found
    
    # Convert to floats
    numbers = list(map(float, numbers))
    
    # Example: return average price
    avg_price = sum(numbers) / len(numbers)
    return round(avg_price,2)


def clean_location(location):
    if location.lower().startswith("from "):
        return location[5:].strip()
    

def categorize_delivery(delivery_price):
    delivery_price = delivery_price.lower()
    
    # Check for free delivery (case-insensitive)
    if 'free' in delivery_price:
        return "Free Delivery"
    
    # Check if contains number + $ sign (price)
    if re.search(r'\$\s*\d+', delivery_price):
        return "Paid Delivery"
    
    # Otherwise
    return "Other Delivery"

import re

def extract_feedback_count(text):
    import re
    match = re.search(r'\(?([\d,]+)\)?', text)
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

def update_item(item):
    if 'feedback_count' in item:
        item['feedback_count'] = extract_feedback_count(item['feedback_count'])
    return item


def clean_delivery_price(delivery_price, delivery_category):
    if delivery_category == "Free Delivery":
        return 0
    elif delivery_category == "Paid Delivery":
        import re
        # Extract the first number in the string
        match = re.search(r'[\d,.]+', delivery_price)
        if match:
            num_str = match.group().replace(',', '')
            try:
                return float(num_str)
            except ValueError:
                return None
        else:
            return None
    else:
        # category is 'other' or unknown
        return None