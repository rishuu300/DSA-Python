from collections import deque

def generate(n):
    q = deque()
    q.append("5")
    q.append("6")

    for _ in range(n):
        curr = q.popleft()
        print(curr, end=" ")
        q.append(curr + "5")
        q.append(curr + "6")

    print()
    