import socket
import matplotlib.pyplot as plt
import requests
from matplotlib.backends.backend_pdf import PdfPages

# Define o endereço IP e as portas que serão escaneadas
ip = '192.168.0.1'
start_port = 1
end_port = 100

# Inicializa as variáveis para armazenar as informações das portas escaneadas
open_ports = 0
closed_ports = 0
ports_are_open = 0
# Executa o escaneamento de portas
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        open_ports += 1
        ports_are_open += port
        #ports = "Port {} is open".format(port)
    else:
        closed_ports += 1
    s.close()

# Gera o gráfico em pizza com as informações das portas escaneadas
labels = [f'Open Ports: {ports_are_open}', 'Closed Ports']
sizes = [open_ports, closed_ports]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

# Salva o gráfico em um arquivo PDF
pdf_file = PdfPages('ports_scan.pdf')
pdf_file.savefig(fig1)
pdf_file.close()

# Envia as informações das portas escaneadas para um chat no Telegram
bot_token = 'token_telegram'
chat_id = 'your_chat_id'

message = f'Port scan results:\n\nOpen ports: {open_ports}, \nClosed ports: {closed_ports}, \nPorts are open: {ports_are_open}'

url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json())
