#!/usr/bin/env python
import Tkinter as tk
import roslaunch


class RunExperimentGUI:

    def __init__(self):
        self.dimensions = "250x100"

        self.switch_controller_node = roslaunch.core.Node("graspit_switch_controller", "switch_controller.py")
        self.threshold_controller_node = roslaunch.core.Node("graspit_threshold_controller", "run.sh")
        self.launcher = roslaunch.scriptapi.ROSLaunch()
        self.launcher.start()

        self.__mainWindow = tk.Tk()
        self.__mainWindow.geometry(self.dimensions)

        self.process = None
        self.process_name = ""

        self.current_process_label = tk.Label(self.__mainWindow, text="Current process: ")
        self._update_process_text()

        tk.Button(self.__mainWindow, text="Run Ultimate Switch Node", command=self._launch_switch_ui).pack()
        tk.Button(self.__mainWindow, text="Run sEMG Interface Node", command=self._launch_threshold_ui).pack()
        tk.Button(self.__mainWindow, text="Close current node", command=self._close_current_process).pack()

        self.__mainWindow.title("Input Command Center")
        self.__mainWindow.tk.mainloop()

    def _launch_switch_ui(self):
        self.process = self.launcher.launch(self.switch_controller_node)
        self.process_name = "Switch Controller"
        self._update_process_text()

    def _launch_alexa_ui(self):
        pass

    def _close_current_process(self):
        if self.process and self.process.is_alive():
            self.process.stop()

        self.process_name = "None"
        self._update_process_text()

    def _launch_threshold_ui(self):
        self.process = self.launcher.launch(self.threshold_controller_node)
        self.process_name = "sEMG Controller"
        self._update_process_text()

    def _update_process_text(self):
        self.current_process_label.config(text="Current process: {}".format(self.process_name))

if __name__ == '__main__':
    RunExperimentGUI()
