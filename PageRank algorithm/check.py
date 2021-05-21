import os
import shutil


def replace_pr():
    os.remove("pr.txt")
    source = "pr1.txt"
    destination = "pr.txt"
    dest = shutil.copyfile(source, destination)


def start(con):
    count = 0
    n = 0
    conv = 0.001  
    total = 0.0
    with open("pr.txt",'r') as file1, open("pr1.txt",'r') as file2:
        
        for line1, line2 in zip(file1, file2):
            count += 1
            old_pagerank = float(line1.split(",")[1])
            new_pagerank = float(line2.split(",")[1])

            total += abs(old_pagerank-new_pagerank)
            if(abs(old_pagerank-new_pagerank) < conv):
                n += 1

    if(n == count):
        con=0
    else:
        print("Convergence: " + str(total/count) + '\n')
        replace_pr()
        con=1
    return con

iter=0
con = 1

while iter<=20:
    iter+=1
    if con==1:
        r=os.system('hadoop jar C:/Users/dhruv/sw/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -input /user/dhruva/output10/part-00000 -output /user/dhruva/output11 -file mapper.py -mapper "python mapper.py C:\\Users\\dhruv\\Downloads\\hadoop\\pagerank\\pr.txt" -file reducer.py -reducer "python reducer.py" & hadoop fs -cat /user/dhruva/output11/part-00000 > C:\\Users\\dhruv\\Downloads\\hadoop\\pagerank\\pr1.txt & hdfs dfs -rm -r /user/dhruva/output11/ &')
        con=start(con)
    else:
        exit()
    
    