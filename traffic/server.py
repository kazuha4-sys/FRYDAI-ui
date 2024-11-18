from flask import Flask, jsonify, render_template
from scapy.all import sniff
from threading import Thread
import time

app = Flask(__name__)
traffic_data = []  # Lista para armazenar dados de tráfego

def capture_packet(packet):
    """Captura pacotes e extrai informações relevantes para análise."""
    if packet.haslayer("IP"):  # Verifica se o pacote tem camada IP
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        packet_size = len(packet)

        # Armazena dados do pacote capturado
        traffic_data.append({
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'protocol': protocol,
            'size': packet_size
        })

        # Limita a quantidade de pacotes armazenados (exemplo: 100 últimos pacotes)
        if len(traffic_data) > 100:
            traffic_data.pop(0)

def start_packet_sniffing():
    """Inicia a captura de pacotes em uma nova thread."""
    sniff(prn=capture_packet, store=0)

@app.route('/traffic')
def traffic():
    """Fornece dados de tráfego em formato JSON."""
    return jsonify(traffic_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Inicia a captura de pacotes em uma thread separada
    thread = Thread(target=start_packet_sniffing)
    thread.start()

    # Inicia o servidor Flask
    app.run(host='0.0.0.0', port=5007)
    app.run(debug=True)
