from sklearn.datasets import load_iris
import pandas as pd
from sklearn import svm
import plotly.express as px

# 데이터 불러오기
iris = load_iris()

# DataFrame 생성
df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

# 품종 이름 추가
df["species"] = iris.target_names[iris.target]

print(df.head())

# SVM 모델 생성
s = svm.SVC(gamma=0.1, C=10)

# 학습
s.fit(iris.data, iris.target)

# 새로운 데이터
new_d = [
    [6.4, 3.2, 6.0, 2.5],
    [7.1, 3.1, 4.7, 1.35]
]

# 예측
res = s.predict(new_d)

print("새로운 2개 샘플의 부류는", res)

for i in res:
    print(iris.target_names[i])

# 3차원 산점도
fig = px.scatter_3d(
    df,
    x="sepal_length",
    y="sepal_width",
    z="petal_width",
    color="species"
)

fig.show(renderer="browser")