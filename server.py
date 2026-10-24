from flask import Flask, send_from_directory, jsonify
import os
import socket

# Folder where your files are stored
HOST_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    # Show available files
    files = [f for f in os.listdir(HOST_DIR) if os.path.isfile(os.path.join(HOST_DIR, f))]
    return f'Demo server running. Available files: {", ".join(files)}'

@app.route('/<path:filename>')
def serve_file(filename):
    # Serve files from the host directory
    return send_from_directory(HOST_DIR, filename, as_attachment=True)

@app.route('/ip')
def get_ip():
    # Useful for debugging to verify server IP
    return jsonify({'ip': socket.gethostbyname(socket.gethostname())})

if __name__ == '__main__':
    # Print server IP for easy reference
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Server running at: http://{local_ip}:5000")
    print(f"Files available from: http://{local_ip}:5000/files/<filename>")
    
    # Listen on all LAN interfaces, port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)