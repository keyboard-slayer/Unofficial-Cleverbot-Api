from setuptools import setup

import cleverbot

setup(name='Cleverbot',
      version='1.0',
      description='Unofficial Cleverbot Api',
      url='https://github.com/0v3rl0w/Unofficial-Cleverbot-Api',
      author='0v3rl0w',
      license='GPL',
      packages=['cleverbot'],
      install_required=['selenium'],
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Natural Language :: French",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows"
      ]
      zip_safe=False)
