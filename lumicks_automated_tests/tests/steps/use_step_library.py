"""
Allows to get all step implementations from subdirectories.
"""

import os

STEPS_DIR = 'tests/steps'

for current_dir, _, files in os.walk(STEPS_DIR):
    if '__pycache__' not in current_dir:
        for file in files:
            __import__((current_dir + '.' + os.path.splitext(file)[0]).replace(os.path.sep, '.'))
