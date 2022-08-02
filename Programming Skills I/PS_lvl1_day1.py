
## 1
low = 3
high = 7

#Slow
l_oddvalues = []
for value in range(low, high+1):
    if value % 2 != 0:
        l_oddvalues.append(value)

#Know that the substraction of 2 number is a pair number then there is : nb_pair_values = nb_odd_values

sub = high - low
if sub % 2 == 0:
    return sub/2
return int(sub/2) +1

# final
return (high-low)//2+max(low%2,high%2)

## 2
salary = [4, 4, 32, 21, 32, 43, 47]

max = max(salary)
min = min(salary)
salary.remove(max)
salary.remove(min)
average = sum(salary) / len(salary)
return average

# smart slicing
salary.sort()
salary_final = salary[1:len(salary)-1]
return sum(salary_final)/len(salary_final)
