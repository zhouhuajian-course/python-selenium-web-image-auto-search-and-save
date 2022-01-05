"""
图片资源自动搜索下载

@author  : zhouhuajian
@version : v1.0
"""
from os.path import dirname

from selenium import webdriver


class ImageAutoSearchAndSave:
    """图片自动搜索保存"""

    def __init__(self):
        """初始化"""
        self.driver = webdriver.Chrome(executable_path=dirname(__file__) + '/chromedriver.exe')

    def run(self):
        """开始运行"""
        print("========= 开始 =========")
        # 访问首页
        self.driver.get("https://pixabay.com/")
        print("========= 结束 =========")


if __name__ == '__main__':
    ImageAutoSearchAndSave().run()
