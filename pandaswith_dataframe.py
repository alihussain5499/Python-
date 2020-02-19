import pandas as pd
pd.DataFrame()
pd.DataFrame(data=[1,2,3])

pd.DataFrame(data=[1,2,3,4,5,6])

pd.DataFrame(data=[1,2,3],index=["ab","bc","cd"])

pd.DataFrame(data=[1,2,3],index=["ab","bc","cd"],columns=["marks"])

pd.DataFrame(data=[1,2,3],index=["ab","bc","cd"],columns=["marks"],dtype='float')

pd.DataFrame(data=[1,2,3],index=["ab","bc","cd"],columns=["marks"],dtype='float',copy=4)

#creating array with dictionary#
d1={"ali":10,"sap":30,"bad":40,"boy":50}
pd.DataFrame(data=d1,index=["0","marks","4","n"])

d1={"ali":60,"sap":30,"bad":40,"boy":"null"}
pd.DataFrame(data=d1,index=["0","marks","4","n"])

