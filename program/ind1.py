def sum_between_negatives(*args):
    if not args or all(arg >= 0 for arg in args):
        return 0  # No negatives or empty list

    first_negative_index = next((i for i, arg in enumerate(args) if arg < 0), None)
    last_negative_index = next((i for i, arg in enumerate(args[::-1]) if arg < 0), None)

    if first_negative_index is None or last_negative_index is None:
        return 0  # No negatives found

    last_negative_index = len(args) - 1 - last_negative_index

    if first_negative_index >= last_negative_index:
        return 0  # No values between negatives

    values_between_negatives = args[first_negative_index + 1:last_negative_index]
    return sum(values_between_negatives)


# Example usage:
result = sum_between_negatives(1, 2, -3, 4, 5, -6, 7, 8, -9)
print(result)
