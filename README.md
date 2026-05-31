# rpc-htop
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/redbith/rpc-htop)

A minimalist, terminal-style Discord Rich Presence client for Linux that displays real-time CPU, RAM, and battery status using crisp ANSI block characters for a clean, `htop`-inspired look.

## Features

- **ANSI Progress Bars:** Custom alignment using precise block characters (`████░░░`) that preserve layout consistency across different devices and fonts.
- **Resource Efficient:** Light on dependencies and system resources, updating data every 15 seconds.
- **Systemd Integration:** Runs seamlessly in the background as a user service.
- **Zero Bloat:** No external emojis or clutter—just pure system status metrics.

## Preview

The presence will display your system stats like this in Discord:
```text
Playing a game
LINUX
CPU: ████░░░ 52.3%
RAM: ██░░░░░ 28.1% | 🔌 22.0%
47:10 elapsed
```

## Prerequisites

Ensure you have Python 3 and pip installed on your Linux system.

You will also need the `pypresence` and `psutil` libraries. Install them using pip:
```bash
pip install pypresence psutil
```

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/redbith/rpc-htop.git
    cd rpc-htop
    ```

2.  Copy the script to your local bin directory, renaming it to match the service file:
    ```bash
    mkdir -p ~/.local/bin
    cp rpc-htop.py ~/.local/bin/rpc_htop.py
    chmod +x ~/.local/bin/rpc_htop.py
    ```

3.  Configure the Systemd user service:
    ```bash
    mkdir -p ~/.config/systemd/user/
    cp rpc-htop.service ~/.config/systemd/user/rpc-htop.service
    ```

4.  Enable and start the service:
    ```bash
    systemctl --user daemon-reload
    systemctl --user enable --now rpc-htop.service
    ```
    You can check the status of the service at any time with `systemctl --user status rpc-htop.service`.

## Configuration

If you wish to use your own Discord Developer Application, open `~/.local/bin/rpc_htop.py` with a text editor and replace the `client_id` variable with your application ID:

```python
client_id = "YOUR_APPLICATION_ID"
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
