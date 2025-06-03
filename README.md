# 🚀 Flood-script

This Python script performs a burst of HTTP GET requests to a target URL using multithreading. It can be used for testing how a server handles multiple simultaneous requests.

> ⚠️ **Use this script only in a controlled lab environment with explicit permission. Unauthorized use is illegal and unethical.**

---

## 📁 Files

- `flood_script.py`: The main script that sends HTTP GET requests in parallel.

---

## 🛠️ Requirements

- Python 3.x
- `requests` library (install with pip)

---

## 💻 How to Run

### Step 1: Clone this Repository

```bash
git clone https://github.com/Laxmitripathi67/Flood-script.git
cd Flood-script

### Step 2: Install Dependencies
```bash
pip install requests

### Step 3: Edit the Target

Open flood_script.py and change the target_url:
target_url = "http://<your-target-ip>/"

### Step 4: Run the Script

python flood_script.py

# Disclaimer 
This script is for educational and authorized testing purposes only. Do not use it to attack systems you do not own or have permission to test.
