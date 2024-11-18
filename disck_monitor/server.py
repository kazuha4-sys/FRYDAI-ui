from flask import Flask, jsonify, render_template
import psutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/disk_usage')
def disk_usage():
    partitions = psutil.disk_partitions()
    disk_info = []

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        except PermissionError:
            continue  # Ignora partições inacessíveis

    return jsonify(disk_info)

@app.route('/api/files/<path:dir_path>')
def list_files(dir_path):
    try:
        files = []
        for item in os.listdir(dir_path):
            path = os.path.join(dir_path, item)
            if os.path.isfile(path):
                files.append({
                    'name': item,
                    'size': os.path.getsize(path),
                    'path': path
                })
        files.sort(key=lambda x: x['size'], reverse=True)  # Ordena por tamanho
        return jsonify(files)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
    app.run(debug=True)
