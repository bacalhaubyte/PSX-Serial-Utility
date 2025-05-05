import serial
import time
import os
import struct
import binascii

def transfer_binary(file_path, serial_port):
    """
    Transfer a binary file to the PSX via serial connection.
    
    Args:
    file_path (str): Path to the binary file to be transferred.
    serial_port (str): COM port for the USB-Serial adapter.
    """
    try:
        # Open the serial connection with a baud rate of 115200 and a timeout of 5 seconds
        ser = serial.Serial(serial_port, 115200, timeout=5)
        
        # Read the entire binary file into memory
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        
        # Calculate the size of the file
        file_size = len(binary_data)
        print(f"File size: {file_size} bytes")
        
        # Send the file size as a 4-byte big-endian integer
        ser.write(file_size.to_bytes(4, byteorder='big'))
        time.sleep(0.1)  # Short delay to ensure data is sent
        
        # Wait for an acknowledgment byte (ACK, 0x06) from the PSX
        ack = ser.read(1)
        if ack != b'\x06':
            raise Exception("File size not acknowledged by console")
        
        print("File size acknowledged. Starting data transfer...")
        
        # Send the binary data in chunks
        chunk_size = 1024  # Size of each chunk in bytes
        total_sent = 0
        for i in range(0, file_size, chunk_size):
            # Extract a chunk of data
            chunk = binary_data[i:i+chunk_size]
            
            # Send the chunk
            ser.write(chunk)
            
            # Wait for acknowledgment after each chunk
            ack = ser.read(1)
            if ack != b'\x06':
                raise Exception(f"Chunk at offset {i} not acknowledged by console")
            
            # Update and display progress
            total_sent += len(chunk)
            print(f"Progress: {total_sent}/{file_size} bytes sent", end='\r')
            
            time.sleep(0.01)  # Small delay to prevent buffer overflow
        
        print("\nAll data sent. Waiting for final acknowledgment...")
        
        # Wait for final acknowledgment from PSX
        final_ack = ser.read(1)
        if final_ack != b'\x06':
            raise Exception("Final acknowledgment not received from the console")
        
        print("Transfer completed successfully")
        
    except serial.SerialException as e:
        print(f"Serial communication error: {e}")
    except IOError as e:
        print(f"File I/O error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the serial connection is closed, even if an error occurred
        if 'ser' in locals() and ser.is_open:
            ser.close()

def calculate_crc32(data):
    """
    Calculate the CRC32 checksum of the given data.
    
    Args:
    data (bytes): The data to calculate the checksum for.
    
    Returns:
    bytes: The CRC32 checksum as a 4-byte string.
    """
    return struct.pack('>I', binascii.crc32(data) & 0xFFFFFFFF)

def get_valid_file_path():
    """
    Prompt the user for a valid file path.
    
    Returns:
    str: A valid path to an existing file.
    """
    while True:
        file_path = input("Enter full path to the compiled binary file: ").strip()
        if os.path.exists(file_path):
            return file_path
        else:
            print("Error: File not found. Enter a valid file path.")

def get_valid_com_port():
    """
    Prompt the user for a valid COM port.
    
    Returns:
    str: A string representing a COM port (e.g., 'COM3').
    """
    while True:
        com_port = input("Enter COM port for the USB-Serial adapter (e.g., COM3): ").strip()
        if com_port.lower().startswith('com'):
            return com_port
        else:
            print("Error: Invalid COM port. Enter a valid COM port (e.g., COM3).")

if __name__ == "__main__":
    # Main execution block
    print("PSX Binary Transfer Tool")
    print("==================================")
    
    # Get file path and COM port from user
    binary_file = get_valid_file_path()
    serial_port = get_valid_com_port()
    
    print(f"\nTransferring {binary_file} to PSX console via {serial_port}...")
    # Start the transfer process
    transfer_binary(binary_file, serial_port)
