
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