import json
#load config file
json_file = open('config.json')
config = json.load(json_file)
conPos = config['conPos']
bytePos = config['bytePos']
#load data file
data_file = open(config['fileName'],"r")
data = data_file.read()
data = data.split('\n')
n=len(data)
#creare dict
con_dict={}
byte_dict={}
for i in range(1,n-1):
    #read data,remove empty string
    line = data[i]
    line = line.split(' ')
    while '' in line:
        line.remove('')
    #count start
    if line[conPos] in con_dict:
        con_dict[line[conPos]]+=1
        byte_dict[line[conPos]]+=int(line[bytePos])
    else:
        con_dict[line[conPos]]=1
        byte_dict[line[conPos]]=int(line[bytePos])
#sort the dict
con_dict=sorted(con_dict.items(),key=lambda x:x[1],reverse=True)
byte_dict=sorted(byte_dict.items(),key=lambda x:x[1],reverse=True)
#print the result
print("Sorted by total number of connections")
print("       IP         CON")
for i in range(0,min(200,len(con_dict)-1)):
    print(con_dict[i])
print("Sorted by total number of Bytes")
print("       IP         TotByts")
for i in range(0,min(200,len(con_dict)-1)):
    print(byte_dict[i])
