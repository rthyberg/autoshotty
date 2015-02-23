import io
import os
import subprocess
import pyimgur
import pyperclip
# refer to man pages for what this does
shutter_quick = subprocess.call(["shutter", "-s", "-C", "--output=~/my_scripts/data/scriptshot.png", "--no_session", "--exit_after_capture"])


# this what im working on now
CLIENT_ID = "56bedd07cb62731"
PATH = "data/scriptshot.png"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with my super duper cool script")

pyperclip.copy(uploaded_image.link)


subprocess.call(["rm", PATH])


