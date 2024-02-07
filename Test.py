num_m = 0
num_w = 0
men = {}
women = {}

with open("input1.txt", 'r') as input_file:
    counter = 0
    for line in input_file:
        data = line.strip().split(' ')
        if counter == 0:
            num_m, num_w = map(int, data)
        elif 1 <= counter <= num_m:
            men[data[0]] = {val: i for i, val in enumerate(data[1:], start=1)}
        else:
            women[data[0]] = {val: i for i, val in enumerate(data[1:], start=1)}
        counter += 1

print(men['D'],end="\n")
print(women['P'])
print(women['P']['B'])