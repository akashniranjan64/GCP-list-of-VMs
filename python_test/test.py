import subprocess

def ping_server(server_ip):
    try:
        result = subprocess.run(['ping', '-c', '4', server_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        success = True
        output = result.stdout
    except subprocess.CalledProcessError as e:
        success = False
        output = e.stderr

    if success:
        print(f"Server {server_ip} is reachable.")
    else:
        print(f"Server {server_ip} is not reachable.")

    print(output)

if __name__ == "__main__":
    server_ip = "google.com"  # Replace with the IP or domain of the server you want to ping
    ping_server(server_ip)