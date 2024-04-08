import subprocess

def scan_port_80(target_ip):
    try:
        # Initialize an empty string to store the scan results
        output = ""

        # Run specific scans for port 80
        output += "http-enum: Enumerate directories, scripts, and more on HTTP servers.\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-enum") + "\n"

        output += "http-headers: Retrieves HTTP headers from web servers.\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-headers") + "\n"

        output += "http-vuln-cve2010-2861: Checks for a specific HTTP vulnerability (CVE-2010-2861).\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-vuln-cve2010-2861") + "\n"

        output += "http-vuln-cve2017-5638: Checks for Apache Struts2 Remote Code Execution vulnerability (CVE-2017-5638).\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-vuln-cve2017-5638") + "\n"

        output += "http-vuln-cve2017-1001000: Checks for Jenkins Unauthenticated Remote Code Execution vulnerability (CVE-2017-1001000).\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-vuln-cve2017-1001000") + "\n"

        output += "http-vuln-cve2019-2725: Checks for Oracle WebLogic Server Deserialization RCE vulnerability (CVE-2019-2725).\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-vuln-cve2019-2725") + "\n"

        output += "http-vuln-cve2020-14882: Checks for Oracle WebLogic Server Remote Code Execution vulnerability (CVE-2020-14882).\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-vuln-cve2020-14882") + "\n"

        output += "http-shellshock: Checks for Shellshock (CVE-2014-6271) vulnerability in HTTP servers.\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-shellshock") + "\n"

        output += "http-php-version: Retrieves PHP version information from web servers.\n"
        output += perform_nmap_scan(target_ip, "-p80 --script=http-php-version") + "\n"

        return output
    except subprocess.TimeoutExpired:
        return "Port 80 scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Port 80 scan failed with error:\n{e}"

def perform_nmap_scan(target_ip, nmap_args):
    # Run nmap command with specified arguments
    nmap_command = ['nmap', '-T4', '-A', '-v', '--open', '--min-rate', '100', target_ip] + nmap_args.split()
    result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=30)
    return result.stdout
