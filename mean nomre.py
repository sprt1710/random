
list_name=[]
list_score=[]

list_students=input("1.shakhsi  2.nomre :")

while True:
    match list_students:
        case "1":
            name=input("enter name: ")
            last_name=input("enter last name: ")
            list_name.append(name)
            list_name.append(last_name)
            print(list_name)
        case "2":
            python_score=float(input("enter your pyton score: "))
            java_score=float(input("enter your java score: "))
            html_score=float(input("enter your html score: "))
            list_score.append(python_score)
            list_score.append(java_score)
            list_score.append(html_score)
            print(list_score)
            score_sum=sum(list_score)
            score_mean=score_sum/len(list_score)
            list_score.append(score_mean)
            print(list_score)
            break

            
            