# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    input_int = int(input("What number would you like to start from? "))
    sum = 0
    while sum < 100:
        sum += input_int
        # print(sum)
    print(sum)

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
