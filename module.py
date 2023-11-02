# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

import twstock
import requests
import IFTTT_info


# 讀取檔案 [台股代號、買進位置、賣出位置]
def get_setting(): 
    
    
    file_path = IFTTT_info.file_path + '\\stock_.txt'
    
    try:
        with open(file_path) as f:  
            slist = f.readlines()     
            print('讀入：', slist)
            res = []
            for lst in slist:
                s = lst.split(',')
                res.append([s[0], float(s[1]), float(s[2])])
                
    except:
        print('stock.txt 讀取錯誤')
        return None

    return res



def get_price(stockid):  
    rt = twstock.realtime.get(stockid)   
    if rt['success']:
        try:                    
            
            return (rt['info']['name'],    
                float(rt['realtime']['latest_trade_price']), str(rt['info']['time']))
        
        except:
            print("可能正在集合競價或報價出了點問題，稍後嘗試")   # 有遇過收盤前讀不到報價
    else:
        return (False, False)


# 檢查是否符合四大買賣點
def get_best(stockid):   
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    
    if(bp):
        return ('買進' if bp[0] else '賣出', bp[1])  
    else:
        return (False, False)  



def send_ifttt(v1, v2, v3):   
    trigger_func_name = IFTTT_info.trigger_func_name
    key = IFTTT_info.ifttt_key
    
    url = ('https://maker.ifttt.com/trigger/' +
           trigger_func_name +
           '/with/key/' +
           key +
          '?value1='+str(v1) +
          '&value2='+str(v2) +
          '&value3='+str(v3))
    
    r = requests.get(url)      
    if r.text[:5] == 'Congra':  
        print('sent (' +str(v1)+', '+str(v2)+', '+str(v3)+ ') to Line')
    return r.text



