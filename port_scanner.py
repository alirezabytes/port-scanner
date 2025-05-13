import socket

def scan_ports(ip, ports):
    print(f"Scanning {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open!")
        else:
            print(f"Port {port} is closed.")
        sock.close()

if __name__ == "__main__":
    print("Welcome to Port Scanner!")
    print("1. Scan localhost (127.0.0.1) with default ports")
    print("2. Scan custom IP and ports")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        target_ip = "127.0.0.1"
        ports_to_scan = [80, 443, 22]
        scan_ports(target_ip, ports_to_scan)
    elif choice == "2":
        target_ip = input("Enter the IP address to scan (e.g., 127.0.0.1): ")
        ports_input = input("Enter ports to scan (e.g., 80,443,22): ")
        try:
            ports_to_scan = [int(port) for port in ports_input.split(",")]
            if not ports_to_scan:
                print("No ports provided!")
            else:
                scan_ports(target_ip, ports_to_scan)
        except ValueError:
            print("Invalid port numbers! Please enter numbers separated by commas.")
    else:
        print("Invalid choice! Please select 1 or 2.")
