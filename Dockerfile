# 轻量级 Python 基础镜像
FROM python:3.10-slim

# 让 Python 不生成 .pyc、并立即输出日志
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 工作目录
WORKDIR /app

# 先复制依赖清单并安装（利用缓存加速）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再复制源代码
COPY . .

# 容器对外暴露的端口（文档用）
EXPOSE 80

# 启动命令（用 Uvicorn 起 FastAPI）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
