import numpy as np

li=[0,1,2,3,4,5,6,7,8]

#changing list into array
a=np.array(li).reshape(3,3)
print(a)

cd=list()

cd.append(a.mean(axis=0).tolist())
#axis = 0 means along the rows
cd.append(a.mean(axis=1).tolist())
#axis = 1  means along the column
cd.append(a.mean())

dic={}

dic['mean']=cd #this holds mean of axis=0 and axis=1 and overall mean of the array
cd=list()

cd.append(a.var(axis=0).tolist())

cd.append(a.var(axis=1).tolist())

cd.append(a.var())

dic['variance']=cd

print(dic)
print('\n')
cd=list()

cd.append(a.std(axis=0).tolist())

cd.append(a.std(axis=1).tolist())

cd.append(a.std())

dic['standard deviation']=cd

print(dic)
print('\n')
cd=list()

cd.append(a.max(axis=0).tolist())

cd.append(a.max(axis=1).tolist())

cd.append(a.max())


dic['max']=cd

print(dic)
print('\n')
cd=list()

cd.append(a.min(axis=0).tolist())

cd.append(a.min(axis=1).tolist())

cd.append(a.min())



dic['min']=cd

cd=list()

cd.append(a.sum(axis=0).tolist())

cd.append(a.sum(axis=1).tolist())

cd.append(a.sum())

dic['sum']=cd

print(dic)
print('\n')
