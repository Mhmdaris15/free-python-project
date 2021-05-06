# nest = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     nest.append([name,score])

# scores = [i[1] for i in nest]
# scores.sort(reverse=True)
# last = []
# for i in nest:
#     if (i[1] == scores[-2]):
#         last.append(i[0])

# last.sort()
# for i in last:
#     print(i)

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))