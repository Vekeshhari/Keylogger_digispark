from flask import Flask, send_from_directory
import os

# Folder where your files are stored
HOST_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return 'Demo server running. Access files via /files/<filename>'

@app.route('/files/<path:filename>')
def serve_file(filename):
    # Serve files from the host directory
    return send_from_directory(HOST_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    # Listen on all LAN interfaces, port 8000
    app.run(host='0.0.0.0', port=8000)
