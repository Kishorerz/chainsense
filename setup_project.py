import os
import subprocess
import sys

def install_requirements():
    # Create virtual environment if not already created
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])

    # Activate virtual environment
    if os.name == 'nt':  # Windows
        activate_script = os.path.join("venv", "Scripts", "activate")
    else:  # macOS/Linux
        activate_script = os.path.join("venv", "bin", "activate")

    # Install required dependencies
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "web3"])

    # Optionally generate requirements.txt if it doesn't exist
    if not os.path.exists("requirements.txt"):
        print("Generating requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "freeze", ">", "requirements.txt"])

def run_flask_server():
    print("Starting Flask server...")
    subprocess.check_call([sys.executable, "backend/server.py"])

def main():
    install_requirements()
    run_flask_server()

if __name__ == "__main__":
    main()
