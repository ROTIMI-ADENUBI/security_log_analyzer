import requests

failed_ips = []

with open("logs.txt", "r") as file:
    for line in file:
        if "failed" in line.lower():
            parts = line.split("IP:")
            if len(parts) > 1:
                ip = parts[1].strip()
                failed_ips.append(ip)

# remove duplicates
unique_ips = list(set(failed_ips))

print("Checking suspicious IPs...\n")

for ip in unique_ips:
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()

    print("IP:", ip)
    print("Country:", data.get("country_name"))
    print("City:", data.get("city"))
    print("Org:", data.get("org"))
    print("-" * 30)