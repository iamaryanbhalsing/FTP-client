#!/usr/bin/env python3
"""
FTP Program - Simple FTP Client for transferring files to/from a remote server.

Features:
- Connect to FTP server
- List directories
- Download files
- Upload files
- Create directories
- Delete files/directories
- Navigate directories

Usage:
    python ftp_client.py
"""

import ftplib
import os
import sys
from getpass import getpass
from datetime import datetime


class FTPClient:
    def __init__(self):
        self.ftp = None
        self.connected = False
        self.current_dir = '/'

    def connect(self, host, username=None, password=None, port=21):
        """Connect to the FTP server"""
        try:
            print(f"Connecting to {host}:{port}...")
            self.ftp = ftplib.FTP()
            self.ftp.connect(host, port, timeout=30)
            if username is None:
                username = input("Username: ")
            if password is None:
                password = getpass("Password: ")
            
            self.ftp.login(username, password)
            self.connected = True
            print("Connected successfully!")
            self.show_welcome()
            self.current_dir = self.ftp.pwd()
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def show_welcome(self):
        """Show server welcome message"""
        print(self.ftp.getwelcome())

    def list_files(self, directory=None):
        """List files in current or specified directory"""
        if not self.connected:
            print("Not connected to server.")
            return
        
        try:
            if directory:
                self.ftp.cwd(directory)
            
            print(f"\nDirectory listing for: {self.ftp.pwd()}")
            print("-" * 60)
            print(f"{'Type':<6} {'Size':>10} {'Last Modified':<20} Name")
            print("-" * 60)
            
            files = []
            self.ftp.dir(lambda x: files.append(x))
            
            for line in files:
                print(line)
                
        except Exception as e:
            print(f"Error listing files: {e}")

    def download_file(self, remote_file, local_path=None):
        """Download a file from server"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            if local_path is None:
                local_path = os.path.basename(remote_file)
            
            print(f"Downloading {remote_file} to {local_path}...")
            
            with open(local_path, 'wb') as f:
                self.ftp.retrbinary(f'RETR {remote_file}', f.write)
            
            print(f"Downloaded: {local_path}")
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False

    def upload_file(self, local_file, remote_path=None):
        """Upload a file to server"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            if remote_path is None:
                remote_path = os.path.basename(local_file)
            
            print(f"Uploading {local_file} to {remote_path}...")
            
            with open(local_file, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_path}', f)
            
            print(f"Uploaded: {remote_path}")
            return True
        except Exception as e:
            print(f"Upload failed: {e}")
            return False

    def change_directory(self, directory):
        """Change current directory"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            self.ftp.cwd(directory)
            self.current_dir = self.ftp.pwd()
            print(f"Changed to: {self.current_dir}")
        except Exception as e:
            print(f"Failed to change directory: {e}")

    def make_directory(self, dirname):
        """Create a new directory"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            self.ftp.mkd(dirname)
            print(f"Created directory: {dirname}")
        except Exception as e:
            print(f"Failed to create directory: {e}")

    def delete_file(self, filename):
        """Delete a file"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            self.ftp.delete(filename)
            print(f"Deleted file: {filename}")
        except Exception as e:
            print(f"Failed to delete file: {e}")

    def rename(self, old_name, new_name):
        """Rename a file or directory"""
        if not self.connected:
            print("Not connected.")
            return
        
        try:
            self.ftp.rename(old_name, new_name)
            print(f"Renamed {old_name} to {new_name}")
        except Exception as e:
            print(f"Rename failed: {e}")

    def disconnect(self):
        """Close connection"""
        if self.ftp:
            try:
                self.ftp.quit()
                print("Disconnected from server.")
            except:
                self.ftp.close()
            self.connected = False


def main():
    print("=" * 60)
    print("FTP Client - File Transfer Program")
    print("=" * 60)
    
    client = FTPClient()
    
    # Get connection details
    host = input("Enter FTP server hostname/IP: ").strip()
    if not host:
        print("Hostname required.")
        return
    
    port_str = input("Port (default 21): ").strip()
    port = int(port_str) if port_str else 21
    
    if not client.connect(host, port=port):
        return
    
    # Interactive shell
    while True:
        try:
            print(f"\nCurrent directory: {client.current_dir}")
            cmd = input("\nftp> ").strip().lower()
            
            if cmd in ['quit', 'exit', 'bye']:
                client.disconnect()
                break
                
            elif cmd == 'ls' or cmd == 'dir':
                client.list_files()
                
            elif cmd.startswith('cd '):
                directory = cmd[3:].strip()
                client.change_directory(directory)
                
            elif cmd.startswith('get '):
                remote_file = cmd[4:].strip()
                client.download_file(remote_file)
                
            elif cmd.startswith('put '):
                local_file = cmd[4:].strip()
                if os.path.exists(local_file):
                    client.upload_file(local_file)
                else:
                    print(f"Local file not found: {local_file}")
                
            elif cmd.startswith('mkdir '):
                dirname = cmd[6:].strip()
                client.make_directory(dirname)
                
            elif cmd.startswith('delete ') or cmd.startswith('rm '):
                filename = cmd.split(' ', 1)[1].strip()
                client.delete_file(filename)
                
            elif cmd.startswith('rename '):
                parts = cmd[7:].strip().split()
                if len(parts) >= 2:
                    client.rename(parts[0], parts[1])
                else:
                    print("Usage: rename old_name new_name")
                    
            elif cmd == 'pwd':
                print(f"Current directory: {client.ftp.pwd()}")
                
            elif cmd == 'help':
                print("""
Commands:
  ls / dir          - List files in current directory
  cd <dir>          - Change directory
  get <file>        - Download file
  put <localfile>   - Upload file
  mkdir <name>      - Create directory
  delete/rm <file>  - Delete file
  rename <old> <new>- Rename file/dir
  pwd               - Show current directory
  help              - Show this help
  quit/exit         - Disconnect and exit
                """)
                
            else:
                print("Unknown command. Type 'help' for commands.")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"Unexpected error: {e}")