# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11
# 設定工作目錄
WORKDIR /app

# 複製專案文件到容器內
COPY . .  

# 安裝必要的依賴
RUN pip install -r requirements.txt  

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
