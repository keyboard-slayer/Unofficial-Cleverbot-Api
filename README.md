# Unofficial-Cleverbot-Api

## How to install ?

```
sudo apt install python python-pip
sudo pip install -r ./requirement.txt
sudo python ./setup.py install 
```

### How to install PhantomJS (required)

For [Debian](https://gist.github.com/julionc/7476620) based distro

For [Windows](https://www.joecolantonio.com/2014/10/14/how-to-install-phantomjs/)

For [Mac OSX](https://ariya.io/2012/02/phantomjs-and-mac-os-x-)

## How to use it ?

```
>>> from cleverbot import *
>>> bot = Cleverbot()
>>> bot.send("Hello")
>>> print(bot.get()) # Get the awnser
"Hi"
```
