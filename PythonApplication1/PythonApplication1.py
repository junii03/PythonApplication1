file=open(20200317.txt")
count=0;
for lines in file:
    print(lines.rstrip())
    count=count+1
    
print('Number of lines in file',count)
