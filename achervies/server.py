import os
from flask import Flask, jsonify, render_template
from pathlib import Path

app = Flask(__name__)

def list_common_user_folders():
    """Lista algumas pastas principais do usuário que podem estar fixadas."""
    home = Path.home()
    common_folders = {
        "Documentos": str(home / "Documents"),
        "Downloads": str(home / "Downloads"),
        "Área de Trabalho": str(home / "Desktop"),
        "Músicas": str(home / "Music"),
        "Imagens": str(home / "Pictures"),
        "Vídeos": str(home / "Videos"),
    }
    
    # Filtrar apenas as pastas que realmente existem no sistema
    return {name: path for name, path in common_folders.items() if os.path.exists(path)}

@app.route('/folders')
def folders():
    folders = list_common_user_folders()
    return jsonify(folders)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
