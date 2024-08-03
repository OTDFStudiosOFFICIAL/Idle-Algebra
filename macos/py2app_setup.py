from setuptools import setup

APP = ['../main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['kivy'],
    'iconfile': 'res/icon.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
