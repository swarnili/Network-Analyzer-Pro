from flask import Flask, render_template, jsonify, request
import socket
import time

app = Flask(__name__)

def run_single_test(target_ip, size_mb=10):
    PORT = 9090
    data = bytes(size_mb * 1024 * 1024)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5) # Stop waiting after 5 seconds if server is down
    
    try:
        client_socket.connect((target_ip, PORT))
        time.sleep(0.1) 
        
        start_time = time.perf_counter()
        client_socket.sendall(data)
        client_socket.shutdown(socket.SHUT_WR)
        end_time = time.perf_counter()
        
        time_taken = end_time - start_time
        bandwidth = size_mb / time_taken
        client_socket.close()
        
        return {"speed": round(bandwidth, 2), "time": round(time_taken, 4), "data_sent": size_mb}
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-test', methods=['POST'])
def api_run_test():
    # Get IP and number of runs from the website
    config = request.json
    target_ip = config.get('ip', 'localhost')
    num_runs = int(config.get('runs', 3))
    
    results = []
    for i in range(num_runs):
        res = run_single_test(target_ip)
        if "error" in res:
            return jsonify(res), 500
        results.append(res)
    
    # Calculate Average
    avg_speed = sum(r['speed'] for r in results) / len(results)
    
    return jsonify({
        "all_runs": results,
        "average": round(avg_speed, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)