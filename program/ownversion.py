def calculate_total(**items):
    prices = {
        'apple': 0.5,
        'banana': 0.3,
        'orange': 0.4,
    }

    total = 0

    for item, quantity in items.items():
        if item in prices:
            total += prices[item] * quantity
        else:
            print(f"Warning: Unknown item '{item}', ignoring.")

    return total


# Example usage:
total_cost = calculate_total(apple=3, banana=2, orange=1)
print(f"Total cost: ${total_cost:.2f}")
