English = {'p1','p2','p5','p6','p8',}
sinhala = {'p2','p3','p4','p7','p8',}
Tamil = {'p1','p4','p8','p9',}

#Question 2 Answers

#1
print(English & sinhala & Tamil)

#2
print(English - (sinhala | Tamil))

#3
print ((Tamil | sinhala) - English)

#4
a = (Tamil | sinhala | English)
print(len(a))