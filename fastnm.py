import subprocess

def nmap_scan(ip):
    initial_scan_cmd = f'nmap {ip} -p- --open -T5 -Pn'
    initial_scan_result = subprocess.run(initial_scan_cmd, shell=True, text=True, capture_output=True)
    open_ports = [line.split('/')[0] for line in initial_scan_result.stdout.splitlines() if 'open' in line]
  
    if open_ports:
        detailed_scan_cmd = f'nmap {ip} -p {",".join(open_ports)} -sV'
        detailed_scan_result = subprocess.run(detailed_scan_cmd, shell=True, text=True, capture_output=True)
        return detailed_scan_result.stdout

    return "Nenhuma porta aberta identificada."

# Acrescente o endereço IP que deseja escanear
ip_alvo = '[Endereço IP que você quer Scanear]'
resultado_scan = nmap_scan(ip_alvo)
print(resultado_scan)
