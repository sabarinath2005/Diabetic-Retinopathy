# verify_setup.py
# Purpose: Confirm every library is installed and importable
# Run this once after setup — never needed again after this

import sys

print("=" * 50)
print("ENVIRONMENT VERIFICATION")
print("=" * 50)

# --- Python Version ---
print(f"\n Python: {sys.version}")

# --- TensorFlow ---
import tensorflow as tf
print(f" TensorFlow: {tf.__version__}")

# --- Keras (bundled inside TensorFlow 2.15) ---
from tensorflow import keras
print(f" Keras: bundled with TensorFlow {tf.__version__}")

# --- NumPy ---
import numpy as np
print(f" NumPy: {np.__version__}")

# --- Pandas ---
import pandas as pd
print(f" Pandas: {pd.__version__}")

# --- OpenCV ---
import cv2
print(f" OpenCV: {cv2.__version__}")

# --- Matplotlib ---
import matplotlib
print(f" Matplotlib: {matplotlib.__version__}")

# --- Scikit-learn ---
import sklearn
print(f" Scikit-learn: {sklearn.__version__}")

# --- Flask ---
import flask
print(f" Flask: {flask.__version__}")

# --- Pillow ---
import PIL
print(f" Pillow: {PIL.__version__}")

# --- tqdm ---
import tqdm
print(f" tqdm: {tqdm.__version__}")

# --- Seaborn ---
import seaborn
print(f" Seaborn: {seaborn.__version__}")

print("\n" + "=" * 50)
print(" ALL IMPORTS SUCCESSFUL!")
print("=" * 50)