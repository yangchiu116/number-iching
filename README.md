# 數字易經磁場分析器 (Number I-Ching Magnetic Field Analyzer)

這是一個基於數字易經理論的應用程式，旨在分析一串數字（例如手機號碼、身分證號碼等）中潛在的「磁場組合」。它最初作為一個 Python 命令列工具，現已擴展為一個基於 Flask 的網頁應用程式。

## 功能 (Features)

*   **數字磁場分析：** 根據預定義的數字對分析規則，識別出數字序列中的天醫、生氣、延年、伏位、絕命、五鬼、禍害、六煞等磁場。
*   **命令列介面 (CLI)：** 允許用戶在終端機中輸入數字進行分析。
*   **網頁應用程式 (Web Application)：** 提供一個友善的網頁介面，用戶可以在瀏覽器中輸入數字並即時查看分析結果。

## 專案結構 (Project Structure)

*   `main.py`: 原始的命令列介面程式，用於在終端機中運行數字分析。
*   `calculator.py`: 包含 `DigitalYiJingCalculator` 核心邏輯的模組，定義了數字磁場的規則和分析方法。
*   `app.py`: Flask 網頁應用程式的入口點，處理網頁請求，並呼叫 `calculator.py` 進行數字分析。
*   `requirements.txt`: 專案所需的 Python 依賴清單。
*   `templates/`: 存放網頁應用程式的 HTML 模板。
    *   `templates/index.html`: 網頁應用程式的單一 HTML 頁面，包含數字輸入介面和結果顯示區。

## 本機運行 (Local Setup)

### 前提條件 (Prerequisites)

*   Python 3.x
*   pip (Python 套件管理器)

### 1. 安裝依賴 (Install Dependencies)

在專案的根目錄下，開啟終端機並執行：

```bash
pip install -r requirements.txt
```

### 2. 運行命令列介面 (Running the CLI Application)

```bash
python main.py
```

程式將提示您輸入一串數字，然後在終端機中顯示分析結果。

### 3. 運行網頁應用程式 (Running the Web Application)

```bash
python app.py
```

應用程式啟動後，在您的網頁瀏覽器中訪問 `http://127.0.0.1:5000/`。您將看到網頁介面，可以在其中輸入數字並查看分析結果。

## 部署到 AWS EC2 並使用 ngrok (Deployment to AWS EC2 with ngrok)

本節概述將應用程式部署到 AWS EC2 實例並透過 ngrok 臨時暴露的步驟。

### 1. 啟動 EC2 實例 (Launch an EC2 Instance)

1.  登入 AWS Console，前往 EC2 服務。
2.  啟動一個新的 EC2 實例，建議選擇 **Ubuntu Server LTS** AMI (例如 `t2.micro`，符合免費方案資格)。
3.  配置安全組 (Security Group)，至少開放 **SSH (Port 22)** 和 **HTTP (Port 80)** 的入站流量。
4.  創建並下載一個新的密鑰對 (`.pem` 檔案)，妥善保管。

### 2. 連接到 EC2 實例 (Connect to EC2 Instance)

在您的本機終端機中，使用 SSH 連接到 EC2 實例：

```bash
chmod 400 /path/to/your-key-pair.pem
ssh -i /path/to/your-key-pair.pem ubuntu@YOUR_EC2_PUBLIC_DNS_OR_IP
```

將 `/path/to/your-key-pair.pem` 替換為您的 `.pem` 檔案路徑，`YOUR_EC2_PUBLIC_DNS_OR_IP` 替換為您 EC2 實例的公共 DNS 或 IP 地址。

### 3. 在 EC2 上安裝必要軟體 (Install Required Software on EC2)

在 EC2 實例的終端機中執行：

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3.8-venv # 根據您的 Ubuntu 版本調整 venv 套件
mkdir number-iching-app
cd number-iching-app
python3 -m venv venv
source venv/bin/activate
pip install Flask gunicorn
```

### 4. 將專案檔案傳輸到 EC2 (Transfer Project Files to EC2)

在您的本機終端機中，從專案根目錄執行 `scp` 命令：

```bash
scp -i /path/to/your-key-pair.pem app.py calculator.py requirements.txt ubuntu@YOUR_EC2_PUBLIC_DNS_OR_IP:~/number-iching-app/
scp -r -i /path/to/your-key-pair.pem templates ubuntu@YOUR_EC2_PUBLIC_DNS_OR_IP:~/number-iching-app/
```

### 5. 在 EC2 上運行 Flask 應用程式 (Run Flask Application on EC2)

回到 EC2 實例的終端機，確保您在 `~/number-iching-app` 目錄中並已激活虛擬環境，然後運行 Gunicorn：

```bash
cd ~/number-iching-app
source venv/bin/activate
pip install -r requirements.txt # 確保所有依賴都已安裝
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app &
```

### 6. 安裝並配置 ngrok (Install and Configure ngrok)

在 EC2 實例的終端機中執行：

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
./ngrok authtoken YOUR_NGROK_AUTHTOKEN # 如果有 ngrok 帳戶，請替換為您的 authtoken
./ngrok http 5000
```

ngrok 會在終端機中顯示一個公共的 HTTPS URL。複製該 URL，您就可以在任何地方訪問您的網頁應用程式了。

## 技術棧 (Technologies Used)

*   **Backend:** Python, Flask, Gunicorn
*   **Frontend:** HTML, CSS, JavaScript
*   **Deployment:** AWS EC2, ngrok

## 注意事項 (Important Notes)

*   ngrok 的免費服務提供的 URL 是臨時的，當您關閉 ngrok 進程後就會失效。
*   完成演示後，請務必停止或終止您的 EC2 實例，以避免產生不必要的 AWS 費用。
