from sklearn.preprocessing import OneHotEncoder
import numpy as np
import neualnets
import filereader as fr

number_of_samples=15;
number_of_nucleotides=560;
no_of_g_fam=4;

x = np.zeros((number_of_samples,number_of_nucleotides,4))
y = np.zeros([number_of_samples],dtype='object')
x_test = np.zeros((number_of_samples,number_of_nucleotides,4))

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\CytoArab.txt",x,y,"Cyto");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\CytoFruit.txt",x,y,"Cyto");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\CytoHuman.txt",x,y,"Cyto");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\CytoMus.txt",x,y,"Cyto");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\GGFArab.txt",x,y,"GGF");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\GGFFruit.txt",x,y,"GGF");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\GGFHuman.txt",x,y,"GGF");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\GGFMus.txt",x,y,"GGF");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HomeoArab.txt",x,y,"Homeo");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HomeoFruit.txt",x,y,"Homeo");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HomeoHuman.txt",x,y,"Homeo");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HSPArab.txt",x,y,"HSP");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HSPFruit.txt",x,y,"HSP");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HSPHuman.txt",x,y,"HSP");

x,y=fr.x_ybuilder(r"C:\Users\user\dafiles\HSPMus.txt",x,y,"HSP");

x_test=fr.x_tester(r"C:\Users\user\dafiles\HomeoNema.txt",x_test)

neualnets.neural_nets(x,y,no_of_g_fam,x_test);
