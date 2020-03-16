import os


class ScreenShot:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, name):
        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshotpath = os.path.join(os.path.sep, ROOT_DIR, 'screenshots' + os.sep)
        self.driver.save_screenshot(screenshotpath + name + '.png')