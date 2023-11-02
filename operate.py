# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

import time               
import module as m 
import IFTTT_info

if __name__ == '__main__':
    
    slist = m.get_setting()   #
    cnt = len(slist)

    
    log1 = []   # 記錄曾經傳送過的股票高或低於期望價的訊息, 避免重複傳送
    log2 = []   # 記錄曾經傳送過符合四大買賣點的訊息, 避免重複傳送

    for i in range(cnt):   #}
        log1.append('')    #} 為每支股票加入一個對應的元素
        log2.append('')    #}
    
    
    
    check_cnt = 5
    
    for j in range(check_cnt):
        
        first_time_cnt = 1  # 只有第一次print出時間
        
        for i in range(cnt):
            
            
            id, low, high = slist[i]  
            name, price, real_time = m.get_price(id) 
            
            if first_time_cnt == 1:
                first_time_cnt = 0
                print(f'時間： {real_time}')
            
            print('股票：',name, '股價：',price, '區間：',low,'~',high)
            
            
            
            name_price = f'{name} ${price}'
            # 根據txt內的區間範圍買賣
            if price <= low:      
                if log1[i] != '買進': 
                    
                    m.send_ifttt(real_time, name_price, '買進 (股價低於 '+ str(low)+')')
                    log1[i]= '買進'   
            elif price >= high:  
                if log1[i] != '賣出':
                    m.send_ifttt(real_time, name_price, '賣出 (股價高於 '+ str(high)+')')
                    log1[i]= '賣出'  
                    
            
            # 買賣策略邏輯
            # 檢查是否符合四大買賣點
            act, reason = m.get_best(id) 
            
            if reason:   
                if log2[i] != reason: 
                    m.send_ifttt(real_time, name_price, act + ' (' + reason + ')')
                    log2[i] = reason    
                    
                    
        print('--------------')
        
        time.sleep(60)            
      
        

