import requests
from concurrent.futures import ThreadPoolExecutor
import time
# 定义发送请求的函数
def send_request():
    response = requests.get('http://localhost:8000/')
    return response.text

# 创建线程池
s=time.time()
num_task=10000
with ThreadPoolExecutor(max_workers=10) as executor:
    # 向线程池提交任务
    futures = [executor.submit(send_request) for _ in range(num_task)]
    
    # 获取任务的结果
    # for future in futures:
        # print(future.result())
e=time.time()
print(f"call {num_task}s, time consume:{e-s}s")