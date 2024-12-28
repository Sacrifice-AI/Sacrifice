"""
Setup Environment Script for Sacrifice AI
This script automates the setup process for the Sacrifice AI project.
"""

import os
import subprocess
import sys


def create_virtual_env():
    """Create a virtual environment."""
    print("Creating virtual environment...")
    if not os.path.exists("venv"):
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("Virtual environment created successfully.")
    else:
        print("Virtual environment already exists.")


def install_dependencies():
    """Install dependencies from requirements.txt."""
    print("Installing dependencies...")
    subprocess.check_call([os.path.join("venv", "bin", "pip"), "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully.")


def main():
    """Main script execution."""
    create_virtual_env()
    install_dependencies()
    print("Environment setup complete!")


if __name__ == "__main__":
    main()
