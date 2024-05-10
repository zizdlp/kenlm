# 基于 Python:alpine 镜像构建
FROM python:alpine

# 设置工作目录
WORKDIR /app

COPY requirements.txt .

# 安装 Flask 和其它依赖
RUN pip install -r requirements.txt

# 安装 KenLM
RUN apk add --no-cache git g++ cmake make \
    && git clone https://github.com/kpu/kenlm.git \
    && cd kenlm \
    && pip install .