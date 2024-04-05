import subprocess

def nmap_scan(target):
    try:
        # Run nmap command
        nmap_command = ['nmap', '-T4', '-A', '-p-', '-v', '--open', '--min-rate', '100', target]
        result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=30)
        output = result.stdout
        
        return output
    except subprocess.TimeoutExpired:
        return "Nmap scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Nmap scan failed with error:\n{e}"
