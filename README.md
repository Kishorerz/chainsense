# ChainSense: Secure Industrial IoT Logging with Blockchain

ChainSense is a secure data logging system designed for industrial environments. It leverages blockchain technology to ensure the integrity and tamper-proof storage of IoT sensor data—starting with temperature logs collected via Raspberry Pi.

## 🚀 Project Objective

In traditional industries, critical operational data is vulnerable to tampering or unauthorized changes when stored in physical logs or central databases. ChainSense addresses this by:
- Logging sensor data (e.g., temperature) from Raspberry Pi
- Generating SHA-256 hashes of this data
- Storing the hash and timestamp on a blockchain
- Enabling integrity verification through a web interface

---

## 🧩 Tech Stack

### Hardware
- Raspberry Pi 4
- DHT11 or DHT22 Temperature Sensor

### Software & Tools
- Python 3
- Adafruit_DHT (for sensor readings)
- Web3.py (for blockchain interactions)
- Solidity (Smart Contract)
- Ganache (Local Ethereum Blockchain)
- VS Code (Development)
- Git + GitHub (Version Control)
- Flask (Optional: API backend)
- HTML/CSS/JS (Web Dashboard UI)

---

## 📁 Project Structure

