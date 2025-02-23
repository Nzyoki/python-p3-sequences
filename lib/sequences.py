def print_fibonacci(length):
    if length <= 0:
        print([])  # Return an empty list for non-positive lengths
        return

    fibonacci = [0, 1]  # Initialize the first two numbers

    while len(fibonacci) < length:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)

    print(fibonacci[:length])  # Print only up to the required length
