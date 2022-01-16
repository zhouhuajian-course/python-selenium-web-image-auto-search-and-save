"""
图片资源自动搜索下载

@author  : zhouhuajian
@version : v1.0
"""
from os.path import dirname

from lxml.etree import HTML
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ImageAutoSearchAndSave:
    """图片自动搜索保存"""

    def __init__(self, keyword, limit=0):
        """初始化"""
        self.driver = webdriver.Chrome(executable_path=dirname(__file__) + '/chromedriver.exe')
        self.keyword = keyword
        self.limit = limit  # 0表示没有限制
        self.count = 0  # 用来计数
        self.all_detail_link = []

    def run(self):
        """开始运行"""
        print("========= 开始 =========")
        # 访问首页
        self.driver.get("https://pixabay.com/")
        # 搜索图片
        self._search_image()
        # 遍历所有页面
        self._iter_all_page()
        print("========= 结束 =========")

    def _search_image(self):
        """搜索图片"""
        elem = self.driver.find_element_by_css_selector("input[name]")
        elem.send_keys(self.keyword + Keys.ENTER)

    def _iter_all_page(self):
        """遍历所有页面"""
        # 获取总页面
        elem = self.driver.find_element_by_css_selector("span[class^=total]")
        page_total = int(elem.text.strip("/ "))
        print(f"总页面数：{page_total}")
        # 遍历所有页面
        base_url = self.driver.current_url
        for page_num in range(1, page_total + 1):
            print(f"正在访问第{page_num}页")
            if page_num > 1:
                self.driver.get(f"{base_url}?pagi={page_num}&")
            #  href属性
            root = HTML(self.driver.page_source)
            detail_links = root.xpath('//div[starts-with(@class, "results")]//a[starts-with(@class, "link")]/@href')
            # print(detail_links)
            is_reach_limit = False
            for detail_link in detail_links:
                self.all_detail_link.append(detail_link)
                self.count += 1
                if self.limit > 0 and self.count == self.limit:
                    is_reach_limit = True
                    print(f"已达到限制{self.limit}，结束收集图片详情页链接")
                    break
            if is_reach_limit:
                break
        print(f"共收集{len(self.all_detail_link)}个图片详情链接")


if __name__ == '__main__':
    keyword = "sunflower"
    limit = 3
    ImageAutoSearchAndSave(keyword, limit).run()
