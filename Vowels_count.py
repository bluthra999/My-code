from os import read


def vowels_count(vowels):

    r = vowles.read()

    lowercase= r.lower()



    Vow_count = {}

    for i in lowercase:
        if  i == 'a' and i not in Vow_count :
            Vow_count[i] = 1
        elif  i == 'e' and i not in Vow_count :
            Vow_count[i] = 1
        elif  i == 'i' and i not in Vow_count :
            Vow_count[i] = 1
        elif  i == 'o' and i not in Vow_count :
            Vow_count[i] = 1
        elif  i == 'u' and i not in Vow_count :
            Vow_count[i] = 1
        elif i  in Vow_count: 
            Vow_count[i] += 1

    return Vow_count

vowles = open("Vowels.txt.txt", "r")
print(vowels_count(vowles))