# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

import w2xfiletypes as filetypes
import os


class FilesystemProber:

    @staticmethod
    def isolate(files):
        final = []

        for file in files:
            if str(file)[-4:] in filetypes.W2xAllowedFt.ALLOWED_FILETYPES and str(file)[0] != ".":
                final.append(file)

        return final

    @staticmethod
    def get_files(path):
        files = []
        if os.path.isdir(path):
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    files.append(os.path.join(path, file))
        else:
            return False

        final = FilesystemProber.isolate(files)
        if len(final) == 0:
            return False
        else:
            return final
