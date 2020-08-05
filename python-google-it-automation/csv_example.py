import csv

file=open("contacts.csv")

csv_file=csv.reader(file)

for row in csv_file:
    name,phone,role=row
    print(f"Name: {name:>10} | Phone: {phone:30}  | Role: {role}")


file.close()

passwords=[["ohidur@yandex.com","mysuperfunnypassword!"],["bappy@yourdomain.com","hello+_ohidur"]]


with open("passwords.csv",'w') as passwords_file:
    csv_writer=csv.writer(passwords_file)
    csv_writer.writerows(passwords)



# dict reader

with open("employees.csv",'r') as employees_csv:
    dict_reader=csv.DictReader(employees_csv)
    
    for row in dict_reader:

        print("{} is  of {} years old and salary is {}".format(
            row['name'],row['age'],row['salary']
        ))


# dict writer

books=[{"name":"The road ahead","author":"Bill gates"},{"name":"Idea man","author":"Paul Allen"}]

header=['name','author']

with open('books.csv','w') as books_csv:
    writer=csv.DictWriter(books_csv,header)
    writer.writeheader()
    writer.writerows(books)