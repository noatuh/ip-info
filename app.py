import requests

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    ip_address = input("Enter an IP address: ")
    info = get_ip_info(ip_address)
    if info:
        print("IP Information:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve information.")

if __name__ == "__main__":
    main()
