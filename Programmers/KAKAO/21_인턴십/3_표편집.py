class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    nodeLi = [Node() for _ in range(n)]

    for i in range(1, n):
        nodeLi[i-1].next = nodeLi[i]
        nodeLi[i].prev = nodeLi[i-1]

    curr = nodeLi[k]
    stack = []

    for st in cmd:
        if st[0] == 'U':
            x = int(st[2:])
            for _ in range(x):
                curr = curr.prev
        elif st[0] == 'D':
            x = int(st[2:])
            for _ in range(x):
                curr = curr.next
        elif st[0] == 'C':
            stack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if nodeLi[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    return answer