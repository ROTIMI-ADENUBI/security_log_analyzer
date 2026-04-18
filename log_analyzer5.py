from datetime import datetime

failed_ips = []

with open("logs.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            print("ALERT:", line.strip())
            
            # Extract IP
            parts = line.split("IP:")
            if len(parts) > 1:
                ip = parts[1].strip()
                failed_ips.append(ip)

print("\nFailed IPs:", failed_ips)

ip_count = {}

for ip in failed_ips:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

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

print("\n" + "=" * 40)  
print("\n", "END OF REPORT", "\n")
print("Generated:", datetime.now())

with open("report.txt", "w") as file:
    file.write("Security Incident Summary\n\n")

    for ip, count in ip_count.items():
        file.write(f"{ip} -> {count} failed attempts\n")