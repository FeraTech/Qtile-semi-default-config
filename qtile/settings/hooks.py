from libqtile import hook
import subprocess

@hook.subscribe.startup_once
def autostart():
	# Change frank for your username (to know your username, type in the terminal: echo $USER)
    subprocess.call(["/home/frank/.config/qtile/scripts/autostart.sh"])
