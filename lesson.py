import numpy as np
x = np.array([1,2,3])
y = np.array([2,3.9,6.1])

## データの中心化
# 平均の算出
x.mean()
y.mean()

xc = x - x.mean()
yc = y - y.mean()

print(xc)
print(yc)

## パラメータaの計算
# 要素ごとの掛け算（要素積）
xx = xc * xc

print(xx)

xy = xc * yc
print(xy)

xxs = xx.sum()
xys = xy.sum()

print(xxs,xys)

a = xy.sum()/xx.sum()
print(a)


