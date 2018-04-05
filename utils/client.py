#client.py
 
import sys
import socket 
 
skClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skClient.connect(("10.1.39.102",8085))
 
sFileName = raw_input("Enter Filename to download from server : ")
sData = "Temp"
 
while True:
    skClient.send(sFileName)
    sData = skClient.recv(1024)
    fDownloadFile = open(sFileName,"w")
    while sData:
        print sData
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print "Download Completed"
    break
fDownloadFile.close()
skClient.close(
