import csv
import os


def createContactsDirectory():
    file_path = "./contacts" #put the path as per your choice
    if not os.path.exists(file_path):
        os.mkdir(file_path);

def convert(fileName):
    count = 0
    with open(fileName) as csvfile:
        createContactsDirectory()
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            #In my case row[0] of csvfile is firstname, row[1] is lastname and row[2] is given name. Change according to your file
            firstname=row[0]
            midname=row[1]
            lastname=row[2]

            #row[20] holds the contact info. Change accorindly
            contact=row[3]

            if(firstname!='' or midname!='' or lastname!=''): #checking for presence of name in firstname
                f = open("contacts/"+firstname+".vcf","w+") #name of vcf file will be based on the value of names
                print('Creating card for '+firstname+" "+midname+" "+lastname)

                #writing the below contents to create vcf file
                f.write('BEGIN:VCARD \n')
                f.write('VERSION:2.1 \n')
                f.write('N:' + firstname + '\n')
                f.write('FN:' + firstname + ' ' + midname +' '+ lastname+ '\n')
                f.write('TEL;HOME;VOICE:' + contact + '\n')
                f.write('END:VCARD\n')
                f.close()
                count=count+1
        print(str(count)+" number of vcfs successfully created")

def main():
    convert('contacts.csv')

if __name__ == '__main__':
    main()
