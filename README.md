# rpc-htop

A minimalist, terminal-style Discord Rich Presence client for Linux that displays real-time CPU, RAM, and battery status using crisp ANSI block characters.

## Features

- **ANSI Progress Bars:** Custom alignment using precise block characters (`████░░░`) that preserve layout consistency across different devices and fonts.
- **Resource Efficient:** Light on dependencies and system resources, updating data every 15 seconds.
- **Systemd Integration:** Runs seamlessly in the background as a user service.
- **Zero Bloat:** No external emojis or clutter on core metrics—just pure system status.

## Preview

```text
Playing LINUX
CPU: ████░░░ 52.3%
RAM: ██░░░░░ 28.1% | 🔌 22.0%
47:10 elapsed

Prerequisites

Ensure you have Python 3 and pip installed on your Linux system.
Bash

pip install pypresence psutil

Installation

    Clone the repository:
    Bash

    git clone [https://github.com/YOUR_USERNAME/rpc-htop.git](https://github.com/YOUR_USERNAME/rpc-htop.git)
    cd rpc-htop

    Move the script to your local bin directory:
    Bash

    mkdir -p ~/.local/bin
    cp rpc_htop.py ~/.local/bin/rpc_htop.py
    chmod +x ~/.local/bin/rpc_htop.py

    Configure the Systemd User Service:
    Bash

    mkdir -p ~/.config/systemd/user/
    cp rpc-htop.service ~/.config/systemd/user/rpc-htop.service

    Enable and Start the Service:
    Bash

    systemctl --user daemon-reload
    systemctl --user enable rpc-htop.service
    systemctl --user start rpc-htop.service

Configuration

If you wish to use your own Discord Developer Application, open rpc_htop.py and replace the client_id variable with your own:
Python

client_id = "YOUR_APPLICATION_ID"

License

This project is open-source and available under the MIT License.
