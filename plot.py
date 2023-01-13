import numpy as np
import matplotlib.pyplot as plt

# x =  np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)
# y1 = np.cos(x)
# y2 = np.tan(x)

# # print(x)
# # print(y)
# # print(y1)
# # print(y2)
# plt.subplot(2,1,1)
# plt.plot(x, y)

# plt.subplot(2,1,2)
# plt.plot(x,y1)
# # plt.plot(x, y2)

# plt.xlabel('X axis label')
# plt.ylabel('y axis label')
# plt.title('sine and cosine')
# plt.legend({'sine','cosine'})
# plt.show()
# print('I am here')

x = np.linspace(-20,20,100)
def fun(x):
    y=[]
    for ele in x:
        # result = ele**2
        # result = 5*(ele**2) + 4*ele
        result = 1 -(ele**2)/2
        y.append(result)
    return y
y = fun(x)
plt.plot(x, y)
plt.show()