import requests
from datetime import datetime 

# Initialize counters for successful and failed login attempts
s_count = 0
f_count = 0
failed_ips = []
ip_count = {}

# Open the log file for all login attempts
with open("logs.txt", "r") as file:
    for row in file:
        
        # Check for successful login attempts
        if "success" in row.lower():
            ip = row.split("IP:")[1].strip() # Extract IP address
            s_count += 1 
            print("ALERT: No issue! IP:", ip)

        # Check for failed login attempts
        elif "failed" in row.lower():
            ip = row.split("IP:")[1].strip() # Extract IP address
            f_count += 1
            print("ALERT: Failed login attempt! IP:", ip)
            failed_ips.append(ip) # Add each failed IP to the list
    
    # Store the list of failed IPs and count occurrences
    for ip in failed_ips:
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

    # Print the summary of login attempts        
    print("\nTotal successful attempts:", s_count)
    print("Total failed attempts:", f_count)
    print("\nTotal login attempts:", s_count + f_count) 
    print("\nFailed IPs:", failed_ips)

    print("\nAttack frequency:")
    for ip, count in ip_count.items():
        print(ip, "->", count, "times")

print("\nAI SECURITY SUMMARY")
print("-" * 30)

for ip, count in ip_count.items():

    if count >= 3:
        print(f"{ip}: Possible brute-force attack detected.")
    
    elif count == 2:
        print(f"{ip}: Repeated suspicious login failures.")
    
    else:
        print(f"{ip}: Single failed login attempt.")

with open("reportP.txt", "w") as file:
    file.write("Security Incident Summary\n\n")

    for ip, count in ip_count.items():
        file.write(f"{ip} -> {count} failed attempts\n")

# remove duplicates
unique_ips = list(set(failed_ips))

print("\nChecking suspicious IPs...\n")

for ip in unique_ips:
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()

    print("IP:", ip)
    print("Country:", data.get("country_name"))
    print("City:", data.get("city"))
    print("Org:", data.get("org"))
    print("-" * 30)

print("\n" + "=" * 40)  
print("\n", "END OF REPORT", "\n")
print("Generated:", datetime.now())
