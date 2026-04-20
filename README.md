<div align="center">

# Zoho Notify

**Real-time desktop notifications for Zoho Mail unread messages.**

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3-3776ab?style=flat-square&logo=python)](https://www.python.org/)

</div>

---

A lightweight Python script that polls the Zoho Mail API for unread messages and sends desktop notifications using `notify-send`.

## Features

- **Instant Notifications** — Get notified as soon as an email hits your inbox.
- **Zoho OAuth2** — Securely authenticates using Zoho's refresh token flow.
- **Lightweight** — Minimal dependencies and low resource usage.
- **Systemd Integration** — Easily run as a background service.

## Prerequisites

- Python 3.x
- `libnotify` (for `notify-send`)
- Zoho Mail API credentials (Client ID, Client Secret, Refresh Token)

## Installation

```bash
git clone https://github.com/jedbillyb/zoho-notify.git
cd zoho-notify
pip install requests python-dotenv
```

## Configuration

Create a `.env` file in the project root:

```env
ZOHO_CLIENT_ID=your_client_id
ZOHO_CLIENT_SECRET=your_client_secret
ZOHO_REFRESH_TOKEN=your_refresh_token
```

## Usage

```bash
python zoho-notify.py
```

## Background Service (Systemd)

To run this as a background service on Linux, you can create a user systemd service:

```ini
# ~/.config/systemd/user/zoho-notify.service
[Unit]
Description=Zoho Mail Notifier

[Service]
ExecStart=/usr/bin/python3 /home/jed/projects/zoho-notify/zoho-notify.py
WorkingDirectory=/home/jed/projects/zoho-notify
Restart=always

[Install]
WantedBy=default.target
```

Then enable and start it:

```bash
systemctl --user daemon-reload
systemctl --user enable zoho-notify.service
systemctl --user start zoho-notify.service
```

---

<div align="center">
<sub>MIT © <a href="https://github.com/jedbillyb">jedbillyb</a> · Made with ❤️</sub>
</div>
