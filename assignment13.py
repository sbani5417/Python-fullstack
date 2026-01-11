scores=[50,60,46,87,65]
total_score=0
for score in scores:
    total_score=total_score+score
avarage_score=total_score/len(scores)
above_avarage_count=0
for score in scores:
    if score >avarage_score:
        above_avarage_count=above_avarage_count+1
print(scores)
print(total_score)
print(avarage_score)
print(above_avarage_count)
