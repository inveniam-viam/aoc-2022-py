# Solution to day 2

number_map: dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def better_calibration_calculator(in_file: str) -> int:

    """calculating calibration according to new logic"""

    with open(in_file, "r", encoding = "utf-8") as file:

        total: int = 0

        for line in file:

            out_list = [(val, idx) for idx, val in enumerate(line) if val.isdigit()]

            for key, value in number_map.items():

                out_list.extend([(str(value), idx) for idx in range(len(line)) if line.startswith(key, idx)])
            
            first = sorted(out_list, key = lambda x: x[1])[0][0]
            last = sorted(out_list, key = lambda x: x[1], reverse = True)[0][0]

            total += int(first + last)

    return total


if __name__ == "__main__":

    print(better_calibration_calculator("sample-input.txt"))
