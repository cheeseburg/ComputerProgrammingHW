import copy
import math
def STRINGTOSTANDARD(a):
    a=a.replace(' ','')
    a=a.replace('[','[[')
    a=a.replace(']',']]')
    a=a.replace(';','],[')
    for i in range(len(a)):
                if a[i] == 'j':
                    a = a.replace(',j',',1j')
                    a = a.replace('[j','[1j')
                    a = a.replace(';j',';1j')
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
    A=A.replace('[(','[')
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
                if Q-boo==0:
                    pass
                else:
                    lee[num]=lee[num]+[(Q-boo)*'0,']
                    lee=str(lee)
                    lee=lee.replace("['",'[')
                    lee=lee.replace(",']",']')
                    print(lee)
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

def MatDiv(a,c):
    if IsStandard(a) == True:
        P=copy.deepcopy(a)
    else:
        P=Sparse2Standard(a)
    for i in P:
        n0=-1
        for j in i:
            n0=n0+1
            i[n0]=i[n0]/c
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
        P=copy.deepcopy(a)
    else:
        P=Sparse2Standard(a)
    mat=[]
    for n in range(len(P[0])):
        mat=mat+[[]]
        for i in range(len(P)):
            mat[n].append(P[i][n])
    return(mat)


def MatSul(a,b):
    z=[]
    Sum=0
    for i in range(len(a)):
            z=z+[[]]
            for j in range(len(b[0])):
                    for k in range(len(a[0])):
                            Sum=Sum+a[i][k]*b[k][j]
                    z[i]=z[i]+[Sum]
                    Sum=0
    z=str(z)
    z=z.replace('.0,',',')
    z=z.replace('.0]',']')
    z=z.replace('+0j','')
    z=z.replace('0j','0')
    z=eval(z)
    return z


def dm(a,i,j):
    b=copy.deepcopy(a)
    b.pop(i-1)
    for M in b:
            M.pop(j-1)
    return b

def SUM(a,p):
    if len(a)==3:
        Sum=0
        for i in range(p):
            Sum=Sum+a[0][i]*Matrix(Mat2StrStandard(dm(a,1,i+1))).determinant()*((-1)**(i))
        return Sum
    else:
        Sum=0
        for i in range(p):
            Mat=dm(a,1,i+1)
            Sum=Sum+a[0][i]*SUM(Mat,p-1)*((-1)**(i))
        return Sum


class MatrixSyntaxError(Exception):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name

class Matrix:
    def __init__ (self,mystr,mymode=None):
        self.mystr,self.mymode=mystr.replace(' ',''),mymode
        if self.mystr.count('[') == 1 and self.mymode == None and self.mystr[0] == '[' and self.mystr[-1] == ']':
            try:
                self.mystr = self.mystr.replace(' ','')
                for i in range(len(self.mystr)):
                    if self.mystr[i] == 'j':
                        self.mystr = self.mystr.replace(',j',',1j')
                        self.mystr = self.mystr.replace('[j','[1j')
                        self.mystr = self.mystr.replace(';j',';1j')
                        self.mystr = self.mystr.replace('+j','+1j')
                        self.mystr = self.mystr.replace('-j','-1j')
                Mat2StrStandard(Str2Mat(self.mystr)) == self.mystr or STANDARDTOSTRING(STRINGTOSTANDARD(self.mystr)) == self.mystr
                p=len(Str2Mat(self.mystr)[0])
                for i in Str2Mat(self.mystr):
                    if len(i) != p:
                        raise MatrixSyntaxError('MatrixSyntaxError')
                    else:
                        pass
                self.mystr = self.mystr.replace('.0,',',')
                self.mystr = self.mystr.replace('.0;',';')
                self.mystr = self.mystr.replace('.0]',']')
                self.mystr = self.mystr.replace(',0+',',')
                self.mystr = self.mystr.replace(',0-',',')
                self.mystr = self.mystr.replace(';0+',';')
                self.mystr = self.mystr.replace(';0-',',')
                self.mystr = self.mystr.replace(',0j',',0')
                self.mystr = self.mystr.replace(';0j',';0')
                self.mystr = self.mystr.replace('[0j','[0')
                self.mystr = self.mystr.replace(',-0j,',',0,')
                self.mystr = self.mystr.replace('+0j','')
                self.mystr = self.mystr.replace('-0j','')
                self.mystr = self.mystr.replace('-0;','0;')
                self.mystr = self.mystr.replace('+0;','0;')
                self.mystr = self.mystr.replace(';-0,',';0,')
                self.mystr = self.mystr.replace(';+0,',';0,')
                self.mystr = self.mystr.replace(',+0;',',0;')
                self.mystr = self.mystr.replace(',-0;',',0;')
                self.mystr = self.mystr.replace(',+',',')
                self.mystr = self.mystr.replace(';+',';')
                self.mystr = self.mystr.replace(',0.0j',',0')
                self.mystr = self.mystr.replace(',+0.0j',',0')
                self.mystr = self.mystr.replace(',-0.0j',',0')
                self.mystr = self.mystr.replace(';-0.0j',',0')
                self.mystr = self.mystr.replace(';+0.0j',',0')
                self.mystr = self.mystr.replace(',-0,',',0,')
                self.mystr = self.mystr.replace(',+0,',',0,')
                self.mystr = self.mystr.replace(',-0]',',0]')
                self.mystr = self.mystr.replace(',+0]',',0]')
                self.mystr = self.mystr.replace('[-0,','[0,')
                self.mystr = self.mystr.replace('[+0,','[0,')
                self.mystr = self.mystr.replace('-0-','-')
                self.mystr = self.mystr.replace('+0+','+')
                self.mystr = self.mystr.replace('-0+','+')
                self.mystr = self.mystr.replace('+0-','')
                self.mystr = self.mystr.replace('-0,',',')
                self.mystr = self.mystr.replace('+0,',',')
                self.mystr = self.mystr.replace('.0j','j')
            except: 
                raise MatrixSyntaxError('MatrixSyntaxError')
        else:
            try:
                if self.mymode == 'prefix' or (self.mymode == None and self.mystr[0] != '['):
                    self.mystr = str(self.prefix())
                elif self.mymode == 'postfix':
                    self.mystr = str(self.postfix())
                elif self.mymode == 'infix':
                    self.mystr = str(self.infix())
            except:
                raise MatrixSyntaxError('MatrixSyntaxError')

    def __str__(self):
        return self.mystr

    def prefix(self):
        mystack = Stack()
        mystr = ''
        i = 0
        while i < len(self.mystr):
            if self.mystr[-1-i] in ']':
                j = 0
                while j < len(self.mystr):
                    if self.mystr[-1-i-j] in '[':
                        mystr += self.mystr[-1-i-j : -1-i] + '] '
                        i += j+1
                        j = len(self.mystr)
                    else:
                        j += 1
            elif self.mystr[-1-i] in '+-*/T':
                mystr += ' ' + self.mystr[-1-i] + ' '
                i += 1
            else:
                i += 1
        mylist = mystr.split(' ')
        if '' in mylist:
            num = mylist.count('')
            for i in range(num):
                mylist.remove('')
        else:
            pass
        for i in range(len(mylist)):
            if '[' in mylist[i]:
                mystack.push(Matrix(mylist[i]))
            elif '(' in mylist[i]:
                if 'j' in mylist[i]:
                    mylist[i] = mylist[i].replace('(j)', '(1j)')
                    mylist[i] = mylist[i].replace('+j', '+1j')
                    mylist[i] = mylist[i].replace('-j', '-1j')
                else:
                    pass
                mystack.push(eval(mylist[i]))
            else:
                if mylist[i] in 'T':
                    mystack.push(mystack.pop().transposition())
                elif mylist[i] == '+' or '-' or '*' or '/':
                    try:
                        mytemp1, mytemp2 = mystack.pop(), mystack.pop()
                        if i != -len(mylist):
                            mystack.push(eval('mytemp1'+ mylist[i] + 'mytemp2'))
                        else:
                            if mystack.size() == 0:
                                mystack.push(eval('mytemp1'+ mylist[i] + 'mytemp2'))
                            else:
                                raise MatrixSyntaxError('MatrixSyntaxError')
                    except:
                        raise MatrixSyntaxError('MatrixSyntaxError')
        temp = mystack.pop()
        if '[' in str(temp):
            if str(temp) == '[]':
                temp = Matrix('[0]')
                return temp
            else:
                return temp
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def postfix(self):
        mystack = Stack()
        mystr = ''
        i = 0
        while i < len(self.mystr):
            if self.mystr[i] in '[(':
                j = 0
                while j < len(self.mystr) - i:
                    if self.mystr[i+j] in ')]':
                        mystr += self.mystr[i : i+j+1] + ' '
                        i += j+1
                        j = len(self.mystr) - i
                    else:
                        j += 1
            elif self.mystr[i] in '+-*/T':
                mystr += ' ' + self.mystr[i] + ' '
                i += 1
            else:
                i += 1
        mylist = mystr.split(' ')
        print(mylist)
        if '' in mylist:
            num = mylist.count('')
            for i in range(num):
                mylist.remove('')
        else:
            pass
        for i in range(len(mylist)):
            if '[' in mylist[i]:
                mystack.push(Matrix(mylist[i]))
            elif '(' in mylist[i]:
                if 'j' in mylist[i]:
                    mylist[i] = mylist[i].replace('(j)', '(1j)')
                    mylist[i] = mylist[i].replace('+j', '+1j')
                    mylist[i] = mylist[i].replace('-j', '-1j')
                else:
                    pass
                mystack.push(eval(mylist[i]))
            else:
                if mylist[i] in 'T':
                    mystack.push(mystack.pop().transposition())
                elif mylist[i] == '+' or '-' or '/' or '*':
                    try:
                        mytemp1, mytemp2 = mystack.pop(), mystack.pop()
                        if i != len(mylist):
                            mystack.push(eval('mytemp2'+ mylist[i] + 'mytemp1'))
                        else:
                            if mystack.size() == 0:
                                mystack.push(eval('mytemp2'+ mylist[i] + 'mytemp1'))
                            else:
                                raise MatrixSyntaxError('MatrixSyntaxError')
                    except:
                        raise MatrixSyntaxError('MatrixSyntaxError')
        temp = mystack.pop()
        if '[' in str(temp):
            if str(temp) == '[]':
                temp = Matrix('[0]')
                return temp
            else:
                return temp
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def infix(self):
        mystr = self.mystr.replace('T', '.transposition()')
        mystr = mystr.replace('[', "Matrix('[")
        mystr = mystr.replace(']', "]')")
        ans = eval(mystr)
        return ans
            
    def __add__(self,other):
        if len(Str2Mat(str(self.mystr)))==len(Str2Mat(str(other.mystr))) and len(Str2Mat(str(self.mystr))[0])==len(Str2Mat(str(other.mystr))[0]):
            return Matrix(Mat2StrStandard(MatAdd(Str2Mat(str(self.mystr)),Str2Mat(str(other.mystr)))))
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')
        raise MatrixSyntaxError('MatrixSyntaxError')

    def __sub__(self,other):
        if len(Str2Mat(str(self.mystr)))==len(Str2Mat(str(other.mystr))) and len(Str2Mat(str(self.mystr))[0])==len(Str2Mat(str(other.mystr))[0]):
            return Matrix(Mat2StrStandard(MatSub(Str2Mat(str(self.mystr)),Str2Mat(str(other.mystr)))))
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def __neg__(self):
        p = Str2Mat(str(self.mystr))
        for i in p:
            n0=-1
            for j in i:
                n0=n0+1
                i[n0]=0-i[n0]   
        p = Matrix(Mat2StrStandard(p))
        return p

    def __mul__(self,other):
        try:
            if len(Str2Mat(str(self.mystr)))==len(Str2Mat(str(other.mystr)))==1:
                return Matrix('[]')
            if len(Str2Mat(str(self.mystr))[0])==len(Str2Mat(str(other.mystr))):
                return Matrix(Mat2StrStandard(MatSul(Str2Mat(str(self.mystr)),Str2Mat(str(other.mystr)))))
            else:
                raise MatrixSyntaxError('MatrixSyntaxError')
        except AttributeError:
            return Matrix(Mat2StrStandard(MatScalarMul(Str2Mat(str(self.mystr)),other)))
        except:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def __truediv__(self,num):
        try:
            return Matrix(Mat2StrStandard(MatDiv(Str2Mat(str(self.mystr)),num)))
        except:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def __eq__(self,other):
        Judge=MatEq(Str2Mat(str(self)),Str2Mat(str(other)))
        return Judge

    def isIdentity(self):
        if self.mystr == '[]':
            return True
        else:
            pass
        if len(Str2Mat(str(self.mystr)))==len(Str2Mat(str(self.mystr))[0]):
            m=copy.deepcopy(self.mystr)
            m=Str2Mat(str(m))
            Count=len(m[0])
            Sum1=0
            Sum2=0
            for i in range(Count):
                if m[i][i]==1:
                    t=m[i].count(0)
                    Sum1=Sum1+1
                    Sum2=Sum2+t
                    t=0
            if Sum1==Count and Sum2==(Count-1)*Count:
                return True
            else:
                return False
        else:
            return False

    def isSquare(self):
        if self.a == '[]':
            return True
        elif len(Str2Mat(str(self.mystr))[0])==len(Str2Mat(str(self.mystr))):
            return True
        else:
            return False

    def __getitem__(self,key):
        if type(key) == tuple and type(key[0])==int:
            if key[0]<=len(Str2Mat(str(self.mystr)))-1 and key[0]>=0 and key[1]<=len(Str2Mat(str(self.mystr))[0])-1 and key[1]>=0:
                return Str2Mat(str(self.mystr))[key[0]][key[1]]
            else:
                raise MatrixSyntaxError('MatrixSyntaxError')
        elif type(key) == int:
            if key<=len(Str2Mat(str(self.mystr)))-1 and key>=0:
                return Matrix(STANDARDTOSTRING(Str2Mat(str(self.mystr))[key]))
            else:
                raise MatrixSyntaxError('MatrixSyntaxError')
        else:
            Lst=[]
            b=Str2Mat(str(self.mystr))[key[0]]
            for i in b:
                Lst=Lst+[i[key[1]]]
            return Matrix(STANDARDTOSTRING(Lst))

    def __setitem__(self,key,item):
        if type(key)==tuple and type(key[0])==int:
            if key[0]<=len(Str2Mat(str(self.mystr)))-1 and key[0]>=0 and key[1]<=len(Str2Mat(str(self.mystr))[0])-1 and key[1]>=0:
                p=Str2Mat(str(self.mystr))
                p[key[0]][key[1]]=item
                self.mystr=STANDARDTOSTRING(p)
            else:
                raise MatrixSyntaxError('MatrixSyntaxError')
        elif type(key) == int:
            if key<=len(Str2Mat(str(self.mystr)))-1 and key>=0:
                q=Str2Mat(str(item))
                p=Str2Mat(str(self.mystr))
                if len(q[0]) == len(p[key]):
                    p[key]=q[0]
                    self.a=STANDARDTOSTRING(p)
                else:
                    raise MatrixSyntaxError('MatrixSyntaxError')
            else:
                raise MatrixSyntaxError('MatrixSyntaxError')
        elif type(key[0])==slice:
            b=Str2Mat(str(self.mystr))
            q=STRINGTOSTANDARD(str(item))
            num=len(b[key[0]])
            i = 0
            try:
                for i in range(num):
                    t=b[key[0]][i]
                    t[key[1]]=q[i]
                self.mystr=STANDARDTOSTRING(b)
                
            except:
                raise MatrixSyntaxError('MatrixSyntaxError')
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def __pow__(self,num):
        if self.isSquare()==True:
            p=copy.deepcopy(self.mystr)
            for i in range(num-1):
                p=Matrix(Mat2StrStandard(MatSul(Str2Mat(str(self.mystr)),Str2Mat(str(p)))))
            return p
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')

    def determinant(self):
        if Matrix(str(self.mystr)).isSquare() != True:
            raise MatrixSyntaxError('MatrixSyntaxError')
        else:
            if self.a=='[]':
                return 1
            else:
                m=copy.deepcopy(self.mystr)
                m=STRINGTOSTANDARD(str(m))
                row=col=len(m)
                if row==2:
                    return m[0][0]*m[1][1]-m[0][1]*m[1][0]
                else:
                    return SUM(m,row)

    def transposition(self):
        m=copy.deepcopy(self.mystr)
        return Matrix(STANDARDTOSTRING(MatTransposition(Str2Mat(str(m)))))

    def inverse(self):
        if Matrix(str(self.mystr)).isSquare() != True:
            raise MatrixSyntaxError('MatrixSyntaxError')
        else:
            if len(STRINGTOSTANDARD(str(self.mystr)))==2:
                m=Matrix(self.mystr)
                h=m[0,0]*m[1,1]-m[0,1]*m[1,0]
                if h==0:
                    raise MatrixSyntaxError('MatrixSyntaxError')
                else:
                    n=[[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]]
                    return Matrix(STANDARDTOSTRING(n))*(1/h)
            else:
                m=copy.deepcopy(self.mystr)
                m=STRINGTOSTANDARD(str(m))
                a1=len(m)
                a2=len(m)
                g=[]
                g=g+a1*[[]]
                for i in range(a1):
                    for k in range(a1):
                        g[i]=g[i]+[Matrix(STANDARDTOSTRING(dm(m,i+1,k+1))).determinant()*((-1)**(i+k))]
                g=Matrix(STANDARDTOSTRING(g))
                g=g.transposition()
                temp=Matrix(self.mystr).determinant()
                if temp != 0:
                    m=g/temp
                    return m
                else:
                    raise MatrixSyntaxError('MatrixSyntaxError')
                
class Stack:  
    def __init__(self): 
        self.items = [] 
         
    def isEmpty(self): 
        return len(self.items)==0  
     
    def push(self, item): 
        self.items.append(item) 
     
    def pop(self):
        if self.isEmpty() == False:
            return self.items.pop()
        else:
            raise MatrixSyntaxError('MatrixSyntaxError')
     
    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 
         
    def size(self): 
        return len(self.items)

    def see(self):
        return self.items




##test area 

x = Matrix("[1,2,3; 4,5,6; 7,8,9]") 
y = Matrix("[0,1,2; 3,4,5; 6,7,8]") 
##
####prefix 
##test0 = Matrix("[]") 
##print(test0) 
##test1 = Matrix("* [1,2,3;3,4 ,5] [1,2;3 ,4;5,6]", "prefix") 
##print(test1) 
##test2 = Matrix("+[3]*T[1](122 j)") 
##print(test2) 
##test3 = Matrix("+++-+[1][1][1][1][1][1]") 
##print(test3) 
##test4 = Matrix('(5)*[4]','prefix') 
##print(test4) 
##test4new = Matrix(' * [4     ](     5 )') 
##print(test4new) 
##
##print(x+y) 
##print(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) 
##print(str(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x+y)) 
##print(str(Matrix("- [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x-y)) 
##print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x*y)) 
##print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x*2)) 
##print(str(Matrix("/ [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x/2)) 
##print(str(Matrix("T [1,2,3; 4,5,6; 7,8,9]"))) 
##z = x * y 
##print(str(Matrix("/ [24,30,36;51,66,81;78,102,126] (2)")) == str(z / 2)) 
##print() 
##
##
##
####postfix 
##
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] +", "postfix")) == str(x+y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] -", "postfix")) == str(x-y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] *", "postfix")) == str(x*y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) *", "postfix")) == str(x*2)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) /", "postfix")) == str(x/2)) 
##print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "postfix"))) 
##z = x * y 
##print(str(Matrix("[24,30,36;51,66,81;78,102,126] (2) /", "postfix")) == str(z / 2)) 
##print(Matrix('/[2][2](2)','prefix')) 

#infix 
##test0 = Matrix("[]","infix") 
##print(test0) 
##test1 = Matrix("[1,2,3; 3,4,5] * [1,3,5; 2,5,6]T","infix") 
##print(test1) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] + [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x+y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] - [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x-y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x*y)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * (2)", "infix")) == str(x*2)) 
##print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] / (2 )", "infix")) == str(x/2)) 
##print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "infix"))) 
##z = x * y 
##print(str(Matrix("[24,30,36;51,66,81;78,102,126] /( 2)", "infix")) == str(z / 2)) 
##print() 

#####extra testcase: 
##x = Matrix('-*[1,2,3; 3,4,5] [1,2; 3,4; 5, 6][1,2;3,4]') 
##x1 = Matrix('*[1,2,3; 3,4,5] [1,2; 3,4; 5, 6]') 
##x2 = Matrix('[1,2;3,4][1,2,3; 3,4,5]* [1,2; 3,4; 5, 6]-','postfix') 
##print(x) 
##print(x1) 
##print(x2) 
##y = Matrix("** [1,2,3; 3,4,5] [1,2; 3,4; 5, 6][1,2;3,4]", "prefix") 
##print(y) 
##z = Matrix("[1,2,3; 3,4,5] * [1,2; 3,4; 5, 6]*[1,2;3,4]", "infix") 
##print(z) 
##z = Matrix("[1,2,3; 3,4,5] /(-5)* [1,2; 3,4; 5, 6]*(5)*([1,2;3,4]*(5)*(6))", "infix") 
##print(z) 
##x = Matrix("[1,2,3; (3),4j,5][1,2; 3,4; 5, 6] *[1,2;3,4]*", "postfix") 
##print(x) 
##x = Matrix('[0*1j]T[0*2j]*', 'postfix')
##print(x)
####x = Matrix('*[0*2j]T[0*1j]','prefix') 
#x = Matrix('([0.1j]+[0.2j])-[0+3j]', 'infix')#?maybe bug 
##y = Matrix('[0.1j][0.2j]+[0+3j]-', 'postfix')#?maybe bug 
##z = Matrix('**[1,2;3,4][1,2;4,5][8j,0;1j,0+j]', 'prefix') 
##print(z) 
##x = Matrix('*[1;(2+j);3;4][1,2,3,4]') 
#print(x.complexmatrix,x) 
##x = Matrix('*[1,2,3,4][1;2;3;4]') 
##x = Matrix('TT[4+j]', 'prefix') 
#x = Matrix('[4+j]TT', 'postfix') 
#y = Matrix('[8]+[0]', 'infix') 
##print(x / 6) 
##print(x + y) 
##print(y) 
##print(x) 
#x = Matrix('*[4][7]','prefix') 
#print(x) 

#ultra testcases 
#x = Matrix("[2,3]*(1+j)", "infix") 
#print(x) 
#x = Matrix("*[2,3](1+j)", "prefix") 
#print(x) 
#x = Matrix("[1,2]+[2,3]+[3,4]", "infix") 
#print(x) 
#x = Matrix("/[2][2](2)", "prefix") 
#print(x) 
#x = Matrix("[2,3](1+j)*", "postfix") 
#print(x) 
#x = Matrix("**T[1,2,3; 4,5,6](0.0j)(5.0)", "prefix") 
#print(x) 
#x = Matrix("**[1,2,3; 4,5,6](0+j)(5)")#bug 
#print(x) 
#x = Matrix("[1,  2  ,3   ;   4, 5, 6]*(0 +   j  )   ", "infix") 
#print(x) 
#x = Matrix("[5]*(4*(2+1j))", "infix") 
#print(x) 
# one more (3) raise Error 
#c = Matrix('[0]    T(3)/(3)*', 'postfix') 
#print (c) 
#c = Matrix('[]T*[3,4,5;1,2,3;2,3,4;6,7,8]T/(3)', 'infix') 
#c = Matrix('[0]', 'infix') 
#print (c) 
#x = Matrix("([5]+[1])*5 ", "infix") 
#print(x) 
#x = Matrix('+T[1;2][2,1]', 'prefix') 
#print(x)



        
                         
        
                    

        
    
