from socket import *

def send_file():
    # Define server IP address and file to send
    host = "127.0.0.1"  # Change this to the server's IP address
    port = 9999  # Server port to send data
    buf = 1024  # Buffer size
    file_name = r"C:\Users\Kasturi\Documents\VS code\CN\UDP file transfer\test_file.txt"  ##### File to send (change this to your file)

    # Set up the UDP socket
    s = socket(AF_INET, SOCK_DGRAM)
    addr = (host, port)

    try:
        # Open the file in read mode
        with open(file_name, "r") as f:
            # Read the file data in chunks of size `buf`
            data = f.read(buf)

            # Send the file name first
            s.sendto(file_name.encode(), addr)

            # Send the file data in chunks
            while data:
                s.sendto(data.encode(), addr)  # Encode the data as bytes
                print(f"Sending... {len(data)} bytes")
                data = f.read(buf)

        print("File transfer completed.")

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    send_file()
