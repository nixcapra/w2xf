# SPDX-FileCopyrightText: Copyright © 2023 nixcapra
# SPDX-License-Identifier: MIT

class W2xFiletype:

    def ft_to_string(filetype):
        if int(filetype) == 1:
            return "png"
        elif int(filetype) == 2:
            return "jpg"
        elif int(filetype) == 3:
            return "webp"
        else:
            return "png"


class W2xAllowedFt:
    ALLOWED_FILETYPES = [".png", ".jpg", ".webp"]
