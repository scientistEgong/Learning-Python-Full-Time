# 12.	Sum of first N natural numbers.
def n_sum():
    """Calculate the sum of all integers from start to end (inclusive)."""
    while True:   
        print("Enter a number N, determine the sum of it from it's lowest to N.")
        data_input = input("Enter two numbers seperated by comma or (q to quit): ")

        # Exit
        if data_input.lower() == "q":
            print("Exiing...")
            break

        try: 
            space_cl = data_input.replace(" ", "").split(",")
            x,  y = [u for u in space_cl]
    
            start = int(x)
            end = int(y)
            
            if start > end:
                print("Start number should be less than or equal to end number.")
                continue

            N_sum = 0
            while end >= start:
                end -= 1
                N_sum += end + 1
                
            print(f"The sum of N numbers from {x} to {y} is {N_sum}.")

        except ValueError:
            print("Invalid input!")


n_sum()
