import time
from PIL import ImageGrab

time.sleep(5)

# capture for 10 seconds
for i in range(1, 11):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)
