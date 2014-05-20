torbot
======

Source for the TorBot robot platform Python library.

####Prerequisites:

```
  $ sudo apt-get install espeak i2c-tools python-espeak python-rpi.gpio \
        python-serial python-setuptools python-smbus
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

####Enable jackd audio server:

```
  $ echo "tmpfs /run/shm    tmpfs   rw,nosuid,nodev,noexec,relatime,size=96M   0   0" \
        > /etc/fstab
  $ mount /run/shm -oremount,size=96M
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

####See INSTALL.txt for further information

All credits go to Simon Monk. For the original ReadMe of his
raspirobotboard project, see below.

raspirobotboard
===============

Source for the RaspiRobotBoard Python library.

For full instructions for installation and use, see:

https://github.com/simonmonk/raspirobotboard/wiki
