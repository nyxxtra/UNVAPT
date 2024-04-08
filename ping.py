import subprocess

def ping_device(ip_address):
    try:
        # Run ping command
        result = subprocess.run(["ping", "-c", "10", ip_address], capture_output=True, text=True, timeout=10)
        output = result.stdout
        
        return output
    except subprocess.TimeoutExpired:
        return "Ping timed out. Device might be unreachable."
    except subprocess.CalledProcessError:
        return "Ping failed. Device is unreachable."


