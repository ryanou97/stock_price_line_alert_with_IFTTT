# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

import time               
import module as m 
import IFTTT_info


trigger_func_name = IFTTT_info.trigger_func_name
key = IFTTT_info.ifttt_key
file_path = IFTTT_info.file_path + '\\stock.txt'

    

if __name__ == '__main__':
    
    print(file_path)
    slist = m.get_setting()   #
    cnt = len(slist)

    
    log1 = []
    log2 = []  
    for i in range(cnt):   #}
        log1.append('')    #} 為每支股票加入一個對應的元素
        log2.append('')    #}
    
    check_cnt = 20 
    
    
    while True:
        for i in range(cnt):
            id, low, high = slist[i]  
            name, price = m.get_price(id) 
            print('檢查：',name, '股價：',price, '區間：',low,'~',high)
            if price <= low:      
                if log1[i] != '買進': 
                    m.send_ifttt(name, price, '買進 (股價低於 '+str(low)+')')
                    log1[i]= '買進'   
            elif price >= high:  
                if log1[i] != '賣出':
                    m.send_ifttt(name, price, '賣出 (股價高於 '+str(high)+')')
                    log1[i]= '賣出'  
            act, why = m.get_best(id) 
            if why:   
                if log2[i] != why: 
                    m.send_ifttt(name, price, act + ' (' +why+ ')')
                    log2[i] = why    
                    
        print('--------------')
        check_cnt -= 1
        if check_cnt == 0: break   
        time.sleep(180)            
        

