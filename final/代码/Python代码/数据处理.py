import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.ticker import FuncFormatter

import math
import seaborn as sns
import tsfresh as tsf

train_path = "../data/train.csv"

# 设置字体
plt.rcParams['font.sans-serif'] = 'Songti SC'
plt.rcParams['axes.unicode_minus'] = False
import warnings
warnings.filterwarnings('ignore')

Data = pd.read_csv(train_path, encoding = 'gbk')
Data = Data.drop_duplicates(keep = 'first')
Data.to_csv('Data_drop_duplicates.csv', index = None)

#导入已经去重后的数据
Data = pd.read_csv('Data_drop_duplicates.csv')
#查看数据前五行
Data.head()
#查看缺失数据
Data.isnull().sum()
#删除缺失数据
Data.dropna(axis=0, how='any',inplace=True)
#提取月、日、时
Data['Month'] = Data['日期'].apply(lambda x: (int(x.split('/')[-2]) if ((x[-3]=='/')|(x[-2]=='/')) else int(x.split('-')[-2])))
Data['Day'] = Data['日期'].apply(lambda x: int(x.split('/')[-1][-2:]))
Data['Hour'] = Data['时间'].apply(lambda x: int(x.split(':')[0]))
Data.drop(['日期','时间'],axis = 1,inplace=True)
#将月、日、时按时间顺序进行排序
Data.sort_values(['ID','Month','Day','Hour'],inplace=True)
Data.reset_index(drop=True,inplace=True)
#提取小区编号列表
ID_list = sorted(list(set(Data.ID)))
#计算小区编号列表长度
print(len(ID_list))
#提取需要删除的索引
ID_index=[]
for Id in ID_list:
    if len(Data.loc[Data['ID']==Id]) < 720:
        t1 = Data.loc[Data.ID == Id].index.tolist()
        ID_index.extend(t1)
#计算需要删除的索引的长度
len(ID_index)
#删除无关数据
Data.drop(index = ID_index, inplace = True)
#将索引进行重排
Data.reset_index(drop = True, inplace = True)
#保存文件到本地
Data.to_csv('Data_final.csv',index=None)










#导入数据
Data = pd.read_csv('Data_final.csv')

ID_list = sorted(list(set(Data.ID)))
ID_list = ID_list[:-1000:1000]

#提取样本标准差 SD(Standard Deviation)
ses_list = []
for Id in ID_list:
    df1 = Data.loc[Data.ID==Id]
    t1_d = df1.DOWN
    tm_d = df1.DOWN.mean()
    t1_u = df1.UP
    tm_u = df1.UP.mean()
    tu = math.sqrt(sum(((t1_u-tm_u)**2))/(len(df1)-1))
    td = math.sqrt(sum(((t1_d-tm_d)**2))/(len(df1)-1))
    ses_list.append([Id,tu,td])
df_data = pd.DataFrame(ses_list, columns=['ID','std_up','std_down'])

#提取变化趋势系数 CT(Change Trend)
ses_list = []
for Id in ID_list:
    df1 = Data.loc[Data.ID==Id]
    length = len(df1)
    
    yu = np.log(df1.UP.tolist())
    xu = np.log([i+1 for i in range(length)])
    bu = ((xu*yu).mean() - xu.mean()*yu.mean())/((xu**2).mean()-(xu.mean())**2)
    
    yd = np.log(df1.DOWN.tolist())
    xd = np.log([i+1 for i in range(length)])
    bd = ((xd*yd).mean() - xd.mean()*yd.mean())/((xd**2).mean()-(xd.mean())**2)
    ses_list.append([bu,bd])
df_data[['CT_up','CT_down']] = ses_list

#提取超均值占比 LR(Limit Radio)
ses_list = []
for Id in ID_list:
    df1 = Data.loc[Data.ID==Id]
    
    t1u = df1['UP'].quantile(0.25)
    t3u = df1['UP'].quantile(0.75)
    IQRu = t3u - t1u
    tu = len((df1['UP']<(df1.loc[df1.UP<(t1u-1.5*IQRu)])))+len((df1.loc[df1.UP>(t1u+1.5*IQRu)]))
    tu = tu/len(df1)
    
    t1d = df1['DOWN'].quantile(0.25)
    t3d = df1['DOWN'].quantile(0.75)
    IQRd = t3d - t1d
    td = len((df1['DOWN']<(df1.loc[df1.DOWN<(t1d-1.5*IQRd)])))+len((df1.loc[df1.DOWN>(t1d+1.5*IQRd)]))
    td = td/len(df1)
    
    ses_list.append([tu,td])
df_data[['LR_up','LR_down']] = ses_list

#提取一阶差分绝对值和 DS(Difference Sum)
ses_list = []
for Id in ID_list:
    df1 = Data.loc[Data.ID==Id]
    tsu = df1.UP
    tsd = df1.DOWN
    tu = tsf.feature_extraction.feature_calculators.absolute_sum_of_changes(tsu)
    td = tsf.feature_extraction.feature_calculators.absolute_sum_of_changes(tsd)
    ses_list.append([tu,td])
df_data[['DS_up','DS_down']] = ses_list

#提取流量普及率 PR(Popularity Radio)  
ses_list = []
tmaxu = 407.46858617609195
tminu = 1.2299478095153273
tmaxd = 3459.3380758666917
tmind = 7.8084020133992340
for Id in ID_list:
    
    df1 = Data.loc[Data.ID==Id]
    t1u = df1.UP.sum()*24*50/(len(df1.UP))
    tu = (t1u - tminu)/(tmaxu-tminu)
    
    df1 = Data.loc[Data.ID==Id]
    t1d = df1.DOWN.sum()*24*50/(len(df1.DOWN))
    td = (t1d - tmind)/(tmaxd-tmind)
    ses_list.append([tu,td])
df_data[['PR_up','PR_down']] = ses_list















#导入数据
Data = pd.read_csv('final_10.csv', encoding = 'utf-8')

def IDD(a,d):
    y79 = Data.loc[Data.ID == a].DOWN[:24*2+d+1-5]
    x = range(len(y79)-d-1)
    VPTmaxlist = []
    VPTminlist = []
    y1 = []
    
    for i in range(len(x)):
        y = y79[i:i+d]
        y_mean = y.mean()
        y_std = y.std()
        b = y_std/y_mean
        VPTmax = list(y79)[i+d] + b*y_std#*1.5
        VPTmaxlist.append(VPTmax)
        VPTmin = list(y79)[i+d] - b*y_std-0.05#*1.5
        VPTminlist.append(VPTmin)

        y1.append(list(y79)[i+d-1])

        if (list(y79)[i+d+1] > VPTmax):
            pass
            #print('开')
        elif (list(y79)[i+d+1] < VPTmin):
            pass
            #print('关')
        else:
            pass
            #print('好')
    plt.figure(figsize=(16/2,9/2),dpi=130)
    
    x_major_locator=MultipleLocator(1)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.grid()  
    plt.plot(VPTmaxlist[24-d:],'--',linewidth=1,alpha=0.9,label='$H_Q$')
    plt.plot(VPTminlist[24-d:],'--',linewidth=1,alpha=0.9,label='$L_Q$')
    plt.xlabel('小时',size=12) 
    plt.ylabel('流量',size=12)
    plt.xlim(0,23)
    plt.plot(y1[24-d:],linewidth=1.2,alpha=1,label='$Q_{t_n}$')
    plt.legend(loc = 'best')
    plt.savefig('指标图',dpi=600)
    y2 = VPTmaxlist[24-d:]
    e = 1 - (sum(y2))/(max(y2)*len(y2))
    print(e)

plt.figure(figsize=(16/2,7/2),dpi=300)
elist = [0.48,0.58,0.6024,0.57,0.51,0.47]
ex = [4,5,6,7,8,9]
#plt.grid()

plt.ylabel('滑动窗口长度',size=15)
#plt.xlabel('节能效率',size=15)
def to_percent(temp, position):
  return '%1.0f'%(100*temp) + '%'
#plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

#plt.plot(ex,elist,'r--')
plt.barh(ex,elist,alpha=0.9)
plt.savefig('D:/竞赛/mathorcup复赛/final5.0/Image/节能效率2',dpi=600)

plt.figure(figsize=(16,9))
begin = 1
for i in range(24):
    
    y = Data.loc[Data.ID == idlist[begin+i]].DOWN
    y = y[:180]
    ax = plt.subplot(6,4,i+1)
    ax.plot(y)

plt.figure(figsize=(16/2,9/2),dpi=130)
plt.grid()
plt.plot(ABdata.A,linewidth=1,alpha=0.9,label='原始流量数据')
plt.plot(ABdata.C,linewidth=1,alpha=0.9,label='滤波后流量数据')
plt.xlabel('小时',size=12) 
plt.ylabel('流量',size=12)
plt.legend(loc = 'best')
plt.savefig('AB1',dpi=600)