import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
drive.mount('/content/drive')

import os
import io

from google.colab import files
myfile1 = files.upload()

# pd.read_csv()로 csv파일 읽어들이기
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
df = pd.read_csv(io.BytesIO(myfile1['high_diamond_ranked_10min.csv']))

df.info()

df.describe()

# DataFrame의 corr() 메소드와 Seaborn의 heatmap() 메소드를 이용하여 Pearson's correlation 시각화하기
fig = plt.figure(figsize=(4, 10))
sns.heatmap(df.corr()[['blueWins']], annot = True)
plt.show()

df.columns

sns.histplot(x='blueGoldDiff', data = df, hue = 'blueWins', palette='RdBu', kde=True)
sns.histplot(x='blueKills', data=df, hue='blueWins', palette='RdBu', kde=True, bins =8)
sns.jointplot(x='blueKills', y='blueGoldDiff',data=df, hue='blueWins', palette='RdBu')
sns.jointplot(x='blueExperienceDiff', y='blueGoldDiff',data=df, hue='blueWins', palette='RdBu')
sns.countplot(x='blueDragons', data = df, hue ='blueWins', palette = 'RdBu')
sns.countplot(x='redDragons', data = df, hue ='blueWins', palette = 'RdBu')
sns.countplot(x='blueFirstBlood', data = df, hue = 'blueWins', palette ='RdBu')

from sklearn.preprocessing import StandardScaler

df.columns

df.drop(['gameId', 
       'redFirstBlood', 'redKills', 'redDeaths','redTotalGold','redTotalExperience',
       'redGoldDiff', 'redExperienceDiff'], axis = 1, inplace=True)

df.columns

X_num = df[['blueWardsPlaced', 'blueWardsDestroyed',
       'blueKills', 'blueDeaths', 'blueAssists', 'blueEliteMonsters',
       'blueTowersDestroyed', 'blueTotalGold',
       'blueAvgLevel', 'blueTotalExperience', 'blueTotalMinionsKilled',
       'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff',
       'blueCSPerMin', 'blueGoldPerMin', 'redWardsPlaced', 'redWardsDestroyed',
       'redAssists', 'redEliteMonsters', 
       'redTowersDestroyed', 'redAvgLevel', 'redTotalMinionsKilled',
       'redTotalJungleMinionsKilled', 'redCSPerMin', 'redGoldPerMin']]

X_cat = df[['blueFirstBlood','blueDragons', 'blueHeralds', 'redDragons', 'redHeralds']]

scaler = StandardScaler()
scaler.fit(X_num)
X_scaled = scaler.transform(X_num)
X_scaled = pd.DataFrame(X_scaled, index = X_num.index, columns=X_num.columns)

X = pd.concat([X_scaled, X_cat], axis = 1)
y = df['blueWins']

X

from sklearn.model_selection import train_test_split

# train_test_split() 함수로 학습 데이터와 테스트 데이터 분리하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1)

from sklearn.linear_model import LogisticRegression

# LogisticRegression 모델 생성/학습
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)

from sklearn.metrics import classification_report

# Predict를 수행하고 classification_report() 결과 출력하기
pred = model_lr.predict(X_test)
print(classification_report(y_test, pred))


# Logistic Regression 모델의 coef_ 속성을 plot하기
model_coef = pd.DataFrame(data=model_lr.coef_[0], index=X.columns, columns=['Model Coefficient'])
model_coef.sort_values(by='Model Coefficient', ascending=False, inplace= True)
plt.bar(model_coef.index, model_coef['Model Coefficient'])
plt.xticks(rotation=90)
plt.grid()
plt.show()

from google.colab import files
myfile2 = files.upload()

df2 = pd.read_csv(io.BytesIO(myfile2['Master_Ranked_Games.csv']))

df2.info()

df2.head()

df2.describe()

fig = plt.figure(figsize=(4, 10))
sns.heatmap(df2.corr()[['blueWins']], annot = True)
plt.show()

df.columns

sns.histplot(x='blueTowersDestroyed', data = df2, hue = 'blueWins', palette='RdBu', kde=True)

sns.countplot(x='blueBaronKills', data = df2, hue ='blueWins', palette = 'RdBu')

sns.jointplot(x='blueKills', y='blueDeaths',data=df2, hue='blueWins', palette='RdBu')

df2.columns

df2.drop(['gameId','redFirstBlood', 'redKills', 'redDeaths','redFirstTower', 'redDrangonFirstKill','redFirstInhibitor', 'redFirstBaron'], axis = 1, inplace =True)

df2.columns


X2_num = df2[['gameDuraton',
       'blueFirstBaron', 'blueDrangonFirstKill',
       'blueDragonKills', 'blueBaronKills', 'blueTowersDestroyed',
       'blueInhibitorKills', 'blueWardsPlaced', 'blueWardsDestroyed',
       'blueKills', 'blueDeaths', 'blueAssists', 'blueChampionDamageDealt',
       'blueTotalGold', 'blueTotalMinionsKilled', 'blueTotalLevel',
       'blueAvgLevel', 'blueTotalJungleMinionsKilled', 'blueKillingSpree',
       'blueTotalHeal', 'blueObjectDamageDealt',
       'redDragonKills',
       'redBaronKills', 'redTowersDestroyed', 'redInhibitorKills',
       'redWardsPlaced', 'redWardsDestroyed', 'redAssists',
       'redChampionDamageDealt', 'redTotalMinionsKilled', 'redTotalLevel',
       'redAvgLevel', 'redTotalJungleMinionsKilled', 'redKillingSpree',
       'redTotalHeal', 'redObjectDamageDealt']]

X2_cat = df2[['blueFirstBlood','blueFirstTower',
             'blueFirstTower',
             'blueDrangonFirstKill','blueFirstInhibitor', 'blueFirstBaron']]

scaler = StandardScaler()
scaler.fit(X2_num)
X2_scaled = scaler.transform(X2_num)
X2_scaled = pd.DataFrame(X2_scaled, index = X2_num.index, columns=X2_num.columns)

X2 = pd.concat([X2_scaled, X2_cat], axis = 1)
y2 = df2['blueWins']

X2

from sklearn.model_selection import train_test_split

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size = 0.3, random_state=10)

from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression(max_iter = 1000)
model_lr.fit(X2_train, y2_train)

from sklearn.metrics import classification_report

pred2 = model_lr.predict(X2_test)
print(classification_report(y2_test, pred2))

model_coef = pd.DataFrame(data=model_lr2.coef_[0], index=X2.columns, columns=['Model Coefficient'])
model_coef.sort_values(by='Model Coefficient', ascending=False, inplace= True)
plt.bar(model_coef.index, model_coef['Model Coefficient'])
plt.xticks(rotation=90)
plt.grid()
plt.show()

