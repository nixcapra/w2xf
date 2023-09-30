# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

import os


class Vars:
    INSTALLATION_DIRECTORY = os.getcwd()

    W2X_INTERP = INSTALLATION_DIRECTORY + "/../w2x-content/bin/waifu2x-ncnn-vulkan"
    W2X_MODEL = INSTALLATION_DIRECTORY + "/../w2x-content/models/models-cunet"

    W2XF_VERSION = 0.1
