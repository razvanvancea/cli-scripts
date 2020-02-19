# These scripts are shortcuts for your daily tasks - currently available for Linux and MACOS operating systems.
Prerequisites: Python v3.7.6, Docker, Git

Setup:
1. Clone this project in your home directory)
```html
  cd ~/
  git clone https://github.com/razvanvancea/scripts.git
```
2. Open the .bashrc file
```html
nano ~/.bashrc
```
3. For LINUX users: Add the following aliases at the bottom of the file
```html
  alias sdocker='python3 ~/scripts/linux/startdocker.py'
  alias szalenium='python3 ~/scripts/linux/startzalenium.py'
```
3. For MACOS users: Add the following aliases at the bottom of the file
```html
alias szalenium='python3 ~/scripts/macos/startzalenium.py'
```
NOTE: 'sdocker' and 'szalenium' are only shortcut names. They can be renamed with any other names.

4. Save and close the file (e.g. for nano editor: CTRL+X, then press Y and Enter)
5. Reload the .bashrc file, using the following CLI command
```html
source ~/.bashrc
```

How to use the scripts?

For LINUX/MACOS users, to start Zalenium with a desired number of containers via CLI:
```html
szalenium 3
```
The above command will create 3 containers. If you do not pass the argument (3), a message asking for the number will be prompted in the terminal, waiting for your input (it accepts only numbers).

For LINUX users, to start Docker via CLI:
```html
sdocker
```

It it will verify if the Docker daemon is already running. If so, it will notify you by a console message. Otherwise, it will start the docker service.
