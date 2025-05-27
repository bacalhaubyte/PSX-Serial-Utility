# PSX-Serial-Utility
A Python file transfer utility for PlayStation 1 (PSX/PS1) development. The script utilizes the pyserial library to enable uploading of compiled binaries from a PC to the PlayStation console's RAM via a USB-to-Serial cable (CH340G based cable). The utility is compatible with PSXSerial by PSXdev.net. 

PSX Serial transfers binary data in 1024-byte chunks from the host PC to PSX console at 115200 baud and implements basic error checking to enhance reliability. This includes waiting for acknowledgments (ACK) after sending the file size and each data chunk with exceptions raised if the expected ~0x06~ byte is not received. A final acknowledgment confirms successful file transfer. The script also employs a try-except block to catch and handle various error types, including serial communication errors, file I/O errors, and general exceptions. Additionally, a CRC32 calculation function is provided, which can be integrated for further verify data integrity if needed.

WARNING: This program is a work in progress; it is buggy and not production-ready. 

## License
This project is licensed under the GNU General Public License v3. Attribution should go to [RetroGameplayer.com](http://retrogameplayer.com)
