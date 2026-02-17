import mss
import mss.tools
from datetime import datetime
from .config import SCREENSHOT_DIR

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{SCREENSHOT_DIR}/screen_{timestamp}.png"

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # primary screen
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)

    return filename, timestamp
