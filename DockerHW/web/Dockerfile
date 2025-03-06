FROM python:3.11-slim
# 設定工作目錄
WORKDIR /web_run

# 複製專案文件到容器內
COPY . .  

# 安裝必要的依賴
RUN pip install -r requirements.txt  

CMD ["python", "main.py"]
