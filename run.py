#!/usr/bin/env python3
"""
Root entrypoint for running DhwaniLekh.
Usage:
    python run.py
"""

from pathlib import Path
import sys

# Add src/ to path so it can run directly without prior pip install -e .
SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from dhwanilekh.app import main

if __name__ == "__main__":
    main()
