# 1。 获取image所有图片
# 2. 找到所有图片
# 3. 如果image有，但md里面没有，则删除
from os import listdir, remove
from re import match, findall

all_image_filename = listdir("./image")
all_image_filename = frozenset(all_image_filename)
# print(all_image_filename)

all_markdown_file = listdir(".")
all_markdown_used_image = []
for markdown_file in all_markdown_file:
    if not markdown_file.endswith(".md"):
        continue
    with open(f"./{markdown_file}", encoding="utf-8", mode="r") as f:
        file_content = f.read()
        image_path_list = findall(r"\(image/image-.*\.png\)", file_content)
        for image_path in image_path_list:
            all_markdown_used_image.append(image_path[7:-1])
all_used_image_filename = frozenset(all_markdown_used_image)
# print(all_image_filename)
# print(all_used_image_filename)
# print(all_image_filename.difference(all_used_image_filename))
all_need_del_image = all_image_filename.difference(all_used_image_filename)
for need_del_image in all_need_del_image:
    print(remove(f"./image/{need_del_image}"))





