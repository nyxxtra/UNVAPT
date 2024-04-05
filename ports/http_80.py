import subprocess

def scan_port_80(target_ip):
    try:
        # Run specific scan for port 80
        nmap_command = ['nmap', '-p', '80', '-A', '-v', '--open', '--min-rate', '100', target_ip]
        result = subprocess.run(nmap_command, capture_output=True, text=True, timeout=30)
        output = result.stdout
        
        return output
    except subprocess.TimeoutExpired:
        return "Port 80 scan timed out."
    except subprocess.CalledProcessError as e:
        return f"Port 80 scan failed with error:\n{e}"
