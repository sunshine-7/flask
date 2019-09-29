import json
import urllib.request
import base64
import cv2
import numpy as np
import requests
from matplotlib import pyplot as plt
# #
# # def rgb2gray(rgb):
# #     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
# # url="http://localhost:5000/auth/signin"
# # new_url = urllib.request.Request(url)
# # response = urllib.request.urlopen(new_url)
# # result = response.read().decode('utf-8')  # 读取响应结果
# # result=urllib.parse.unquote(result[4:])
# # tImg = cv2.imdecode(np.fromstring(base64.b64decode(result), dtype='uint8'),1)
# # imgray = rgb2gray(tImg)
# # plt.imshow(imgray)
# # plt.show()
# # imgrayEncode = cv2.imencode(".jpg", imgray)[1]
# # result = base64.b64encode(np.array(imgrayEncode).tostring())

# user_info={'name':'liuwen'}
# # 客户端向服务端发送数据，r其实就是服务端对客户端的一个响应吗？？？？
# r = requests.post("http://127.0.0.1:5000/auth/signin/", data=user_info)
# print(r.text)
# w=requests.get("http://127.0.0.1:5000/auth/signin/")
# print(w.text)
imgPath = r"E:\pythonproject\LargeApp\app\mod_auth\pic.jpg"
img = cv2.imread(imgPath)
# print('img======\n',img)
imgEncode = cv2.imencode(".jpg", img)[1]
# print('imgEncode图片三维数组编码======\n',imgEncode)
imgstr=np.array(imgEncode).tostring()
# print("数组转换成字符串")
# print(imgstr)
imgData = base64.b64encode(imgstr)
# print("字符串加密",imgData)
punchType = "8"
data = {"pic": imgData, "mID": "1234567890", "punchType": punchType}
data = urllib.parse.urlencode(data)
#将字符串转换为字节
data = data.encode('utf-8')
# print(data)
url="http://127.0.0.1:5000/auth/signin/"
# class urllib.request.Request(url, data=None,
# headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个参数是请求链接，这个是必传参数，其他的都是可选参数。
# data 参数如果要传必须传 bytes （字节流）类型的，
# 如果是一个字典，可以先用 urllib.parse.urlencode() 编码。
new_url = urllib.request.Request(url,data,method="POST")
response = urllib.request.urlopen(new_url)
result = response.read().decode('utf-8')    #读取响应结果
print(result)
