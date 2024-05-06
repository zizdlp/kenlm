import requests
from concurrent.futures import ThreadPoolExecutor
import time
# 定义发送请求的函数
def test_base_api():
    response = requests.get('http://localhost:8000/')
    return response.text

def test_kenlm_api():

    # 准备要发送的 JSON 数据
    data = {
        "lang": "zh",
        "text": "你好"
    }

    # 发送 POST 请求
    response = requests.post('http://localhost:8000/kenlm_api', json=data)

    # 输出响应内容
    print(response.text)



# 创建线程池
s=time.time()
num_task=1
with ThreadPoolExecutor(max_workers=10) as executor:
    # 向线程池提交任务
    futures = [executor.submit(test_kenlm_api) for _ in range(num_task)]
    
    # 获取任务的结果
    # for future in futures:
        # print(future.result())
e=time.time()
print(f"call {num_task}s, time consume:{e-s}s")