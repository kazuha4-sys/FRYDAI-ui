from flask import Flask, jsonify, render_template
import psutil
import platform

app = Flask(__name__)

# Rota para obter informações do sistema
@app.route('/system-stats')
def system_stats():
    # Coleta as informações do sistema
    cpu_usage = psutil.cpu_percent(interval=1)  # % de uso da CPU
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 2)  # MB
    used_memory = memory.used / (1024 ** 2)   # MB

    system_info = {
        'cpu_cores': psutil.cpu_count(logical=True),  # Número de núcleos lógicos
        'cpu_load': cpu_usage,
        'memory_total': round(total_memory, 2),
        'memory_used': round(used_memory, 2),
        'os': f"{platform.system()} {platform.release()}"  # Sistema operacional
    }
    return jsonify(system_info)

# Rota principal que renderiza o HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Execute o servidor Flask
    app.run(host="0.0.0.0", port=5003)
    app.run(debug=False) 