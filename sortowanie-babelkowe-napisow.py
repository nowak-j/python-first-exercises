# Napisz program, który pobierze ciąg napisów (zapisanych w jednej linii oddzielonych spacją) posortuje dany ciąg rosnąco, 
# (czyli od najmniejszego słowa do największego) używając do tego metody sortowania bąbelkowego.

ciąg_napisów = input().split()
index = 0
while index < (len(ciąg_napisów)-1):
    for j in range(len(ciąg_napisów)-1): 
        if ciąg_napisów[j] > ciąg_napisów[j+1]:
            tymczasowy_napis = ciąg_napisów[j]
            ciąg_napisów[j] = ciąg_napisów[j+1]
            ciąg_napisów[j+1] = tymczasowy_napis
    index += 1
print(*ciąg_napisów)