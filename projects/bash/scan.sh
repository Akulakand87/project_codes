#!/bin/bash

# This script is a simple CLI interface for nmap.

# Define the default scan type and port range.
SCAN_TYPE="syn"
PORT_RANGE="1-1024"

# Get the target IP address from the user.
echo "Enter the target IP address: "
read TARGET

# Get the scan type from the user.
echo "Select the scan type:"
echo "1. SYN scan (default)"
echo "2. TCP scan"
echo "3. UDP scan"
read SCAN_TYPE

# Get the port range from the user.
echo "Enter the port range to scan (default: 1-1024): "
read PORT_RANGE

# Run nmap with the specified target IP address, scan type, and port range.
nmap -sT -A $SCAN_TYPE $TARGET $PORT_RANGE

# Save the nmap output to a file.
cat nmap.out > nmap_scan.txt

# Display the nmap output to the console.
cat nmap.out
