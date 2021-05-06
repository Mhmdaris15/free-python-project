# N = int(input())
# arr = []
# for i in range(N):
#     cmd = input().split()
#     if cmd[0] == 'insert':
#         arr.insert(int(cmd[1]), int(cmd[2]))
#     elif cmd[0] == 'print':
#         print(arr)
#     elif cmd[0] == 'remove':
#         arr.remove(int(cmd[1]))
#     elif cmd[0] == 'append':
#         arr.append(int(cmd[1]))
#     elif cmd[0] == 'sort':
#         arr.sort()
#     elif cmd[0] == 'pop':
#         arr.pop(-1)
#     elif cmd[0] == 'reverse':
#         arr.reverse()

l = []
for _ in range(int(input())):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != 'print':
        cmd += '(' + ','.join(args) + ')'
        eval('l.' + cmd)
    else:
        print(l)