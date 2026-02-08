import random


def get_numbers_ticket(min_val, max_val, quantity):
    """
    Generates a sorted list of unique random integers for a lottery ticket.

    Parameters:
        min_val (int): Minimum possible number in the set (not less than 1).
        max_val (int): Maximum possible number in the set (not more than 1000).
        quantity (int): Number of numbers to select (value between min_val and max_val).

    Returns:
        list: Sorted list of unique random numbers in the given range.
              Empty list if parameters do not meet the constraints.
    """
    if min_val < 1 or max_val > 1000 or min_val > max_val:
        return []
    if quantity < min_val or quantity > max_val or quantity > (max_val - min_val + 1):
        return []

    population = range(min_val, max_val + 1)

    return sorted(random.sample(population, quantity))


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)