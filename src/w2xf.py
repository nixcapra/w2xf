# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

import subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import w2xcpu as cpu
import w2xvars as variables
import w2xcmdbuilder as command_builder
import os


class Main:
    def __init__(self):

        def reset(self):
            cpu_topology_write.set_value(1)
            cpu_topology_proc.set_value(int(cpu.CpuInfo.get_cores() / 2))
            cpu_topology_loading.set_value(1)
            noise_reduction_value.set_range(0, 3)
            scale_value.set_value(2)

            output_folder_selector.set_filename("/home/" + os.getlogin() + "/")
            output_folder_selector.set_filename("/home/" + os.getlogin() + "/")

            input_recursive_toggle.set_active(False)
            model_folder_picker.set_filename(variables.Vars.W2X_MODEL)

            noise_reduction_toggle(self, self)

        def noise_reduction_toggle(ASelf, BSelf):
            if not noise_reduction_switch.get_active():
                noise_reduction_value.set_sensitive(False)
            else:
                noise_reduction_value.set_sensitive(True)

        def recursive_toggle(self):
            if not input_recursive_toggle.get_active():
                input_folder_selector.hide()
                input_file_selector.show()
            else:
                input_folder_selector.show()
                input_file_selector.hide()

        def integrity():
            flag = True
            if not os.path.isdir(model_folder_picker.get_filename()):
                flag = False

            if not input_recursive_toggle.get_active():
                if not os.path.isfile(input_file_selector.get_filename()):
                    flag = False
            else:
                if not os.path.isdir(input_folder_selector.get_filename()):
                    flag = False

            if not os.path.isdir(output_folder_selector.get_filename()):
                flag = False

            if output_filename.get_text() == "":
                flag = False

            return flag

        def display_about(self):
            about.show()
            return 0

        def hide_about(ASelf, BSelf=0):
            about.hide()
            return 0

        def set_error_message(EMSG):
            error_dialog_label.set_text(str(EMSG))

        def display_error_dialog(self):
            error_dialog.show()

        def hide_error_dialog(a_self, b_self):
            error_dialog.hide()

        def submit(selfA):
            instruction = []
            if integrity():
                instruction = command_builder.CommandBuilder.builder(cpu_topology_loading.get_value(),
                                                                     cpu_topology_proc.get_value(),
                                                                     cpu_topology_write.get_value(),
                                                                     model_folder_picker.get_filename(),
                                                                     noise_reduction_switch.get_active(),
                                                                     scale_value.get_value(),
                                                                     input_file_selector.get_filename(),
                                                                     output_filename.get_text(),
                                                                     output_folder_selector.get_filename(),
                                                                     output_filetype_selector.get_active_id(),
                                                                     input_recursive_toggle.get_active(),
                                                                     input_folder_selector.get_filename(),
                                                                     noise_reduction_value.get_value())
            else:
                set_error_message("Invalid Inputs, cannot possibly execute.")
                display_error_dialog(self)
            print(instruction)
            run_instruction(instruction)

        def run_instruction(instructions):
            if instructions:
                for instruction in instructions:
                    subprocess.run(instruction, shell=True)
            else:
                set_error_message("Something went wrong. Did you select a directory with no images?")
                display_error_dialog(self)

        glade_file = "w2xf.glade"

        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)

        main_window = self.builder.get_object("Main")
        main_window.connect("delete-event", Gtk.main_quit)
        main_window.show()

        # About Dialog

        about = self.builder.get_object("AboutDiag")
        about.set_version(str(variables.Vars.W2XF_VERSION))

        about_exit = self.builder.get_object("AboutDiagCloseButton")
        about_exit.connect("clicked", hide_about)

        about_button = self.builder.get_object("VersionButton")
        about_button.connect("clicked", display_about)

        # Error Dialog

        error_dialog = self.builder.get_object("EDialog")

        error_dialog_exit = self.builder.get_object("EDiagCloseButton")
        error_dialog_exit.connect("clicked", hide_error_dialog)

        error_dialog_label = self.builder.get_object("EDiagLabel")

        # SpinButtons on Init

        cpu_topology_loading = self.builder.get_object("CpuTopolNumLoading")
        cpu_topology_loading.set_range(1, cpu.CpuInfo.get_cores())
        cpu_topology_loading.set_increments(1, 4)

        cpu_topology_proc = self.builder.get_object("CpuTopolNumProc")
        cpu_topology_proc.set_range(1, cpu.CpuInfo.get_cores())
        cpu_topology_proc.set_increments(1, 4)

        cpu_topology_write = self.builder.get_object("CpuTopolNumSave")
        cpu_topology_write.set_range(1, cpu.CpuInfo.get_cores())
        cpu_topology_write.set_increments(1, 4)

        # Model Folder Picker

        model_folder_picker = self.builder.get_object("ModelFolderPicker")

        # Noise Reduction

        noise_reduction_switch = self.builder.get_object("NoiseRedToggle")
        noise_reduction_switch.connect("state-set", noise_reduction_toggle)

        noise_reduction_value = self.builder.get_object("NoiseRedNum")
        noise_reduction_value.set_increments(1, 3)

        # Scaling

        scale_value = self.builder.get_object("ScaleGridNum")
        scale_value.set_range(1, 2)
        scale_value.set_increments(1, 1)

        # Input

        input_recursive_toggle = self.builder.get_object("InputRecursiveToggle")
        input_recursive_toggle.connect("toggled", recursive_toggle)

        input_file_selector = self.builder.get_object("InputFilePicker")
        input_file_selector.set_current_folder("/home/" + os.getlogin() + "/")
        input_folder_selector = self.builder.get_object("InputFolderPicker")

        # Output

        output_folder_selector = self.builder.get_object("OutputFolderPicker")
        output_filename = self.builder.get_object("OutputFilename")

        output_filetype_selector = self.builder.get_object("OutputFiletypeSelector")

        # Submit

        submit_button = self.builder.get_object("SubmitButton")
        submit_button.connect("clicked", submit)

        reset(self)


if __name__ == '__main__':
    main = Main()
    Gtk.main()
