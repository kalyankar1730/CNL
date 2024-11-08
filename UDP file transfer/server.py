from socket import *

def receive_file():
    # Define server host and port
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 9999  # Port to listen on
    buf = 1024  # Buffer size

    # Set up the UDP socket
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((host, port))  # Bind the server to listen on all interfaces at the specified port
    print(f"Server listening on {host}:{port}...")

    # Open the file to save incoming data
    with open("received_file.txt", 'w') as f:
        print("Ready to receive file...")

        # Receive the file name first
        data, addr = s.recvfrom(buf)
        file_name = data.decode()
        print(f"Receiving file: {file_name}")

        # Receive the file data in chunks
        try:
            while True:
                data, addr = s.recvfrom(buf)
                if not data:
                    break  # No more data, end the transfer
                f.write(data.decode())  # Decode and write the data to file
                print(f"Received {len(data)} bytes...")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            print("File download complete.")
            s.close()

if __name__ == "__main__":
    receive_file()
