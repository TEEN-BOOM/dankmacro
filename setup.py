import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(os.path.dirname(__file__), 'dankmacro/VERSION.txt')
with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
  version = f.read().strip()

setup(
    name = "dankmacro",        # what you want to call the archive/egg
    version = version,
    packages=["dankmacro"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=['pynput==1.6.8'],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {"dankmacro": ["VERSION.txt"]},
    author="TEEN_BOOM",
    author_email = "ojasscoding@gmail.com",
    description = "A python macro for dank memer discord",
    license = "MIT",
    keywords= "macro discord python dank memer",
    url = "git+https://github.com/TEEN-BOOM/dankmacro#egg=dankmacro",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "dankmacro = dankmacro.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)
