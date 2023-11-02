# stock_price_line_alert_with_IFTTT
 # 台股股價監控系統

這個項目包含了兩支Python程式，用於監控台股股價並夠過Line發送通知。
module.py用於的function，operate.py作為主要操作程式。

## 文件結構
operate.py: 主要的程式入口，負責設定、操作和執行監控。
module.py: 包含讀取股價紀錄、取得即時報價、買賣策略、發送至IFTTT推播到line Notify的函數和邏輯。
IFTTT_info.py: 包含IFTTT的相關設定信息，此為個人資訊需自行創建。
stock_.txt: 包含要監控的台股代號和相關的買進位置和賣出位置。

## 如何使用

1. 需先安奘以下兩個Python庫：

```shell
pip install twstock, requests

2.至[IFTTT]("https://ifttt.com")申請帳號，使用其webhooks服務

3. 於stock_.txt內紀錄需要關注的股票代號，期望的買賣出位置

4. 執行operate.py



