# Count failed login attempts
count = 0

with open("logs.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print("ALERT:", line.strip())
            count += 1

print("\nTotal failed attempts:", count)