# 📂FTP Client

A simple, interactive command-line FTP client written in Python for transferring files to and from remote web servers.

---
## 🧑‍💻Features

- ✅ Connect to any FTP server
- ✅ List files and directories (`ls` / `dir`)
- ✅ Download files (`get`)
- ✅ Upload files (`put`)
- ✅ Navigate directories (`cd`, `pwd`)
- ✅ Create directories (`mkdir`)
- ✅ Delete files (`delete` / `rm`)
- ✅ Rename files and directories
- ✅ Password-protected login (hidden input)
- ✅ Clean, user-friendly interface
- ✅ Error handling and feedback

---
## 🍃Requirements

- Python 3.6 or higher
- No external dependencies (uses built-in `ftplib`)

---

## ⬇️Installation

1. **Download the script**

   ```bash
   curl -O https://example.com/ftp_client.py
   # or copy the code from ftp_client.py

Make it executable (optional)
```
chmod +x ftp_client.py
```

---
## ❔Usage
```
Bash python3 ftp_client.py
```

Interactive Commands
Once connected, you can use the following commands at the ftp> prompt:
## Interactive Commands
```
| Command                        | Description                              | Example                          |
|--------------------------------|------------------------------------------|----------------------------------|
| `ls` / `dir`                   | List files in current directory          | `ls`                             |
| `cd <directory>`               | Change directory                         | `cd /public`                     |
| `get <filename>`               | Download a file from server              | `get image.jpg`                  |
| `put <localfile>`              | Upload a local file to server            | `put report.pdf`                 |
| `mkdir <name>`                 | Create a new directory                   | `mkdir backups`                  |
| `delete <file>` / `rm <file>`  | Delete a file                            | `delete old.log`                 |
| `rename <old> <new>`           | Rename file or directory                 | `rename old.txt new.txt`         |
| `pwd`                          | Show current directory                   | `pwd`                            |
| `help`                         | Show help menu                           | `help`                           |
| `quit` / `exit` / `bye`        | Disconnect and exit                      | `quit`                           |
```
---
```
====================================================
FTP Client - File Transfer Program
====================================================
```
Enter FTP server hostname/IP: ftp.example.com
Port (default 21): 
Username: john_doe
Password: 
220 ProFTPD Server ready.

ftp> ls
Directory listing for: /home/john

ftp> get website_backup.zip
Downloading website_backup.zip to website_backup.zip...
Downloaded: website_backup.zip

ftp> cd public_html
Changed to: /home/john/public_html

ftp> put index.html
Uploading index.html to index.html...
Uploaded: index.html

ftp> quit
Disconnected from server.
Goodbye!

---

## ⚠️Security Notes
```
FTP is inherently insecure (transmits data in plain text).
For sensitive data, use SFTP (SSH File Transfer Protocol) instead.
Never hardcode passwords in scripts.
Consider using environment variables or a .env file for credentials in automated scripts.
```
---

## Advanced Usage (Scripting)

```
You can also use the FTPClient class programmatically:
Pythonfrom ftp_client import FTPClient
```
```
client = FTPClient()
if client.connect("ftp.example.com", "user", "password"):
    client.download_file("remote.txt", "local_copy.txt")
    client.upload_file("important.pdf")
    client.disconnect()
````
---

## Future Enhancements
```
 SFTP support (paramiko)
 GUI version (Tkinter or customtkinter)
 Progress bars for large files
 Batch operations (upload/download multiple files)
 Configuration file support
 Passive/Active mode toggle
 File size and date formatting
```
---

### 🤝 Open to Opportunities

- Backend / Full-Stack Internships  
- Freelance web projects  
- AI/ML and productivity-focused collaborations  

---

### 📫 Contact & Socials

<p align="center">
  <a href="mailto:aryanbhalsing7090@gmail.com">
    <img src="https://img.shields.io/badge/Email-aryanbhalsing7090%40gmail.com-red?style=for-the-badge&logo=gmail" />
  </a>
  <a href="https://www.linkedin.com/in/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LinkedIn-iamaryanbhalsing-blue?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://github.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/GitHub-iamaryanbhalsing-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://leetcode.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LeetCode-Profile-orange?style=for-the-badge&logo=leetcode" />
  </a>
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=iamaryanbhalsing&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>

---
<img src="https://camo.githubusercontent.com/a5dbb660f658cb0ba61949a83a2eac3bde636395a476ecc7c16124d2a1f9d8a0/68747470733a2f2f73746174732e70706861742e746f702f69636f6e733f6e616d653d6170706c652c617263686c696e75782c646f636b65722c646a616e676f2c666173746170692c6769746c61622c6769742c6769746875622c6a736f6e2c6a6176617363726970742c6c696e75782c6d6f6e676f64622c6e656f76696d2c6e67696e782c706f737467726573716c2c707974686f6e2c727573742c72656163742c72656469732c7461696c77696e646373732c26636f6c756d6e733d3230" />

---
