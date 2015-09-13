#!/usr/bin/env python
import io
import os
import subprocess
import pyimgur
import pyperclip
import sys

#if os.path.isdir(os.path.join(current_path, "data")):
#   current_path = os.path.join(current_path, "data")
pathtodir = os.path.expanduser('~');
print(pathtodir);
screenshot_path = pathtodir + "/.scriptshot.png";
print(screenshot_path);
# calls scrot with commandline arguments for selection, no cursor, savepath, nosession, exit after capture
scrot_quick = subprocess.call(["scrot", "-s", screenshot_path])

# register app with imgur
CLIENT_ID = "56bedd07cb62731"

# upload image at our path
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(screenshot_path, title="Uploaded with my super duper cool script")

# copy the image link to clip board
pyperclip.copy(uploaded_image.link)

# delete image
subprocess.call(["rm", screenshot_path])

