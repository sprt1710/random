

import random
while   True:
    list_javayez=[]

    afrad=["pedram","sahar","roham","tiam"]
    jayeze=["mashin","khone","mobile","ps"]

    jayeze1_1=random.choice(afrad)
    jayeze_1_2=random.choice(jayeze)
    afrad.remove(jayeze1_1)
    jayeze.remove(jayeze_1_2)

    jayeze_2_1=random.choice(afrad)
    afrad.remove(jayeze_2_1)
    jayeze_2_2=random.choice(jayeze)
    jayeze_2_2.remove(jayeze_2_2)

    jayeze3_1=random.choice(afrad)
    jayeze_3_2=random.choice(jayeze)
    afrad.remove(jayeze3_1)
    jayeze.remove(jayeze_3_2)
    
    jayeze_4_1=random.choice(afrad)
    afrad.remove(jayeze_4_1)
    jayeze_4_2=random.choice(jayeze)
    jayeze.remove(jayeze_4_2)

    list_javayez.append(jayeze1_1)
    list_javayez.append(jayeze_1_2)
    list_javayez.append(jayeze_2_1)
    list_javayez.append(jayeze_2_2)
    list_javayez.append(jayeze3_1)
    list_javayez.append(jayeze_3_2)
    list_javayez.append(jayeze_4_1)
    list_javayez.append(jayeze_4_2)
print(list_javayez)