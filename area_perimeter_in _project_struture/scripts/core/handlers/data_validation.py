def input_function(input_from_prompt):
    while True:
        try:
            float_input = float(input(input_from_prompt))
            if float_input == 0:
                print("Dimensions cannot be zero")
                continue
            return float_input
        except ValueError:
            print("Invalid input.Enter valid number")
            continue
