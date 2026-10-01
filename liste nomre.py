
list=[]

list_students=input("1.register  2.login :")

while True:
    match list_students:
        case "1":
            username=input("enter username: ")
            password=int(input("enter password: "))
            list.append(username)
            list.append(password)
            break

        case "2":
            karbari=input("name carbari: ")
            ramz=int(input("ramz ra vared kon: "))

            if karbari=="username" and ramz=="password":
                print("fill the form")
            else:
                print("try again")

            name=input("enter name: ")
            last_name=input("enter last name: ")
            python_score=float(input("enter your pyton score: "))
            java_score=float(input("enter your java score: "))
            html_score=float(input("enter your html score: "))
            list.append(name)
            list.append(last_name)
            list.append(python_score)
            list.append(java_score)
            list.append(html_score)
            print(list)
            break
            