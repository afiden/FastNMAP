import nmap
import os


def port_scan(target):
    nm = nmap.PortScanner()
    print(f"Realizando port scan no alvo: {target}")

    nm.scan(target, arguments='-T4')

    scan_results = f"## Resultados do Port Scan para {target}\n\n"
    for host in nm.all_hosts():
        scan_results += f"### Host: {host} ({nm[host].hostname()})\n"
        scan_results += f"*Estado:* {nm[host].state()}\n\n"

        for proto in nm[host].all_protocols():
            scan_results += f"#### Protocolo: {proto}\n\n"

            lport = nm[host][proto].keys()
            for port in lport:
                scan_results += f"- **Porta:** {port}\n\t- **Estado:** {nm[host][proto][port]['state']}\n\t- **Serviço:** {nm[host][proto][port]['name']}\n\n"

    save_scan_results(scan_results, "Descoberta de Portas", f"{target}.md")
    print(scan_results)


def save_scan_results(content, folder_name, file_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(content)


if __name__ == "__main__":
    target = input("Digite o endereço do alvo para o port scan: ")
    port_scan(target)
