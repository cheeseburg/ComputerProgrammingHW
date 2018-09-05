
import copy
def STRINGTOSTANDARD(a):
    a=a.replace('[','[[')
    a=a.replace(']',']]')
    a=a.replace(';','],[')
    a=eval(a)
    return a

	
def STRINGTOSPARSE(a):
    a=a.replace('{',"',")
    a=a.replace('(','[')
    a=a.replace(')',']')
    a=a.replace('}',']')
    a="['"+a
    a=eval(a)
    return a

	
def Str2Mat(a):

    if a[0]=='[':
        return(STRINGTOSTANDARD(a))
    else:
        return(STRINGTOSPARSE(a))

		
def IsStandard(A):
    if type(A[0])==list:
        return True
    else:
        return False


def STANDARDTOSTRING(A):
    A=str(A)
    A=A.replace('[[','[')
    A=A.replace(']]',']')
    A=A.replace('], [',';')
    A=A.replace(', ',',')
    A=A.replace(',(',',')
    A=A.replace(';(',';')
    A=A.replace(');',';')
    A=A.replace(')','')
    return A


def SPARSETOSTRING(A):
    A=str(A)
    if 'j' in A:
        A=A.replace('[','(')
        A=A.replace(', ',',')
        A=A.replace("',",'*')
        A=A.replace(')]',')')
        A=A.replace('),(','#')
        A=A.replace(',(',',')
        A=A.replace('#','),(')
        A=A.replace(')]',')}')
        A=A.replace('*','{')
        A=A.replace("['",'{')
    else:
        pass
    if A[6] ==']':
        A=A.replace("['",'')
        A=A.replace("']",'{}')
    else:
        A=A.replace("[",'(')
        A=A.replace(']',')')
        A=A.replace(', ',',')
        A=A.replace("',",'{')
        A=A.replace('))',')}')
        A=A.replace("('",'')
    return A


def Standard2Sparse(A):
    L=[]
    if A==[[]]:
        L=['0-0']
    else:
        i=1
        while i <= len(A):
            for j in A:
                b=0
                for n in range(1,len(j)+1):
                    b=b+1
                    if j[n-1] != 0:
                        L.append([i,b,j[n-1]])
                i=i+1
        m=len(A)
        m=str(m)
        n='-'
        k=len(j)
        k=str(k)
        q=m+n+k
        q=[q]
        L=q+L
    return(L)


def Mat2StrSparse(A):
    if type(A[0])==list:
        return SPARSETOSTRING(Standard2Sparse(A))
    else:
        return SPARSETOSTRING(A)


def BlankMatStr4Standard(a):
    for j in a:
        if type(j[0]) == str:
            p=int(j[0])
        if type(j[2]) ==str:
            q=int(j[2])
    s='[]'
    s=s+(p-1)*',[]'
    return s


def TransStr2Mat(s):
    s=s.replace('[','[[')
    s=s.replace(',[[',',[')
    s=s.replace(']',']]')
    s=s.replace(']],','],')
    s=eval(s)
    return s


def Sparse2Standard(A):
    if A==[]:
        lee=[]
    else:
        lib=''
        boo=''
        num=-1
        lee=TransStr2Mat(BlankMatStr4Standard(A))
        for i in A:
            if type(i)==str:
                q=int(i[0])
                Q=int(i[2])
            if type(i)==list:
                b=str(i[0])
                lib=lib+b
        for n in range(1,q+1):
            boo=lib.count(str(n))
            num=num+1
            if boo != 0:
                lee[num]=lee[num]+[(Q-boo)*'0,']
                lee=str(lee)
                lee=lee.replace("['",'[')
                lee=lee.replace(",']",']')
                lee=eval(lee)
                for i in A:
                    if type(i)==list:
                        if i[0] == n:
                            val=i[2]
                            col=i[1]-1
                            c=lee[num]
                            c=c.insert(col,val)
            else:
                lee[num]=[Q*'0,']
                lee=str(lee)
                lee=lee.replace("['",'[')
                lee=lee.replace(",']",']')
                lee=eval(lee)
    return(lee)



def Mat2StrStandard(a):
    if a==[[]]:
        return '[]'
    else:
        if IsStandard(a)==True:
            return STANDARDTOSTRING(a)
        else:
            b=Sparse2Standard(a)
            return STANDARDTOSTRING(b)
	

def Mat2StrSparse(a):
    if a==[[]]:
        return '0-0{}'
    else:
        if IsStandard(a)==True:
            b=Standard2Sparse(a)
            return SPARSETOSTRING(b)
        else:
            return SPARSETOSTRING(a)

    
def MatAdd(a,b):
    n1=-1
    if IsStandard(a) == True:
        P=copy.deepcopy(a)
    else:
        P=Sparse2Standard(a)
    if IsStandard(b)==True:
        Q=copy.deepcopy(b)
    else:
        Q=Sparse2Standard(b)
    for i in P:
        n1=n1+1
        M=Q[n1]
        n2=-1
        for j in i:
            n2=n2+1
            i[n2]=i[n2]+M[n2]
    return P


def MatSub(a,b):
    n3=-1
    if IsStandard(a) == True:
        P=copy.deepcopy(a)
    else:
        P=Sparse2Standard(a)
    if IsStandard(b)==True:
        Q=copy.deepcopy(b)
    else:
        Q=Sparse2Standard(b)
    for i in P:
        n3=n3+1
        M=Q[n3]
        n4=-1
        for j in i:
            n4=n4+1
            i[n4]=i[n4]-M[n4]
    return P


def MatScalarMul(a,c):
    if IsStandard(a) == True:
        P=copy.deepcopy(a)
    else:
        P=Sparse2Standard(a)
    for i in P:
        n0=-1
        for j in i:
            n0=n0+1
            i[n0]=c*i[n0]
    return P


def MatEq(A,B):
    if IsStandard(A)==True:
        P=copy.deepcopy(A)
    else:
        P=Sparse2Standard(A)
    if IsStandard(B)==True:
        Q=copy.deepcopy(B)
    else:
        Q=Sparse2Standard(B)
    if P==Q:
        return True
    else:
        return False


def MatTransposition(a):
    if IsStandard(a) ==True:
        P=Standard2Sparse(a)
    else:
        P=copy.deepcopy(a)
    P[0]=(P[0])[2]+(P[0])[1]+(P[0])[0]
    for n in range(1,len(P)):
        P[n][0],P[n][1]=P[n][1],P[n][0]
    return(P)


s1 = '[0,0,3,0;0,5,0,0;1,0,0,0]'
s2 = '3-4{(1,3,3),(2,2,5),(3,1,1)}'
##s1 = '[0,0,0,0;0,0,0,0;0,0,0,0]'
##s2 = '3-4{}'
##s1='[]'
##s2='0-0{}'
a = Str2Mat(s1); print(a)
b = Str2Mat(s2); print(b)
print(IsStandard(a))
print(IsStandard(b))
print(Mat2StrStandard(a))
print(Mat2StrStandard(b))
print(Mat2StrSparse(a))
print(Mat2StrSparse(b))
print(Standard2Sparse(a))
print(Sparse2Standard(b))
print(MatAdd(a,b))
print(MatAdd(b,a))
print(MatSub(a,b))
print(MatSub(b,a))
print(MatScalarMul(a, 2))
print(MatScalarMul(a, 2.5))
print(MatScalarMul(a, 1+1j))
print(MatScalarMul(b, 2))
print(MatScalarMul(b, 2.5))
print(MatScalarMul(b, 1+1j))
print(MatTransposition(a))
print(MatTransposition(b))
print(MatEq(a,b))
print(MatEq(b,a))

print()

print(s1 == Mat2StrStandard(a))
print(s1 == Mat2StrStandard(b))
print(s2 == Mat2StrSparse(a))
print(s2 == Mat2StrSparse(b))
print(Mat2StrStandard(MatAdd(a,b)))
print(Mat2StrStandard(MatSub(a,b)))
print(Mat2StrStandard(MatScalarMul(a, 2)))
print(Mat2StrStandard(MatScalarMul(a, 2.5)))
print(Mat2StrStandard(MatScalarMul(a, 1+1j)))
print(Mat2StrStandard(MatScalarMul(b, 2)))
print(Mat2StrStandard(MatScalarMul(b, 2.5)))
print(Mat2StrStandard(MatScalarMul(b, 1+1j)))
print(Mat2StrStandard(MatTransposition(a)))
print(Mat2StrStandard(MatTransposition(b)))

print(Mat2StrSparse(MatAdd(a,b)))
print(Mat2StrSparse(MatSub(a,b)))
print(Mat2StrSparse(MatScalarMul(a, 2)))
print(Mat2StrSparse(MatScalarMul(a, 2.5)))
print(Mat2StrSparse(MatScalarMul(a, 1+1j)))
print(Mat2StrSparse(MatScalarMul(b, 2)))
print(Mat2StrSparse(MatScalarMul(b, 2.5)))
print(Mat2StrSparse(MatScalarMul(b, 1+1j)))
print(Mat2StrSparse(MatTransposition(a)))
print(Mat2StrSparse(MatTransposition(b)))

print()

print(Str2Mat(Mat2StrStandard(MatAdd(a,b))))
print(Str2Mat(Mat2StrStandard(MatSub(a,b))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(a, 2))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(a, 2.5))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(a, 1+1j))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(b, 2))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(b, 2.5))))
print(Str2Mat(Mat2StrStandard(MatScalarMul(b, 1+1j))))
print(Str2Mat(Mat2StrStandard(MatTransposition(a))))
print(Str2Mat(Mat2StrStandard(MatTransposition(b))))

print(Str2Mat(Mat2StrSparse(MatAdd(a,b))))
print(Str2Mat(Mat2StrSparse(MatSub(a,b))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(a, 2))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(a, 2.5))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(a, 1+1j))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(b, 2))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(b, 2.5))))
print(Str2Mat(Mat2StrSparse(MatScalarMul(b, 1+1j))))
print(Str2Mat(Mat2StrSparse(MatTransposition(a))))
print(Str2Mat(Mat2StrSparse(MatTransposition(b))))

print()

