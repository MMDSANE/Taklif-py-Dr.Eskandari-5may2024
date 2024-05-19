#bazi pamayesh dar list ta be enteha beresim

lst1 = []

for _ in range(6):
    while True:
        inp = input("Enter a Positive Integer: ")
        if inp.isdigit():
            inp = int(inp)
            lst1.append(inp)
            break
        else:
            print("Invalid input")

def traverse_list(index):
    steps = lst1[index]

    if steps == 0:
        return "Rahi Nist"

    for step in range(1, steps + 1):
        next_index = index + step
        if next_index >= len(lst1):
            return "Shoma be payan residid dar ((( PEYMAYESH ))) list"
        if lst1[next_index] != 0:
            return traverse_list(next_index)
    
    return "Rahi Nist"

result = traverse_list(0)
print(result)
