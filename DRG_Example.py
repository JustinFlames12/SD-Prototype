import random
import os
import shutil
#import openpyxl

#Making Directories
if not os.path.exists("DRG Directory (Fake)"):
    os.mkdir('DRG Directory (Fake)')

fake_directories = ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
for fake_dir in fake_directories:
    if not os.path.exists(f"DRG Directory (Fake)/{fake_dir}"):
        os.mkdir(f'DRG Directory (Fake)/{fake_dir}')

#Copying files
shutil.copy("HR Work Schedule.xlsx", 'DRG Directory (Fake)/Documents')
if not os.path.exists("DRG Directory (Fake)/Documents"):
    os.rename('DRG Directory (Fake)/Documents/HR Work Schedule.xlsx', 'DRG Directory (Fake)/Documents/HR Work Schedule (Fake).xlsx')

shutil.copy("Employee Payment System Tutorial.docx", 'DRG Directory (Fake)/Documents')
if not os.path.exists("DRG Directory (Fake)/Documents"):
    os.rename('DRG Directory (Fake)/Documents/Employee Payment System Tutorial.docx', 'DRG Directory (Fake)/Documents/Employee Payment System Tutorial (Fake).docx')

shutil.copy("Mustang.png", 'DRG Directory (Fake)/Pictures')
if not os.path.exists("DRG Directory (Fake)/Pictures"):
    os.rename('DRG Directory (Fake)/Pictures/Mustang.png', 'DRG Directory (Fake)/Pictures/Mustang (Fake).png')


info = []
real = open ("DRG Example.txt", "r") #Real DRG file
fake = open ("DRG Directory (Fake)/Documents/DRG Example (Fake).txt", "w") #Fake DRG file
#fake_hrsch = open ("DRG Directory (Fake)\HR Work Schedule (Fake).xlsx", "w") #Fake HR Work Schedule file
hrsch = open ("HR Work Schedule.xlsx", "r") #Fake HR Work Schedule file

#Opening Excel File Sheets


#Generating files
fname = open ("DRG_Generator\First Names.txt", "r")
lname = open ("DRG_Generator\Last Names.txt", "r")
streets = open ("DRG_Generator\Streets.txt", "r")
wtitle = open ("DRG_Generator\Work Titles.txt", "r")


#Variables
counter = 0
filecounter = 1
randfnamecounter = random.randint(0, 50)
randlnamecounter = random.randint(0, 50)
randaccnumcounter = random.randint(0, 1000000000000)  
randrounumcounter = random.randint(0, 1000000000) 
randemplcounter = random.randint(0, 10000000)
randwtitlecounter = random.randint(0, 50)
randaddrcounter1 = random.randint(0, 10000)
randaddrcounter2 = random.randint(0,50)

fake_info = '' #['First Name', 'Last Name', 'Account Number', 'Routing Number', 'Employee ID', 'Title', 'Address']
with real:
    for lines in real.readlines():
        with open ("DRG Directory (Fake)/Documents/DRG Example (Fake).txt", "w"):
            part = lines.split(':')
            #info.append(part)
            if part[counter] == 'First Name':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                for flines in fname.readlines():
                    #print("Random: " + str(randfnamecounter) + "Line: " + str(filecounter))
                    if filecounter == randfnamecounter:
                        secpart = flines.split(':')
                        #print(secpart)   
                        fake.writelines(part[counter] + ": " + secpart[0])
                        #print(part[counter] + ": " + secpart[filecounter + 1] + "\n") 
                        filecounter = 0
                        break
                    filecounter = filecounter + 1          
            elif part[counter] == 'Last Name':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                for llines in lname.readlines():
                    #print("Random: " + str(randfnamecounter) + "Line: " + str(filecounter))
                    if filecounter == randlnamecounter:
                        secpart = llines.split(':')
                        #print(secpart)   
                        fake.writelines(part[counter] + ": " + secpart[0])
                        #print(part[counter] + ": " + secpart[filecounter + 1] + "\n") 
                        filecounter = 0
                        break
                    filecounter = filecounter + 1  
            elif part[counter] == 'Account Number':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                fake.writelines(part[counter] + ": " + str(randaccnumcounter) + "\n")
            elif part[counter] == 'Routing Number':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                fake.writelines(part[counter] + ": " + str(randrounumcounter) + "\n") 
            elif part[counter] == 'Employee ID':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                fake.writelines(part[counter] + ": " + str(randemplcounter) + "\n") 
            elif part[counter] == 'Title':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                for tlines in wtitle.readlines():
                    #print("Random: " + str(randfnamecounter) + "Line: " + str(filecounter))
                    if filecounter == randwtitlecounter:
                        secpart = tlines.split(':')
                        #print(secpart)   
                        fake.writelines(part[counter] + ": " + secpart[0])
                        #print(part[counter] + ": " + secpart[filecounter + 1] + "\n") 
                        filecounter = 0
                        break
                    filecounter = filecounter + 1         
            elif part[counter] == 'Address':
                #fake.write(part[counter] + ": " + "*First Name*\n")
                for alines in streets.readlines():
                    #print("Random: " + str(randfnamecounter) + "Line: " + str(filecounter))
                    if filecounter == randaddrcounter2:
                        secpart = alines.split(':')
                        #print(secpart)   
                        fake.writelines(part[counter] + ": " + str(randaddrcounter1) + " " + secpart[0])
                        #print(part[counter] + ": " + secpart[filecounter + 1] + "\n") 
                        filecounter = 0
                        break
                    filecounter = filecounter + 1       
            else:
                fake.write(part[counter] + ": " + "*Fake_Info*\n")
            counter + 1