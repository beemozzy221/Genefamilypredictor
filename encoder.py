import numpy as np;
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def encoder(arr1):

    enc = OneHotEncoder(handle_unknown='ignore')
    arr2 = np.array([["A"],["G"],["T"],["C"]])
    enc.fit(arr2)

    x = np.zeros(shape=(len(arr1),len(arr1[0]),4))

    for i in range (len(arr1)):
        for j in range(len(arr1[i])):
            x[i,j]=enc.transform([[arr1[i,j]]]).toarray();
         
    
    return x

def encodery(arr2):
    enc = OneHotEncoder(handle_unknown='ignore')
    arr2=arr2.reshape(-1,1)
    enc.fit(arr2)
    arr2=enc.transform(arr2).toarray()
    return arr2

def encoderytest(arr2):
    enc = OneHotEncoder(handle_unknown='ignore')
    arr2=arr2.reshape(-1,1)
    enc.fit(arr2)
    arr2=enc.transform(arr2).toarray()
    print(enc.inverse_transform(arr2))
    return arr2
    
             

