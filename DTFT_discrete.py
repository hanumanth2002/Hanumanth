import matplotlib.pyplot as plt
import numpy as np

w=np.arange(-np.pi,np.pi,0.01*np.pi);

x=[2,3,4,56,8]
y=[]
j=(-1)**0.5
for i in w:
	sum1=0
	for n in range (0,len(x)):
		sum1=sum1+x[n]*np.exp(-1*j*i*n)
	y.append(sum1)
plt.subplot(211);
plt.stem(w,np.abs(y));
plt.subplot(212);
plt.stem(w,np.angle(y));
plt.show()
print(y)
