import matplotlib.pyplot as plt
with open("values.txt") as f:
    data = f.read().split('\n')
    x = [float(row.split(',')[0]) for row in data]
    y = [float(row.split(',')[1]) for row in data]
    
plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('graph')
plt.show()
