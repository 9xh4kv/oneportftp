# OnePortFTP 
OnePortFTP is a Python-based FTP server designed for easy passive port management. 
It simplifies the process by utilizing a single passive port, making it a convenient choice for UFW users.
## Usage
Default Listening port: 21
Default Passive port: 1620
- Start the FTP server with credentials
```
python3 oneportftp.py -u USER -p PASSWORD 
```
- Start the FTP server with Anonymous login and write/read permissions (no account required)
```
python3 oneportftp.py
```
- Customizing the listening port and passive port:
```
python3 oneportftp.py -l 4444 -P 8888
```