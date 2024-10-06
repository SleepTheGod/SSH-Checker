import paramiko
import concurrent.futures

# ASCII Art Banner
banner = """
    ███████╗███████╗██╗  ██╗      
    ██╔════╝██╔════╝██║  ██║      
    ███████╗███████╗███████║      
    ╚════██║╚════██║██╔══██║      
    ███████║███████║██║  ██║      
    ╚══════╝╚══════╝╚═╝  ╚═╝      

███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗██║     ███████║██╔██╗ ██║
╚════██║██║     ██╔══██║██║╚██╗██║
███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ 
Made By Taylor Christian Newsome !              
"""

def load_credentials(filename):
    """Load credentials from a given file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_ssh(cred):
    """Attempt to connect via SSH and return success message if successful."""
    ip_port, user_pass = cred.split(' ')
    ip, port = ip_port.split(':')
    username, password = user_pass.split(':')

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip, username=username, password=password, timeout=5)
        success_message = f"Success: {ip}:{port} with {username}/{password}"
        print(success_message)

        # Save to working.txt immediately upon success
        with open('working.txt', 'a') as file:
            file.write(f"{success_message}\n")

        return True  # Indicate success
    except (paramiko.AuthenticationException, paramiko.SSHException):
        return False  # Indicate failure
    except Exception as e:
        print(f"Error connecting to {ip}: {e}")
        return False  # Indicate failure
    finally:
        client.close()

def main():
    """Main function to load credentials and perform SSH checks."""
    print(banner)  # Print the ASCII art banner

    # Create or clear the working.txt file
    open('working.txt', 'w').close()

    credentials = load_credentials('ssh.txt')

    # Use ThreadPoolExecutor for concurrent SSH attempts
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(check_ssh, cred): cred for cred in credentials}

        # Wait for futures to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()  # We don't need to do anything with the result here

if __name__ == '__main__':
    main()
