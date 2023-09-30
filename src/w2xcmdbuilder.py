# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

import w2xfiletypes as filetypes
import w2xvars as variables
import w2xfsio as filesystem


def build_proc(cpu_load, cpu_proc, cpu_save):
    return " -j " + str(int(cpu_load)) + ":" + str(int(cpu_proc)) + ":" + str(int(cpu_save))


def build_model(model_path):
    return " -m " + str(model_path)


def build_noise_reduction(noise_reduction, noise_reduction_lvl):
    if not noise_reduction:
        return " -n -1"
    else:
        return " -n " + str(int(noise_reduction_lvl))


def build_scale(scale):
    return " -s " + str(int(scale))


def build_filetype(filetype):
    return " -f " + filetypes.W2xFiletype.ft_to_string(filetype)


def build_input(input_file):
    return " -i " + str(input_file)


def build_output(output_directory, output_file, filetype):
    return " -o " + str(output_directory) + "/" + str(output_file) + "." + filetypes.W2xFiletype.ft_to_string(filetype)


class CommandBuilder:

    def builder(cpu_load, cpu_proc, cpu_save, model_path, noise_reduction, scale, input_filename, output_filename,
                output_directory, filetype,
                recursion=False, recurse_directory=0, noise_reduction_level=-1):

        base = variables.Vars.W2X_INTERP + build_proc(cpu_load, cpu_proc, cpu_save) + build_filetype(
            filetype) + build_model(
            model_path) + build_noise_reduction(noise_reduction, noise_reduction_level) + build_scale(scale)
        recursive_final = []
        if recursion:
            files = filesystem.FilesystemProber.get_files(recurse_directory)

            if not files:
                return False
            else:
                counter = 1
                for file in files:
                    recursive_final.append(
                        base + build_input(file) + build_output(output_directory, output_filename + "_" + str(
                            counter) + "_[x" + str(scale) + "]", filetype))
                    counter = counter + 1
        else:
            fle = base + build_input(input_filename) + build_output(output_directory, output_filename, filetype)
            recursive_final.append(fle)

        if len(recursive_final) != 0:
            return recursive_final
        else:
            return False
