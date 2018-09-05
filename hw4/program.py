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

class program:
    def __init__(self,mystr):
        mystr=mystr.replace('\t','')
        mystr=mystr.replace('\v','')
        self.mystr = mystr
        self.value = None
##    def __str__(self):
##        return self.mystr
    def evaluate(self):
        newstr = ''
        mystr = copy.deepcopy(self.mystr)
        mystr = mystr.replace('\t', '')
        mystr = mystr.replace('bool', '')
        mystr = mystr.replace(' ', '')
        mystr = mystr.replace('!', ' not ')
        mystr = mystr.replace('|', ' or ')
        mystr = mystr.replace('&', ' and ')
        mystr = mystr.replace('bool', 'bool ')
        mystr = mystr.replace(')\n', '):\n')
        mystr = mystr.replace('():\n', '()')
        mystr = mystr.replace('{', '')
        mystr = mystr.replace('}', '')
        mystr = mystr.replace(';', '')
        mystr = mystr.replace('return', 'return ')
        mylist = mystr.split('\n')
        mylist.insert(0, 'def main():')
        mylist.insert(1, 'mycount = 0')
##        print(mylist)
        for i in mylist:
            num = mylist.index(i)
            if i == '    main()':
                mylist[num] = ''
            if i == '':
                continue
            elif 'def main():' in i:
                for j in range(1, len(mylist)):
                    mylist[j] = '    '+mylist[j]
            elif ':' in i:
                Count = i.count('    ')
                for k in range(len(i)):
                    if i[k] == ':':
                        i = i.replace(i[:k+1], Count * '    ')
                        mylist[num] = i
                        break
                    else:
                        pass
            if 'if' in i:
                p = num - 1
                while p < len(mylist):
                    if 'if' in mylist[p]:
                        for q in range(p+1, len(mylist)):
                            if 'fi' in mylist[q]:
                                mylist[q] = ''
                                break
                            else:
                                mylist[q] = '    '+mylist[q]
                        p += len(mylist)
                    else:
                        p += 1
            if 'while' in i:
                p = num -1
                while p < len(mylist):
                    if 'while' in mylist[p]:
                        for q in range(p+1, len(mylist)):
                            if 'done' in mylist[q]:
                                break
                            else:
                                mylist[q] = '    '+mylist[q]
                        p += len(mylist)
                    else:
                        p += 1
            else:
                pass
        myList = []
        [myList.append(i) for i in mylist if not i == '']
        for mystr in myList:
            newstr += mystr+'\n'
        newstr = newstr.replace('    done', '        mycount += 1\n        if mycount > 20:\n            return "infinite"\n        else:\n            pass')
        newstr += 'self.value = main()'
##        print(mylist)
##        print(myList)
##        print(newstr)
        exec(newstr)
        return self.value

    def getCFG(self):
        mystr = copy.deepcopy(self.mystr)
        mystr = mystr.replace('    ', '')
        mystr = mystr.split('\n')
        myList, mylist, L,matrix,mydict = [], [], [], '', {}
        for i in range(len(mystr)):
            if ':' in mystr[i] or 'fi' in mystr[i] or 'done' in mystr[i]:
                mylist.append(mystr[i])
            else:
                pass
        for j in range(len(mylist)):
            if j == 0 and 'while' not in mylist[j] and 'if' not in mylist[j]:
                mynum = mylist[j].find(':')
                temp1 = mylist[j][:mynum]
                mydict[temp1] = 'None'
                myList.append(temp1)
            if j+1 < len(mylist):
                if 'while' in mylist[j]:
                    mynum = mylist[j].find(':')
                    temp1 = mylist[j][:mynum]
                    mynum = mylist[j+1].find(':')
                    temp2 = mylist[j+1][:mynum]
                    mydict[temp1] = 'while'
                    mydict[temp2] = 'None'
                    myList.append(temp1)
                    myList.append(temp2)
                elif 'if' in mylist[j]:
                    mynum = mylist[j+1].find(':')
                    temp1 = mylist[j+1][:mynum]
                    mydict[temp1] = 'if'
                    myList.append(temp1)
                elif 'fi' in mylist[j] or 'done' in mylist[j]:
                    if 'while' in mylist[j+1]:
                        pass
                    else:
                        mynum = mylist[j+1].find(':')
                        temp1 = mylist[j+1][:mynum]
                        mydict[temp1] = 'None'
                        myList.append(temp1)
                else:
                    pass
            else:
                pass
        L = sorted(myList)
        for i in range(len(myList)):
            if i == 0:
                matrix += '['
            for j in range(len(myList)):
                if j == len(myList) - 1:
                    if i == len (myList) - 1:
                        matrix += '0'
                    else:
                        matrix += '0;'
                else:
                    matrix += '0,'
            if i == len(myList) - 1:
                matrix += ']'
            else:
                pass
        a = STRINGTOSTANDARD(matrix)
        i = 0
        while i < len(myList):
            if i+1 < len(myList) or i+2 < len(myList):
                if 'if' in mydict[myList[i]]:
                    temp1 = L.index(myList[i-1])
                    temp2 = L.index(myList[i+1])
                    temp3 = L.index(myList[i])
                    a[temp1][temp2]=1
                    a[temp3][temp2]=1
                    i+=1
                elif 'while' in mydict[myList[i]]:
                    temp1 = L.index(myList[i+1])
                    temp2 = L.index(myList[i+2])
                    temp3 = L.index(myList[i])
                    a[temp1][temp2]=0
                    a[temp3][temp1]=1
                    a[temp1][temp3]=1
                    a[temp3][temp2]=1
                    i+=2
                else:
                    temp1 = L.index(myList[i])
                    temp2 = L.index(myList[i+1])
                    a[temp1][temp2]=1
                    i += 1
            else:
                i+=1
        a = STANDARDTOSTRING(a)
        a = a.replace(' ', '')
        return a



##s="""
##    bool x = True;
##    bool y = False;
##    bool z = True;
##    bool a = True;
##    main()
##    {
##    1:  x= !y;
##    2:  z= !x;
##    3:  if ( (x & y) | (! z) )
##    4:      y= !y;
##    5:      pass;
##        fi
##    6:  x=!y;
##    7:  z=!z;
##    8:  while ( ( x | y) & (a | z) )
##    9:      a=!y;
##    10:     y=!z;
##        done
##    11: return x;
##    } 
##"""
##
##p=program(s)
##print(p.getCFG())
