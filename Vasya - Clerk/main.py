def tickets(people):
    fee = [people[0]]
    for i in range(1,len(people)):
        if people[i] == 25:
            fee.append(people[i])
            if i == len(people)-1:
                return "YES"
        elif people[i] == 50:
            if fee.count(25) >= 1:
                fee.remove(25)
                fee.append(50)
                if i == len(people)-1:
                    return "YES"
            else:
                return "NO"
        elif people[i] == 100:
            if fee.count(50) == 0 and fee.count(25) >= 3:
                for _ in range(3):
                    fee.remove(25)
                fee.append(100)
                if i == len(people)-1:
                    return "YES"
            if fee.count(25) >= 1 and fee.count(50) >= 1:
                fee.remove(25)
                fee.remove(50)
                fee.append(100)
                if i == len(people)-1:
                    return "YES"
            else:
                return "NO" 

print(tickets([25, 25, 50])) # return YES
print(tickets([25, 10])) # return No