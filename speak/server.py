import os
import subprocess
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Função para abrir um site
def abrir_site(url):
    subprocess.Popen(["start", url], shell=True)

# Função para desligar o computador
def desligar_computador():
    subprocess.Popen(["shutdown", "/s", "/f", "/t", "0"], shell=True)

# Função para reiniciar o computador
def reiniciar_computador():
    subprocess.Popen(["shutdown", "/r", "/f", "/t", "0"], shell=True)

# Função para bloquear o computador
def bloquear_computador():
    subprocess.Popen("rundll32.exe user32.dll,LockWorkStation", shell=True)

# Função para controlar o volume
def ajustar_volume(acao):
    if acao == "aumentar":
        subprocess.Popen("nircmd.exe changesysvolume 5000", shell=True)
    elif acao == "diminuir":
        subprocess.Popen("nircmd.exe changesysvolume -5000", shell=True)
    elif acao == "mutar":
        subprocess.Popen("nircmd.exe mutesysvolume 1", shell=True)
    elif acao == "desmutar":
        subprocess.Popen("nircmd.exe mutesysvolume 0", shell=True)

# Função para abrir um aplicativo
def abrir_aplicativo(nome_aplicativo):
    aplicativos = {
        "whatsapp": "https://web.whatsapp.com",
        "instagram": "https://www.instagram.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "gmail": "https://mail.google.com",
        "google": "https://www.google.com",
        "twitter": "https://twitter.com"
    }
    url = aplicativos.get(nome_aplicativo.lower())
    if url:
        abrir_site(url)
    else:
        return jsonify({"erro": "Aplicativo não encontrado"}), 404

# Função para reconhecer comandos de forma mais flexível
def reconhecer_comando(comando):
    comando = comando.lower()
    if "instagram" in comando or "insta" in comando:
        return "instagram"
    elif "whatsapp" in comando:
        return "whatsapp"
    elif "youtube" in comando:
        return "youtube"
    elif "desligar" in comando:
        return "desligar"
    elif "reiniciar" in comando:
        return "reiniciar"
    elif "bloquear" in comando:
        return "bloquear"
    elif "aumentar volume" in comando:
        return "aumentar volume"
    elif "diminuir volume" in comando:
        return "diminuir volume"
    elif "mutar" in comando:
        return "mutar"
    elif "desmutar" in comando:
        return "desmutar"
    else:
        return None

# Rota para execução dos comandos de voz
@app.route('/comando/<comando>', methods=['GET'])
def executar_comando(comando):
    comando_reconhecido = reconhecer_comando(comando)
    
    if comando_reconhecido == "instagram":
        abrir_aplicativo("instagram")
        return jsonify({"mensagem": "Abrindo Instagram"})
    elif comando_reconhecido == "whatsapp":
        abrir_aplicativo("whatsapp")
        return jsonify({"mensagem": "Abrindo WhatsApp"})
    elif comando_reconhecido == "youtube":
        abrir_aplicativo("youtube")
        return jsonify({"mensagem": "Abrindo YouTube"})
    elif comando_reconhecido == "desligar":
        desligar_computador()
        return jsonify({"mensagem": "Desligando computador"})
    elif comando_reconhecido == "reiniciar":
        reiniciar_computador()
        return jsonify({"mensagem": "Reiniciando computador"})
    elif comando_reconhecido == "bloquear":
        bloquear_computador()
        return jsonify({"mensagem": "Bloqueando computador"})
    elif comando_reconhecido == "aumentar volume":
        ajustar_volume("aumentar")
        return jsonify({"mensagem": "Aumentando volume"})
    elif comando_reconhecido == "diminuir volume":
        ajustar_volume("diminuir")
        return jsonify({"mensagem": "Diminuindo volume"})
    elif comando_reconhecido == "mutar":
        ajustar_volume("mutar")
        return jsonify({"mensagem": "Mutando volume"})
    elif comando_reconhecido == "desmutar":
        ajustar_volume("desmutar")
        return jsonify({"mensagem": "Desmutando volume"})
    else:
        return jsonify({"erro": "Comando não reconhecido"}), 400

# Rota para verificar status
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
