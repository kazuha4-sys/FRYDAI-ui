from flask import Flask, request, jsonify, render_template
import subprocess
import platform

app = Flask(__name__)

# Lista de comandos suportados
COMMANDS = {
    # Sistema e rede
    "ipconfig": "Exibe a configuração de rede do sistema (Windows).",
    "ifconfig": "Exibe a configuração de rede do sistema (Linux/Mac).",
    "ping <host>": "Testa a conectividade com outro host.",
    "hostname": "Exibe o nome do computador.",
    "systeminfo": "Mostra informações do sistema.",
    "tracert <host>": "Rastreia o caminho até um host na rede.",
    "netstat": "Exibe conexões de rede ativas.",
    "arp -a": "Exibe a tabela ARP.",
    "nslookup <domain>": "Realiza consultas DNS.",
    "whoami": "Exibe o usuário atual.",
    "shutdown -s -t <segundos>": "Agenda o desligamento do sistema.",
    "tasklist": "Lista os processos em execução.",
    "taskkill /PID <id> /F": "Finaliza um processo pelo PID.",

    # Arquivos e diretórios
    "dir": "Lista os arquivos e diretórios no diretório atual.",
    "cd <path>": "Navega até o diretório especificado.",
    "md <nome>": "Cria um novo diretório.",
    "rd <nome>": "Remove um diretório.",
    "del <arquivo>": "Apaga um arquivo.",
    "copy <src> <dest>": "Copia arquivos.",
    "move <src> <dest>": "Move arquivos.",
    "rename <arquivo> <novo_nome>": "Renomeia um arquivo.",
    "attrib": "Exibe ou altera atributos de arquivo.",
    "tree": "Exibe a estrutura de pastas do diretório.",
    "type <arquivo>": "Exibe o conteúdo de um arquivo.",
    "find <texto> <arquivo>": "Procura por texto dentro de um arquivo.",

    # Sistema e processos
    "ver": "Exibe a versão do sistema operacional.",
    "cls": "Limpa a tela do terminal.",
    "echo <texto>": "Exibe o texto no terminal.",
    "set": "Exibe variáveis de ambiente.",
    "path": "Exibe ou define variáveis de caminho.",
    "assoc": "Exibe associações de extensões de arquivo.",
    "fc <arquivo1> <arquivo2>": "Compara dois arquivos.",
    "schtasks": "Agenda tarefas para execução.",
    "sc query": "Exibe informações de serviços.",

    # Informações do hardware
    "wmic cpu get loadpercentage": "Exibe a carga atual da CPU.",
    "wmic memorychip get capacity": "Exibe a capacidade de memória RAM.",
    "diskpart": "Abre a ferramenta de gerenciamento de discos.",
    "chkdsk": "Verifica e corrige erros no disco.",
    "defrag": "Desfragmenta uma unidade de disco.",
    "driverquery": "Lista os drivers instalados.",
    "powercfg": "Configurações de energia.",

    # Diversos
    "date": "Exibe ou ajusta a data do sistema.",
    "time": "Exibe ou ajusta a hora do sistema.",
    "color <code>": "Altera a cor do terminal.",
    "title <texto>": "Altera o título do terminal.",
    "exit": "Encerra o terminal."
}

# Rota para executar os comandos
@app.route('/execute-command', methods=['POST'])
def execute_command():
    command = request.json.get('command')

    if not command:
        return jsonify({'error': 'Comando vazio!'}), 400

    base_command = command.split()[0]  # Obtém o comando principal
    if base_command not in [cmd.split()[0] for cmd in COMMANDS.keys()]:
        return jsonify({'error': f'Comando "{command}" não permitido! Use "--help" para ajuda.'}), 403

    try:
        # Executa o comando no sistema
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota para listar comandos
@app.route('/help')
def list_commands():
    commands_list = "\n".join([f"{cmd}: {desc}" for cmd, desc in COMMANDS.items()])
    return jsonify({'help': commands_list})

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
