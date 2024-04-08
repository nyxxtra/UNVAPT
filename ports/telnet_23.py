import subprocess

def scan_port_23(target_ip):
    try:
        # Initialize an empty string to store the scan results
        output = ""

        # Check if port 23 is open before proceeding with Telnet scans
        if check_port_open(target_ip, 23):
            output += "Telnet Port (23) is open.\n\n"

            # Run specific Telnet scans
            output += "telnet-brute: Performs brute-force password guessing against Telnet services.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-brute") + "\n"

            output += "telnet-encryption: Detects if Telnet sessions are encrypted.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-encryption") + "\n"

            output += "telnet-ntlm-info: Retrieves NTLM authentication information over Telnet.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-ntlm-info") + "\n"

            output += "telnet-protocols: Detects supported Telnet protocols.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-protocols") + "\n"

            output += "telnet-vuln-cve2011-4862: Checks for a specific Telnet vulnerability (CVE-2011-4862).\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-vuln-cve2011-4862") + "\n"

            output += "telnet-ntlm-info: Retrieves NTLM authentication information over Telnet.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-ntlm-info") + "\n"

            output += "telnet-encryption: Detects if Telnet sessions are encrypted.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-encryption") + "\n"

            output += "telnet-fingerprint: Fingerprint Telnet services to determine the underlying OS.\n"
            output += perform_nmap_scan(target_ip, "-p23 --script=telnet-fingerprint") + "\n"

        else:
            output += "Port 23 is closed. Telnet scans cannot be performed.\n"

        return output
    except subprocess.TimeoutExpired:
        return "Port 23 scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Port 23 scan failed with error:\n{e}"

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
