#!/usr/bin/env python
import Tkinter as tk
import subprocess as sub
from PIL import Image, ImageTk
import rospy

dim = "250x100"

root = tk.Tk()
root.geometry(dim)

alexa_cmd = 'python ~/ros/bci_project/graspit_bci_ws/src/graspit_alexa_controller/scripts/graspit_alexa_controller.py'
switch_cmd = 'python ~/ros/bci_project/graspit_bci_ws/src/graspit_switch_controller/scripts/switch_controller.py'
bci_cmd = '~/ros/bci_project/graspit_bci_ws/src/graspit_threshold_controller/scripts/run.sh'

def toggle_experiment_type():
	if rospy.has_param('experiment_type'):
		experiment_type = rospy.get_param('experiment_type')
	else:
		experiment_type = "block"

	if experiment_type == "block":
		experiment_type = "object"
	else:
		experiment_type = "block"

	rospy.set_param("experiment_type", experiment_type)

tk.Button(root, text="Open Switch Interface", command=lambda: sub.call(switch_cmd, shell=True)).pack()
# tk.Button(root, text="Open Echo Interface", command=lambda: sub.call(alexa_cmd, shell=True)).pack()
tk.Button(root, text="Open BCI Interface", command=lambda: sub.call(bci_cmd, shell=True)).pack()
tk.Button(root, text="Change Experiment Type", command=toggle_experiment_type).pack()


img = Image.open('icon.png')
pic = ImageTk.PhotoImage(img)
root.tk.call('wm', 'iconphoto', root._w, pic)
root.title("Input Command Center")
root.tk.mainloop()