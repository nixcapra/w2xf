# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

import multiprocessing


class CpuInfo:

    @staticmethod
    def get_cores():
        return multiprocessing.cpu_count()
