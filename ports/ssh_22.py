import subprocess

def scan_port_22(target_ip):
    try:
        # Initialize an empty string to store the scan results
        output = ""

        # Check if port 22 is open before proceeding with SSH scans
        if check_port_open(target_ip, 22):
            output += "SSH Port (22) is open.\n\n"

            # Run specific SSH scans
            output += "ssh-auth-methods: Determines authentication methods supported by an SSH server.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-auth-methods") + "\n"

            output += "ssh-hostkey: Retrieves SSH host key information.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-hostkey") + "\n"

            output += "sshv1: Checks if SSH protocol version 1 is supported.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=sshv1") + "\n"

            output += "ssh2-enum-algos: Enumerates supported algorithms for SSH version 2.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh2-enum-algos") + "\n"

            output += "ssh2-enum-channels: Enumerates active channels on an SSH server.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh2-enum-channels") + "\n"

            output += "sshv2: Checks if SSH protocol version 2 is supported.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=sshv2") + "\n"

            output += "ssh-brute: Performs brute force password guessing against SSH servers.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-brute") + "\n"

            output += "ssh-exec: Executes a command on an SSH server and retrieves the output.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-exec") + "\n"

            output += "ssh-known-hosts: Retrieves SSH known host keys from a file.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-known-hosts") + "\n"

            output += "ssh-run: Runs a command via SSH and retrieves the output.\n"
            output += perform_nmap_scan(target_ip, "-p22 --script=ssh-run") + "\n"

        else:
            output += "Port 22 is closed. SSH scans cannot be performed.\n"

        return output
    except subprocess.TimeoutExpired:
        return "Port 22 scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Port 22 scan failed with error:\n{e}"

def check_port_open(target_ip, port):
    # Check if the specified port is open using Nmap
    nmap_command = ['nmap', '-p', str(port), target_ip]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    return f"{port}/tcp open" in result.stdout

def perform_nmap_scan(target_ip, nmap_args):
    # Run nmap command with specified arguments
    nmap_command = ['nmap', '-T4', '-A', '-v', '--open', '--min-rate', '100', target_ip] + nmap_args.split()
    result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=3000)
    return result.stdout
