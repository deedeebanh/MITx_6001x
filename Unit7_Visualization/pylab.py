#import matplotlib
#matplotlib.use('tkAgg')
import matplotlib.pyplot as plt
#import pylab as plt

mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(i**4)

plt.figure('lin quad')
plt.clf()
plt.plot(mySamples,myLinear,'b-',label='Linear')
plt.plot(mySamples,myQuadratic,'ro',label='Quadratic')
plt.legend(loc='upper left')
plt.show()
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples,myCubic,'g--',label='Cubic')
plt.plot(mySamples,myExponential,'r',label='Exponential')
plt.legend()
plt.show()

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples,myLinear,'b-',label='Linear',linewidth=2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples,myQuadratic,'ro',label='Quadratic',linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')
plt.show()

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0,14000)
plt.plot(mySamples,myCubic,'g--',label='Cubic',linewidth=4.0)
plt.subplot(122)
plt.ylim(0,14000)
plt.plot(mySamples,myExponential,'r',label='Exponential',linewidth=5.0)
plt.legend()
plt.title('Cubic vs Exponential')
plt.show()

plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples,myCubic,'g--',label='Cubic',linewidth=4.0)
plt.plot(mySamples,myExponential,'r',label='Exponential',linewidth=5.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs Exponential')
plt.show()
