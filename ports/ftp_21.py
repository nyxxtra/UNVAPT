import subprocess

def scan_port_21(target_ip):
    try:
        # Initialize an empty string to store the scan results
        output = ""

        # Check if port 21 is open before proceeding with FTP scans
        if check_port_open(target_ip, 21):
            output += "FTP Port (21) is open.\n\n"

            # Run specific FTP scans
            output += "ftp-anon: Checks if an FTP server allows anonymous login.\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-anon") + "\n"

            output += "ftp-bounce: Checks if an FTP server allows port bouncing (FTP bounce attack).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-bounce") + "\n"

            output += "ftp-brute: Performs brute force password guessing against FTP servers.\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-brute") + "\n"

            output += "ftp-syst: Retrieves system information from FTP servers.\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-syst") + "\n"

            output += "ftp-vsftpd-backdoor: Checks for VSFTPD 2.3.4 backdoor vulnerability (CVE-2011-2523).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vsftpd-backdoor") + "\n"

            output += "ftp-vuln-cve2010-4221: Checks for ProFTPD 1.3.3c mod_copy Command Execution vulnerability (CVE-2010-4221).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2010-4221") + "\n"

            output += "ftp-vuln-cve2015-3306: Checks for ProFTPD 1.3.5 Mod_copy Remote Command Execution vulnerability (CVE-2015-3306).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2015-3306") + "\n"

            output += "ftp-vuln-cve2015-5600: Checks for Pure-FTPd External Authentication Backdoor vulnerability (CVE-2015-5600).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2015-5600") + "\n"

            output += "ftp-vuln-cve2018-13379: Checks for Fortinet FortiOS Unauthenticated FTP vulnerability (CVE-2018-13379).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2018-13379") + "\n"

            output += "ftp-vuln-cve2018-15133: Checks for ProFTPD 1.3.6 Remote Command Execution vulnerability (CVE-2018-15133).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2018-15133") + "\n"

            output += "ftp-vuln-cve2019-12815: Checks for ProFTPD 1.3.5 Remote Command Execution vulnerability (CVE-2019-12815).\n"
            output += perform_nmap_scan(target_ip, "-p21 --script=ftp-vuln-cve2019-12815") + "\n"

        else:
            output += "Port 21 is closed. FTP scans cannot be performed.\n"

        return output
    except subprocess.TimeoutExpired:
        return "Port 21 scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Port 21 scan failed with error:\n{e}"

def check_port_open(target_ip, port):
    # Check if the specified port is open using Nmap
    nmap_command = ['nmap', '-p', str(port), target_ip]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    return f"{port}/tcp open" in result.stdout

def perform_nmap_scan(target_ip, nmap_args):
    # Run nmap command with specified arguments
    nmap_command = ['nmap', '-T4', '-A', '-v', '--open', '--min-rate', '100', target_ip] + nmap_args.split()
    result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=30000)
    return result.stdout
