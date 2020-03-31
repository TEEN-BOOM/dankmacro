import io
import os.path
from setuptools import setup

setup(
    name = "dankmacro",        # what you want to call the archive/egg
    version = '1.2.5',
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
    url = "https://github.com/TEEN-BOOM/dankmacro",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "dankmacro = dankmacro.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)
