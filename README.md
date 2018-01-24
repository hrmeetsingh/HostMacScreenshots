## HostMacScreenshots
Wrote this one for automating the process of using the screenshots taken on mac in my locally hosted [remarkjs](https://remarkjs.com) markdown presentations.
Additional benefits
- No need to manually copy my screenshots to locations other than desktop and refer them
- Desktop is cleaned up as soon as screenshot is taken
- Quick
- Did not change my system settings to store screenshots elsewhere

### TODO
1. Can be done efficiently by binding to the system's screenshot event, no additional thread would be required
2. Currently written to work with Python 2.7, Mac OS Sierra, Python 3 might need some changes

### Usage
```bash
~/Desktop$ git clone https://github.com/hrmeetsingh/HostMacScreenshots.git
~/Desktop$ cd HostMacScreenshots
~/Desktop/HostMacScreenshots$ python HostMacScreenshots.py
```
