#This program writes down the days of the week into the file 
l1=['Monday','Tuesday','Wednesday','Thursday','Friday']  #list containing all the days
f=open('ash1.txt','w') #creates the text and  w is used for write 
for ele in l1:
    f.write(ele+'\n')   #write operation is performed
f.close()    

