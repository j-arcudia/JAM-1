import os
import numpy as np
#-------------------------------------
def is_number(s):
    try:
        float(s).is_integer()
        return True
    except ValueError:
        pass
#-------------------------------------
def get_a_int(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    if len(readline) == 2:
                        data0=readline[0].strip('\t\n\r') 
                        data1=readline[1].strip('\t\n\r')
                        if data0 == str(strchain):
                            if is_number(data1):
                                finalvalue=int(data1)
                                return finalvalue
                            else:
                                print('%s is not a number' %(strchain))
                                return False
        bilfile.close()
    print('%s is not specified.' %(strchain))
    return False
#-------------------------------------
def get_str_list(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    data0=readline[0].strip('\t\n\r') 
                    if data0 == str(strchain):
                        del readline[0]
                        data1=[str(item) for item in readline]
                        finalvalue=data1
        bilfile.close()
    return finalvalue
#-------------------------------------
def get_a_float(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    if len(readline) == 2:
                        data0=readline[0].strip('\t\n\r') 
                        data1=readline[1].strip('\t\n\r')
                        if data0 == str(strchain):
                            if is_number(data1):
                                finalvalue=float(data1)
                                return finalvalue
                            else:
                                print('%s is not a number' %(strchain))
                                return False
        bilfile.close()
    print('%s is not specified.' %(strchain))
    return False
#-------------------------------------
def split(word):
    return [char for char in word]
#-------------------------------------
def cambio_de_signo(a):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            if ichar[1] != '0':
                if ichar[0] == '+': a[i,j]='-'+ichar[1]
                if ichar[0] == '-': a[i,j]='+'+ichar[1]
    return a
#-------------------------------------
def ask_equivalents(a,b,option):
    b1=np.array([b[:,0],b[:,1],b[:,2]])
    b2=np.array([b[:,1],b[:,2],b[:,0]])
    b3=np.array([b[:,2],b[:,0],b[:,1]])
    b4=np.array([b[:,0],b[:,2],b[:,1]])
    b5=np.array([b[:,2],b[:,1],b[:,0]])
    b6=np.array([b[:,1],b[:,0],b[:,2]])
    b1=b1.transpose()
    b2=b2.transpose()
    b3=b3.transpose()
    b4=b4.transpose()
    b5=b5.transpose()
    b6=b6.transpose()
    for bi in [b1,b2,b3,b4,b5,b6]:
        if np.array_equal(a,bi): return True
    b1=np.flipud(b1)
    b2=np.flipud(b2)
    b3=np.flipud(b3)
    b4=np.flipud(b4)
    b5=np.flipud(b5)
    b6=np.flipud(b6)
    if option in [3,4,6]:
        b1=cambio_de_signo(b1)
        b2=cambio_de_signo(b2)
        b3=cambio_de_signo(b3)
        b4=cambio_de_signo(b4)
        b5=cambio_de_signo(b5)
        b6=cambio_de_signo(b6)
    for bi in [b1,b2,b3,b4,b5,b6]:
        if np.array_equal(a,bi): return True
    return False
#-------------------------------------
def cadenax(a):
    chain=''   
    for k in a[:,0]: chain=chain+k
    chain=chain+'/'
    for k in a[:,1]: chain=chain+k
    chain=chain+'/'
    for k in a[:,2]: chain=chain+k
    return chain
#-------------------------------------
def allatomsx(a,atom_list):
    cj,ck=0,0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            if   ichar[1] == 'j': cj=cj+1
            elif ichar[1] == 'k': ck=ck+1
    allatoms=list(zip(atom_list,[cj,ck]))
    return allatoms
#-------------------------------------
def poscardata(a,zdlist,zlattice,buckling):
    listaxyz=[]
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            signo,letra=ichar[0],ichar[1]
            if letra != '0':
                if j==0: xd,yd=0.0000000000,0.0000000000
                if j==1: xd,yd=0.3333333333,0.6666666667
                if j==2: xd,yd=0.6666666667,0.3333333333
                if signo=='-': zd=zdlist[i]-(buckling/zlattice)
                if signo=='+': zd=zdlist[i]+(buckling/zlattice)
                if   letra == 'j': zi=0
                elif letra == 'k': zi=1
                listaxyz.append([xd, yd, zd, zi])
    listaxdydzd = sorted(listaxyz, key=lambda x: int(x[3]))
    return listaxdydzd
#-------------------------------------
def build_poscarx(a,inamex,filename,z_vacuum,num_layers,d,latticep,atom_list,buckling):
    zlattice=(z_vacuum+float(num_layers-1)*d)
    zmax = (zlattice+float(num_layers-1)*d)/2.0
    zdlist=[]
    for ii in range(num_layers):
        zc=zmax-float(ii)*d
        zd=zc/zlattice
        zdlist.append(zd)
    fopen = open(filename,'w')
    print("%s" %(inamex), file=fopen)
    print("%f" %(latticep), file=fopen)
    print("0.500000000  -0.866025403  0.000000000", file=fopen)
    print("0.500000000   0.866025403  0.000000000", file=fopen)
    print("0.000000000   0.000000000  %11.9f" %(zlattice/latticep), file=fopen)
    allatoms=allatomsx(a,atom_list)
    print(' '.join([str(item[0]) for item in allatoms]), file=fopen)
    print(' '.join([str(item[1]) for item in allatoms]), file=fopen)
    print("Direct", file=fopen)
    listaxyz=poscardata(a,zdlist,zlattice,buckling)
    for ixyz in listaxyz:
        xd, yd, zd, si=ixyz[0],ixyz[1],ixyz[2],atom_list[ixyz[3]]
        print("%12.10f %12.10f %12.10f !%s" %(xd, yd, zd, si), file=fopen)
    fopen.close()
#-------------------------------------
