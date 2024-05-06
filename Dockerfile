# 基于 Python:alpine 镜像构建
FROM python:alpine

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录中
COPY . .

# 安装 Flask 和其它依赖
RUN pip install -r requirements.txt

# 暴露端口
EXPOSE 8000

# 使用 Gunicorn 启动 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
