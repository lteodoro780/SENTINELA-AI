#!/bin/bash

echo "Applying network lockdown rules..."

# Flush old rules
iptables -F
iptables -X

# Default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow localhost
iptables -A INPUT -i lo -j ACCEPT

# Allow established connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow Open WebUI
iptables -A INPUT -p tcp --dport 3000 -j ACCEPT

# Allow Ollama API
iptables -A INPUT -p tcp --dport 11434 -j ACCEPT

echo "Firewall rules applied."
