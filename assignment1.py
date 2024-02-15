import sys


class StableMatching:
    def __init__(self, input_file_path):
        # Initialize the StableMatching class with necessary attributes
        self.input_file_path = input_file_path
        self.men = {}  # Dictionary to store preferences of men
        self.women = {}  # Dictionary to store preferences of women
        self.num_m = 0  # Number of men
        self.num_w = 0  # Number of women
        self.free_men = set()  # Set to track available men
        self.free_women = {}  # Dictionary to track available women
        self.match_women = {}  # Dictionary to store final stable matches

    def read_input(self):
        # Read input from the specified file and populate men and women preferences
        with open(self.input_file_path, 'r') as input_file:
            counter = 0
            for line in input_file:
                data = line.strip().split(' ')
                if counter == 0:
                    # Extract the number of men and women from the first line of the input file
                    self.num_m, self.num_w = map(int, data)
                elif 1 <= counter <= self.num_m:
                    # Populate men's preferences
                    self.men[data[0]] = {val: i for i, val in enumerate(data[1:], start=1)}
                else:
                    # Populate women's preferences
                    self.women[data[0]] = {val: i for i, val in enumerate(data[1:], start=1)}
                counter += 1

    def initialize_free_sets(self):
        # Initialize sets of free men and women
        self.free_men = set(self.men.keys())
        self.free_women = {i: True for i in self.women.keys()}

    def stable_matching_algorithm(self):
        # Implement the stable matching algorithm
        while self.free_men:
            current_man = self.free_men.pop()
            preferred_women = self.men[current_man]

            for k, v in preferred_women.items():
                if self.free_women[k]:
                    # If the woman is free, match the current man with her
                    self.match_women[k] = current_man
                    self.free_women[k] = False
                    break
                else:
                    priority_men = self.women[k]
                    matched_man = self.match_women[k]

                    if priority_men.get(matched_man, self.num_m + self.num_w) > priority_men.get(current_man,
                                                                                                 self.num_m + self.num_w):
                        # If the current man has higher priority than the matched man, update the match
                        self.match_women[k] = current_man
                        self.free_men.add(matched_man)
                        break

    def print_stable_match(self):
        # Print the final stable matching result
        print("Stable Matching Result:")
        print(self.match_women)

    def write_output(self):
        # Write the stable matching result to an output file
        output_file_path = self.input_file_path.replace('input', 'output')
        with open(output_file_path, 'w') as output_file:
            for woman, man in self.match_women.items():
                output_file.write(f"{man} {woman}\n")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py input_file_name.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]

    # Create an instance of the StableMatching class
    stable_matching_instance = StableMatching(input_file_path)
    stable_matching_instance.read_input()
    stable_matching_instance.initialize_free_sets()
    stable_matching_instance.stable_matching_algorithm()
    stable_matching_instance.print_stable_match()
    stable_matching_instance.write_output()
