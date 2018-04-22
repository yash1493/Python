import os,os.path
import csv
dir ='C:\\Users\\yash1493\\Desktop\\Python\\input.txt'
dic={'A':0,'B':1,'C':2,'D':3,'E':4}
list=[]         #will contain pair
out =[]

def series(x,y):
    if out[x][y]==0:
        return
    out[x][y]=0
    

##################################################################
if __name__ == "__main__":
    with open(dir,mode='r') as f:
        list=[line.strip() for line in f]

    for i in range(0,5):
        inn =[]
        for j in range(0,5):
            inn.append(0)
        out.append(inn)
    for item in list:
        x=item[0]
        y=item[2]
        out[dic[x]][dic[y]]=1
    for i in range(0,5):
        for j in range(0,5):
            if out[i][j]==1:
                series(i,j)
##############Above part converts file to a matrix################

