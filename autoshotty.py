#!/usr/bin/env python3
import io
import os
import subprocess
from imgurpython import ImgurClient
import pyperclip
import sys

# Find home path
pathtodir = os.path.expanduser('~')
screenshot_path = pathtodir + "/.scriptshot.png"
# calls maim with commandline arguments for selection, no cursor, savepath, nosession, exit after capture
maim_quick = subprocess.call(["maim", "-s", screenshot_path])

# register app with imgur
CLIENT_ID = "9ead9b7b006931b"
CLIENT_SECRET = ""

# upload image at our path
im = ImgurClient(CLIENT_ID, CLIENT_SECRET);
uploaded_image = im.upload_from_path(screenshot_path)

# copy the image link to clip board
pyperclip.copy(uploaded_image['link'])

# delete image
subprocess.call(["rm", screenshot_path])
