from collections import deque

member = deque(("adam", "najmi", "naja", "hadi"))
member.append("soya")  # type: ignore
member.appendleft("lara")  # type: ignore

print(member)

member.pop()
member.popleft()

print(member)
