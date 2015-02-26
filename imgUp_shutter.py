import io
import os
import subprocess
import pyimgur
import pyperclip
import sys

pathname = os.path.dirname(sys.argv[0])
current_path = os.path.abspath(pathname)
print(current_path)
if os.path.isdir(os.path.join(current_path, "data")):
   current_path = os.path.join(current_path, "data")

screenshot_path = os.path.join(current_path, "scriptshot.png")

# calls shutter with commandline arguments for selection, no cursor, savepath, nosession, exit after capture
shutter_quick = subprocess.call(["shutter", "-s", "-C","--output={0}".format(screenshot_path) , "--no_session", "--exit_after_capture"])

# register app with imgur
CLIENT_ID = "56bedd07cb62731"

# upload image at our path
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(screenshot_path, title="Uploaded with my super duper cool script")

# copy the image link to clip board
pyperclip.copy(uploaded_image.link)

# delete image
subprocess.call(["rm", screenshot_path])

