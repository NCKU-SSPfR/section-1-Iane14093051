# 使用適合的基礎映像
FROM python:3.9  

# 設定工作目錄
WORKDIR /web 

# 複製專案文件到容器內
COPY . .  

# 安裝必要的依賴（假設使用 Flask）
RUN pip install -r requirements.txt  

# 設定容器啟動時執行的指令
CMD ["python", "main.py"]
