import subprocess

def ping_server(server_ip):
    try:
        result = subprocess.run(['ping', '-c', '4', server_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def pingtest():
    server_ip = "google.com"
    success, output = ping_server(server_ip)
    if success:
        print(f"Server {server_ip} is reachable.")
        print(output)
    else:
        print(f"Server {server_ip} is not reachable.")
        print(output)