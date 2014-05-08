torbot
======

Source for the TorBot robot platform Python library.

####Prerequisites:

```
  $ sudo apt-get install espeak i2c-tools python-espeak python-rpi.gpio \
        python-serial python-setuptools python-smbus
  $ sudo apt-get purge jackd
```

####Get the sources:

```
  $ git clone https://github.com/tkurbad/torbot.git
  $ cd torbot
  $ export TORBOTPROJECT="$( pwd )"
```

####Patch the configuration of Alsa:

```
  $ cd /usr/share/alsa
  $ sudo patch -p1 < $TORBOTPROJECT/patches/001-alsa.conf.patch
```

####Lay an egg:

```
  $ cd $TORBOTPROJECT
  $ python setup.py bdist_egg
```

####Install the Python egg (or put it in your PYTHONPATH):

```
  $ sudo easy_install dist/torbot-1.0-py2.7.egg
```

---

All credits go to Simon Monk. For the original ReadMe of his
raspirobotboard project, see below.

raspirobotboard
===============

Source for the RaspiRobotBoard Python library.

For full instructions for installation and use, see:

https://github.com/simonmonk/raspirobotboard/wiki
