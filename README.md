# These scripts are shortcuts for your daily tasks - currently available only for Linux OS.
<div>
<h2><b>Prerequisites:</b></h2> Python, Docker, Git
</div>
<div>
<h2><b>Setup:</b></h2>
1. Clone this project in your home directory)
  cd ~/
  git clone https://github.com/razvanvancea/linux_scripts.git
2. Open the .bashrc file (e.g. nano ~/.bashrc)
3. Add the following aliases at the bottom of the file
  alias 'sdocker'='python ~/linux_scripts/startdocker.py'
  alias 'szalenium'='python ~/linux_scripts/startzalenium.py'

<em>NOTE: you can replace 'sdocker' and 'szalenium' with any other shortcut name.</em>

4. Save and close the file
5. Reload the .bashrc file, using the following CLI command
  source ~/.bashrc
 </div> 
<h2><br>How to start the scripts?</br></h2>

<h3><br>Start Docker</br></h3>, executing via CLI: <br>sdocker</br>

It it will verify if the Docker daemon is already running. If so, it will notify you by a message. Otherwise, it will start the docker service.

<h3><b>Start Zalenium with a desired number of containers</b></h3>, executing via CLI: <br>szalenium 3</br>

The above command will create 3 containers. If you do not pass the second argument (3), a message asking for the number will be prompted in the terminal, waiting for your input (accepts only numbers).

