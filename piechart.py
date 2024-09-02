import numpy as np
import matplotlib.pyplot as plt
data={'java':22.2,'python':17.6,'PHP':8.8,'javascript':8,'c#':7.7,'c++':6.7}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
exp=[0.1,0,0,0,0,0]
plt.pie(values,labels=courses,explode=exp,shadow=True)
plt.show()
