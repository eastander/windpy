from WindPy import *
w.start()
import pandas as pd
 
assetList = ["000300.SH"]
startDate = "2012-01-02"
endDate = "2013-01-02"
dataImport = w.wsd(assetList, "close,amt,pct_chg,turn,trade_status,val_pe_deducted_ttm,ps_ttm,pcf_ocf_ttm,dividendyield2,pe_est,ev2_to_ebitda,mkt_cap_CSRC,or_ttm,roe_ttm2,roic2_ttm,roic_ttm2,netprofitmargin_ttm2", "2017-01-01", "2019-03-10", "year=2018;unit=1;Period=Q;PriceAdj=F")



dates = pd.to_datetime(dataImport.Times)
#time series data, 日期作为后面df的index
#作为index时，日期格式统一一下
#错误：df = pd.DataFrame(dataImport.Data, index = dates.strftime("%Y-%m-%d"), columns = assetList)
#生成一个收盘价格的时间序列表格，行名称是日期，列名称是股票代码
#dataImport.data的表达方式：列是日期，资产是行，所以需要转置。要么在转置之后加上index和column。
#要么在加上index和column之后再转置，但加的时候跟上面的不一样。
 
#方法一：
df = pd.DataFrame(dataImport.Data).T
df.index = dates.strftime("%Y-%m-%d")
df.columns = assetList
 
df.to_excel('C:\Users\u1\Desktop\数据函数使用案例', encoding= 'uts-8', index = False, header = false)
