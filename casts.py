import sys  
#returns common number of casts and the common cast
def connectCasts(casts,n):
    #finds common cast betwenn first two casts
    z=casts[0].intersection(casts[1])

    #if there is exactly one common connection in first two casts, then return one.
    if(len(z)>=1):
        return (1,z)
    common=[]
    #otherwiwse, check if there exists other common cast fromm 2 to n casts
    for cast in range(2,len(casts)):
        common=casts[0].intersection(casts[cast])
        if(len(common)==1):
            common1=casts[1].intersection(casts[cast])
            if(len(common1)==1):
                return (2,casts[cast])
    return (3,0)

casts=list()
#filename input as argument
filename="./"+sys.argv[1]
with open(filename) as fp:
    
    #reading  the first line of the file that is no of casts
    n=int(fp.readline()[-2])
    if(n<=2):
        raise Exception("No. of casts must be greater than 2")
    #reading remaining file
    for i in range(n):
        #reading the cast and split the line with commas
        words=(fp.readline()[11:-2]).split(',')
        for word in range(len(words)):
            words[word]=words[word].strip()[1:-1]
            
        casts.append(set(words))


shortest_conn,castname=(connectCasts(casts,n))

if(shortest_conn == 1):
    print("Shortest connection = ",shortest_conn,'\ncast = ',castname)
elif shortest_conn == 2 :
    print("Shortest connection = ",shortest_conn,'\ncast = ',castname)
else:
    print("shortest connection > 2 or no connection")
