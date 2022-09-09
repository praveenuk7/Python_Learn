#create a file
#f=open("sample.txt","w")
#f=open("F:/Downloads/File/Sample.docx","w")
f=open("sample.txt","a")
f.write("Learn Java Programming\n")
f.close()

f=open("sample.txt","r")
read=f.read()
print(read)
f.close()