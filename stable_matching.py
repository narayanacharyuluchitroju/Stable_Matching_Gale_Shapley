# STABLE_MATCHING
# COURSE - CS7200
# TEAM:
# CHITROJU KODANDA SAIAYYAPPA RAGHAVENDRA SESHA NARAYANACHARYULU
# VARUN GRANDHI
# SUDHEER DANIEL MEGHAVARAM


num_m = 0
num_w = 0
men = {}
women = {}

with open("input.txt", 'r') as input_file:
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

free_men = [i for i in men.keys()]  # ['m1', 'm2', 'm3']
free_women = [i for i in women.keys()]  # ['w1', 'w2']
match_women = {}

print(free_men)
print("\n")
print(free_women)
print("Started\n")

while free_men:
    current_man = free_men.pop(0) #D
    # print("Line 24: {}\n".format(current_man))
    preferred_women = men[current_man] # {'P': 1, 'M': 2, 'O': 3, 'N': 4, 'L': 5}
    print(preferred_women)
    print('Loop - start')
    for k,v in preferred_women.items():
        print(k,v)
        if k in free_women:
            print("Line 29: {}".format(k))
            match_women[k] = current_man
            print(k,current_man)
            free_women.remove(k)
            break
        else:
            print('Else block started')
            priority_men = women[k] # {'B': 1, 'E': 2, 'A': 3, 'C': 4, 'D': 5}
            print(priority_men)
            matched_man = match_women[k] # 'B'
            print(matched_man,current_man)
            if priority_men[matched_man] > priority_men[current_man]:
                print(women[k][matched_man],priority_men[current_man])
                match_women[k] = current_man
                print(k,current_man)
                free_men.append(matched_man)
                print(free_men)
                break

print(match_women)