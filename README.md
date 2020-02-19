# These scripts are shortcuts for your daily tasks - currently available only for Linux OS.
Prerequisites: Python v3.7.6, Docker, Git
Setup:
1. Clone this project in your home directory)
  cd ~/
  git clone https://github.com/razvanvancea/scripts.git
2. Open the .bashrc file (e.g. nano ~/.bashrc)
3. Add the following aliases at the bottom of the file
  alias 'sdocker'='python ~/linux_scripts/startdocker.py'
  alias 'szalenium'='python ~/linux_scripts/startzalenium.py'

NOTE: you can replace 'sdocker' and 'szalenium' with any other shortcut name.

4. Save and close the file
5. Reload the .bashrc file, using the following CLI command
  source ~/.bashrc

How to start the scripts?

Start Docker, executing via CLI: sdocker

It it will verify if the Docker daemon is already running. If so, it will notify you by a message. Otherwise, it will start the docker service.

Start Zalenium with a desired number of containers, executing via CLI: szalenium 3

The above command will create 3 containers. If you do not pass the second argument (3), a message asking for the number will be prompted in the terminal, waiting for your input (accepts only numbers).
