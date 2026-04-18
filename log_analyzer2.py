# Print failed logins
with open("logs.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print("ALERT:", line.strip())