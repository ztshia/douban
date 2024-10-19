import requests
import json
import os

# 保存图片的文件夹路径
save_folder = './images/douban/'

# Json 文件路径
json_file_path = './data/douban/movie.json'

# 下载图片的函数，根据传入的图片 URL 和 id 下载图片
def download_file(image_url, image_id):
    # 确保保存图片的文件夹路径存在，如果不存在则创建
    os.makedirs(save_folder, exist_ok=True)

    # 根据图片 URL 发起 HTTP 请求下载图片，设置超时时间为 30 秒
    headers = {'Referer': 'https://doubanio.com'}
    response = requests.get(image_url, headers=headers, timeout=30)

    # 将图片保存为 [id].jpg 的格式
    file_name = f"{image_id}.jpg"
    save_path = os.path.join(save_folder, file_name)

    # 如果文件已经存在，提示文件存在；否则下载并保存
    if os.path.exists(save_path):
        print(f'文件已存在 {file_name}')
    else:
        print('文件不存在')
        with open(save_path, 'wb') as file:
            file.write(response.content)  # 将下载的图片内容写入文件
        print(f'图片已保存为 {file_name}')


# 打开并读取 JSON 文件
with open(json_file_path, 'r', encoding='utf-8') as file:
    data_json = json.load(file)

# 遍历 JSON 数据中的每一项，提取图片 URL 和 id
for item in data_json:
    image_url = item['subject']['pic']['normal']
    image_id = item['subject']['id']
    download_file(image_url, image_id)  # 调用下载函数
