# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:18:34 2016

@author: maben
"""
'''
为物品简历“档案” item profiles
根据用户对物品的打分建立用户“档案” user profiles
推荐时，根据用户档案与物品档案之间的相似程度进行推荐
用之前的文档做例子，TF-IDF矩阵可以视为一个item profiles，
'''
from sklearn.preprocessing import normalize
from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc  

'''read data'''
filepath = 'E:/study/tianchi/IL/datasets'
ijcai2016_merchant_info = pd.read_csv(filepath+"/ijcai2016_merchant_info")
ijcai2016_koubei_test = pd.read_csv(filepath+"/ijcai2016_koubei_test")
ijcai2016_koubei_train = pd.read_csv(filepath+"/ijcai2016_koubei_train")

names = ['User_id','Seller_id','Item_id','Category_id','Online_Action_id','Time_Stamp']
ijcai2016_taobao = pd.read_csv(filepath+"/ijcai2016_taobao",names = names,chunksize=1000)
tot = pd.DataFrame([])
for piece in ijcai2016_taobao:
    print piece
    tot = tot.add(piece)
    
'''distance_user_category,user_id and category_id is a list
   click got score 1,buy got score 2
'''
def distance_user_category(user_id,category_id):
    distance_mat_user_category = pd.DataFrame([])
    distance_mat_user_category.reindex(columns = user_id,index = category_id,fill_value=0)

    
    