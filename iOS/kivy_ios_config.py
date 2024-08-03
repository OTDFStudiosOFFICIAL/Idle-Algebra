# Example configuration for kivy-ios

# Import necessary modules
import os

# Define the app name and package
APP_NAME = "Idle Algebra"
PACKAGE_NAME = "idlealgebra"

# Define the path to the main script
MAIN_PY = os.path.join(os.path.dirname(__file__), 'main.py')

# Define the requirements
REQUIREMENTS = ['python3', 'kivy']

# iOS deployment target version
IOS_MIN_VERSION = '9.0'

# The app icon (if exists)
ICON = os.path.join(os.path.dirname(__file__), 'res', 'icon.png')

# Other configurations
# ...
