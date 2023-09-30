![](https://github.com/nixcapra/w2xf/blob/master/media/icons/icon_256.png)
# w2xf

w2xf is a somewhat user-friendly GTK frontend for [waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan), a program that specializes in upscaling and enhancing images. I personally developed w2xf some time ago for my own use. Although it may not be flawless, it is functional and gets the job done.

>If you are searching for the primary repository of nihui's waifu2x-ncnn-vulkan, you can find it [here](https://github.com/nihui/waifu2x-ncnn-vulkan).

# Screenshots
![](https://github.com/nixcapra/w2xf/blob/master/media/screenshots/adw_light.png)
![](https://github.com/nixcapra/w2xf/blob/master/media/screenshots/adw_dark.png)

# Features Supported by w2xf for waifu2x-ncnn-vulkan
- Single image upscaling
- Option to select models
- Bulk upscaling of all images in a folder
- Effective reduction of image noise, including compression artifacts such as those caused by JPEG compression

# Binaries
w2xf includes the precompiled binaries and models of waifu2x-ncnn-vulkan within its repository. If you prefer to build your own binaries, please refer to [this guide](https://github.com/nihui/waifu2x-ncnn-vulkan#build-from-source).

# Usage
>Currently, w2xf does not have packages available for any distribution. I will likely create packages for Debian and possibly make a Flatpak or AppImage available in the future. However, you can still run it in its current state.

Install the following on Debian 12:

    sudo apt install python3-gi python-gi-dev

Then run:

    python3 w2xf.py
    
# Improving

I am generally open and grateful for contributions, but please understand that I may not be able to respond to pull requests (PRs) promptly. If you wish to report a bug, I am also appreciative. However, please be aware that I will disregard any theming bugs that I cannot reproduce on Adwaita.
Please limit bug reports to issues that are directly related to w2xf only. Bugs or problems related to waifu2x-ncnn-vulkan should be reported separately through the appropriate channels or [repositories](https://github.com/nihui/waifu2x-ncnn-vulkan) dedicated to waifu2x-ncnn-vulkan. 

### Things that i want to do in the future:

- Make packages available, primarily .deb, Flatpak, and/or AppImage.
- Port the GUI to Gtk4 and libadw.
- Add XDG desktop integration.
