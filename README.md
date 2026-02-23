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
