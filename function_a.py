def most_common_value(number_list):
    """ returns the most common element of the list
    """
    return max(set(number_list), key=number_list.count)

if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
