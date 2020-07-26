creditnum = [4,2,3,1,3,7,3,3,1,7,8,0,3,3,0,6]
for i in reversed(range(len(creditnum))):
    if i%2==0:
        creditnum[i] = creditnum[i]*2
        credit = str(creditnum[i])
        if len(credit) >= 2:
            creditnum[i] = int(credit[0]) + int(credit[1])
a = sum(creditnum)
if a % 10 == 0:
    print("valid")
else:
    print("Not valid")
