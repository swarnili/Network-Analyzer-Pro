# =============================================================
#  server.py  -  Bandwidth Measurement Tool (Server Side)
#
#  FIX: The server now loops and accepts MULTIPLE connections
#  so it can handle all runs from the client without crashing.
# =============================================================

import socket


def handle_one_connection(conn, address, run_number):
    """
    Receives all data from a single client connection.
    Called once per run.
    """
    print(f"\n[SERVER] Run {run_number}: Client connected from {address}")

    total_bytes_received = 0

    print(f"[SERVER] Run {run_number}: Receiving data...", end="", flush=True)

    while True:
        chunk = conn.recv(1024)   # Read up to 1024 bytes at a time

        if not chunk:             # Empty = client finished sending
            break

        total_bytes_received += len(chunk)

    print(" Done!")

    total_mb = total_bytes_received / (1024 * 1024)
    print(f"[SERVER] Run {run_number}: Total data received: {total_mb:.2f} MB")

    conn.close()   # Close THIS client's connection (not the server socket)


def start_server():
    # ----------------------------------------------------------
    # Step 1: Create the TCP server socket
    # ----------------------------------------------------------
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = "localhost"
    port = 9090
    server_socket.bind((host, port))
    server_socket.listen(5)   # Allow up to 5 queued connections

    # ----------------------------------------------------------
    # How many total connections to expect:
    #   3 data sizes  x  3 runs each  +  1 final summary run = 10
    #   Must match: RUNS_PER_SIZE * len(DATA_SIZES) + 1
    # ----------------------------------------------------------
    total_expected_connections = 10   # 3 sizes x 3 runs + 1 final run

    print(f"[SERVER] Listening on {host}:{port}")
    print(f"[SERVER] Will handle {total_expected_connections} connections total\n")

    # ----------------------------------------------------------
    # Step 2: Loop — accept one connection per run
    # ----------------------------------------------------------
    for run_number in range(1, total_expected_connections + 1):
        print(f"[SERVER] Waiting for connection {run_number}/{total_expected_connections}...")

        conn, address = server_socket.accept()   # Blocks until client connects
        handle_one_connection(conn, address, run_number)

    # ----------------------------------------------------------
    # Step 3: All runs done — close the server socket
    # ----------------------------------------------------------
    server_socket.close()
    print("\n[SERVER] All runs complete. Server shut down.")


if __name__ == "__main__":
    start_server()