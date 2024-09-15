import numpy as np;
import encoder as en;


def x_ybuilder(filename,x,y,gene_fam_name):
    
    with open(filename, 'r') as f:
        text = f.read()

    arr = [c for c in text];

    arr1 = np.array([arr]);

    arr2 = en.encoder(arr1);
    

    for i in range (len(x)):
        if(x[i].any()!=1):
            x[i]=arr2;
            y[i]=gene_fam_name;
            break;
            
    return x,y

def x_tester(filename,x):
    
    with open(filename, 'r') as f:
        text = f.read()

    arr = [c for c in text];

    arr1 = np.array([arr]);

    arr2 = en.encoder(arr1);
            
    return x 
