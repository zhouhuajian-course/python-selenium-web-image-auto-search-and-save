"""
图片资源自动搜索下载

@author  : zhouhuajian
@version : v1.0
"""
from os.path import dirname

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ImageAutoSearchAndSave:
    """图片自动搜索保存"""

    def __init__(self, keyword):
        """初始化"""
        self.driver = webdriver.Chrome(executable_path=dirname(__file__) + '/chromedriver.exe')
        self.keyword = keyword

    def run(self):
        """开始运行"""
        print("========= 开始 =========")
        # 访问首页
        self.driver.get("https://pixabay.com/")
        # 搜索图片
        self._search_image()
        # 遍历所有图片列表页面
        self._iter_all_page()
        print("========= 结束 =========")

    def _search_image(self):
        """搜索图片"""
        elem = self.driver.find_element_by_css_selector("input[name]")
        elem.send_keys(self.keyword + Keys.ENTER)

    def _iter_all_page(self):
        """遍历所有图片列表页面"""
        # 获取页面总数
        elem = self.driver.find_element_by_css_selector("span[class^=total]")
        page_total = int(elem.text.strip("/ "))
        print(f"总页面数：{page_total}")
        # 遍历所有页面
        base_url = self.driver.current_url
        for page_num in range(1, page_total + 1):
            print(f"正在访问第{page_num}页")
            if page_num > 1:
                self.driver.get(f"{base_url}?pagi={page_num}&")


if __name__ == '__main__':
    keyword = "sunflower"
    ImageAutoSearchAndSave(keyword).run()
