"""

"""


#
def gradingStudents(grades):
    aux = resto = siguiente = 0
    for i in range(0,len(grades)):
        resto = grades[i] % 5
        #print(str(aux))
        if grades[i] >= 38 and resto > 0:
            aux = grades[i] // 5
            #print("aux:", str(aux))
            siguiente = (aux+1) * 5
            #print(str(grades[i]),":",str(siguiente))
            if siguiente - grades[i] < 3:
                grades[i] = siguiente

    return grades

