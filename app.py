from flask import Flask, request, jsonify, send_from_directory
import threading
import time
import os

try:
    import winsound
except Exception:
    winsound = None

app = Flask(__name__, static_folder='.')

state = {"running": False, "remaining": 0}

def server_countdown(seconds: int):
    state['running'] = True
    state['remaining'] = seconds
    try:
        while state['remaining'] > 0:
            time.sleep(1)
            state['remaining'] -= 1
        # play a bark-like sound on the host (Windows winsound if available)
        if winsound:
            def host_bark():
                try:
                    winsound.Beep(900, 140)
                    winsound.Beep(1200, 100)
                    winsound.Beep(700, 160)
                except Exception:
                    pass
            # two quick barks
            host_bark()
            time.sleep(0.18)
            host_bark()
    finally:
        state['running'] = False
        state['remaining'] = 0


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/start', methods=['POST'])
def start():
    data = request.get_json(silent=True) or {}
    # allow seconds via JSON body or query string
    secs = data.get('seconds') if 'seconds' in data else request.args.get('seconds', 0)
    try:
        secs = int(secs)
    except Exception:
        return jsonify({'error': 'invalid seconds'}), 400
    if secs < 0:
        return jsonify({'error': 'invalid seconds'}), 400
    if state['running']:
        return jsonify({'status': 'already_running'}), 409
    t = threading.Thread(target=server_countdown, args=(secs,), daemon=True)
    t.start()
    return jsonify({'status': 'started', 'seconds': secs})


@app.route('/status')
def status():
    return jsonify(state)


if __name__ == '__main__':
    # Run on localhost:5000
    app.run(host='127.0.0.1', port=5000)
