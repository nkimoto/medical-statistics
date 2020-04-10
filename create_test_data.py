from tqdm import tqdm
import numpy as np
import random
import pandas as pd
from datetime import datetime, timedelta


START_DATE = datetime.strptime("20140401", '%Y%m%d')
END_DATE = datetime.strptime("20190507", '%Y%m%d')

def generate_random_date(st_date, ed_date):
    diff = (ed_date - st_date).days + 1
    mid_date = st_date + timedelta(diff * np.random.rand())
    mid_date = mid_date.strftime('%Y%m%d')
    return mid_date

def create_sample_data(N, seed):    
    test_df = pd.DataFrame(columns=["iid", "medica_type", "person_type", "visits_day", "sex", "age",
                                    "hi", "bw", "bmi", "ac", "tg", "ldl", "hdl", "ave_DBP", "ave_SBP",
                                    "bg", "a1c", "cre", "eGFR", "n_of_null"])
    
    for i in tqdm(range(N), desc='Progress'):
        medical_type = 10
        
        # iid = ""
        iid = str(random.randint(1000000000000000, 9999999999999999))
        
        # person_type: 二項分布
        person_type = np.random.binomial(n=1, p=0.72)
        
        seed += 1
        np.random.seed(seed)
        
        # visits_day : 来訪日 20140401-20190507から一様分布を足して生成
        visits_day = generate_random_date(START_DATE, END_DATE)
        seed += 1
        np.random.seed(seed)
        
        # sex: 性別 1 or 2 二項分布
        sex = 1 + np.random.binomial(n=1, p=0.36)
        seed += 1
        np.random.seed(seed)
        
        # age: 年齢 15-75 正規分布
        age = int(np.random.normal(47, 8.35)) 
        seed += 1
        np.random.seed(seed)
        
        # hi: 身長 
        hi = 54.5 + np.random.uniform(72.1 - 54.5)
        # bw: 体重    
        bw = 159.5 + np.random.uniform(171.9 - 159.5)
        # bmi: BMI
        bmi = 20.7 + np.random.uniform(25.2 - 20.7)
        # ac: 腹囲    
        ac = 76 + np.random.uniform(87.1 - 76)
        tg = 61 + np.random.uniform(131 - 61)
        ldl = 101 + np.random.uniform(141 - 101)
        hdl =  52 + np.random.uniform(75 - 52)
        ave_DBP = 61 + np.random.uniform(84 - 68)
        ave_SBP = 68 + np.random.uniform(133 - 112)
        bg = 87 + np.random.uniform(102 - 87)
        a1c = 5.3 + np.random.uniform(5.74 - 5.3)
        cre = 0.69 + np.random.uniform(1 - 0.69)
        eGFR = 61.37 + np.random.uniform(83.54 - 61.37)
        n_of_null = np.random.binomial(n=0, p=0.99998)
        new_row = pd.Series([iid, medical_type, person_type, visits_day, sex, age, hi, bw, bmi, ac, tg, ldl, hdl, ave_DBP, ave_SBP, bg, a1c, cre, eGFR, n_of_null], index=test_df.columns)
        test_df = test_df.append(new_row,  ignore_index=True)
    test_df.to_csv('./data/test_df.csv')

if __name__ == "__main__":
    create_sample_data(1000, 0)
