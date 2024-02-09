# Solution to Day One

def find_total_calibration(in_file: str) -> int:

    """Find the total calibration value given the input file.
    A more piecemeal implementation"""

    total_calibration: int = 0

    with open(in_file, "r", encoding = "utf-8") as file:

        for line in file:

            just_digits = [char for char in line if char.isdigit()]

            total_calibration += int(just_digits[0] + just_digits[-1])
    
    return total_calibration

# A second, more standard-library-using solution

from operator import itemgetter

def total_calibration_calculator(in_file: str) -> int:

    """Same thing as above, just uses itemgetter"""

    total_calibration: int = 0

    nums = itemgetter(0, -1)                                # setting this up to catch the first and last elements

    with open(in_file, "r", encoding = "utf-8") as file:

        for line in file:

            just_digits = [char for char in line if char.isdigit()]

            total_calibration += int(''.join(nums(just_digits)))
        
    return total_calibration

if __name__ == "__main__":

    print(f"The total calibration value is: {find_total_calibration('input.txt')}")

    print(f"The total calibration value (using an alt approach) is: {total_calibration_calculator('input.txt')}")
