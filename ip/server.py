from flask import Flask, jsonify, render_template
from scapy.all import ARP, Ether, srp
import socket

app = Flask(__name__)

def get_connected_devices():
    """Escaneia a rede local e retorna uma lista de IPs conectados."""
    # Descobre o IP local e calcula a faixa de IP
    ip = socket.gethostbyname(socket.gethostname())
    ip_range = f"{ip.rsplit('.', 1)[0]}.1/24"  # Ajuste para seu IP

    # Cria um pacote ARP para escanear a rede
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]
    
    # Extrai os IPs dos dispositivos conectados
    devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in result]
    return devices

@app.route('/connected_devices')
def connected_devices():
    devices = get_connected_devices()
    return jsonify(devices)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5009')
    app.run(debug=True)
