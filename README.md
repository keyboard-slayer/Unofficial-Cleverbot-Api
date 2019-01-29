# Unofficial-Cleverbot-Api

## How to install ?

```
sudo apt install python python-pip
sudo pip install -r ./requirement.txt
sudo python ./setup.py install 
```

## How to use it ?

First, install Firefox and Geckodriver then it should work :p

```
>>> from cleverbot import *
>>> bot = Cleverbot()
>>> bot.send("Hello")
>>> print(bot.get()) # Get the awnser
"Hi"
```
