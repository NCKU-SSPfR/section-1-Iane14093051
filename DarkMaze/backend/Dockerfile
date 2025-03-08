# TODO: Install the backend dependency package into the app folder inside the container.

# 使用 Python 3.11 作為基底映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 先複製 requirements.txt，確保 Docker cache 最優化
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 再複製其餘檔案
COPY . .

# 啟動應用
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

