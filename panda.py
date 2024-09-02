import pandas as pd
x=[1,2,3,4,5]
b=pd.Series(x)
print(b)


import pandas as pd
x={1:"apple",2:"grape",3:"banana"}
b=pd.Series(x)
print(b)


import pandas as pd
x={1:"apple",2:"grape",3:"banana"}
b=pd.Series(x)
print(b)


import pandas as pd
x={1:"apple",2:"grape",3:"banana"}
b=pd.Series(x)
print(b)
y=pd.Series(x[2])
print(y)


import pandas as pd
x={1:"apple",2:"grape",3:"banana"}
b=pd.Series(x)
print(b)
y=pd.Series(x[2])
print(y)


import pandas as pd
data={"x":[1,2,3,4,5],"y":[6,7,8,9,10]}
pd.DataFrame(data)


import pandas as pd
x=pd.read_csv('submission.csv')
x.to_string()


