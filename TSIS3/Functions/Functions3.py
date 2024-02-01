
def solve(numheads, numlegs):
    if numlegs % 2 == 1:
        print("Unreal")
        return 0
    initial = numheads
    while numlegs / 2 != numheads:
        numlegs -= 4
        numheads -= 1
    print(f"Number of rabbits: {initial - numheads}, chickens: {numheads}")

# solve(26, 96)