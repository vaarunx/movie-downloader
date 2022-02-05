#!/bin/bash
sudo protonvpn c -f -p tcp #Running VPN
python3 findtorrent.py  #Running the Python File

sudo protonvpn d #Disconnecting VPN