# Tower of Hanoi Problem using Recursion

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} → {destination}")
    tower_of_hanoi(n-1, helper, source, destination)

# -------- Main Code --------
n = int(input("Enter number of disks: "))
print("\nSteps to solve Tower of Hanoi:\n")
tower_of_hanoi(n, 'A', 'B', 'C')


