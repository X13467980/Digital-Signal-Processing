import numpy as np

x = np.array([[5,2,-4,1,-2,1]]).T # 入力信号
h = np.array([[0.6,-0.5,0.4,-0.2]]).T # インパルス応答
print("x=\n",x)
print("\nh=\n",h)

N = x.shape[0]
K = h.shape[0]
X = np.zeros([N,K]) # 行列Xの初期化

'''
この部分は自力で完成してください。
ヒント：行列Xの要素X(n,k)の一般的表現をよく観察すること


'''

y = np.matmul(X,h) # 行列の乗算で畳み込み演算
print("\ny=\n",y)