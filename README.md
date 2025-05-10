# PSX-Serial-Utility
 A Python script utilizing the pyserial library to enable uploading of compiled binaries from a PC to the PlayStation 1 (PSX/PS1) console's RAM via a USB-to-Serial cable (using a CH340G based interface chip). Use it with the PSX Serial v014 bootloader from psxdev.net.

# What is this?  
A Python script utilizing the pyserial library to enable uploading of compiled binaries from a PC to the PlayStation 1 (PSX/PS1) console's RAM via a USB-to-Serial cable (CH340G based). The script is an alternative method that is compatible with PSXSerial by PSXdev.net. The program prompts for a file path and COM port before transferring binary data in 1024-byte chunks from the host PC to PSX console at 115200 baud.

The program also implements basic error checking to enhance reliability. This includes waiting for acknowledgments (ACK) after sending the file size and each data chunk with exceptions raised if the expected 0x06 byte is not received. A final acknowledgment confirms successful file transfer. The script also employs a try-except block to catch and handle various error types, including serial communication errors, file I/O errors, and general exceptions. Additionally, a CRC32 calculation function is provided, which can be integrated for further verify data integrity if needed.

WARNING: This program is pre-release; it is buggy and not production ready if at all functional. it is available here for testing purposes. 

## License
This project is licensed under the GNU General Public License v3.0 (GPLv3).  
