# 1
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
result1 = set(ips)

# 2
blocked = {"root", "admin", "test"}
blocked.add("hacker")
blocked.remove("test")
result2 = blocked

# 3
forbidden = {21, 22, 23, 25}
port = 22
result3 = "Порт запрещён" if port in forbidden else "Порт разрешён"

# 4
known = {"mal.com", "bad.net"}
new = {"bad.net", "xevil.org"}
result4 = new - known

# 5
white = {"alice", "bob", "root"}
black = {"root", "admin"}
result5 = white & black

# 6
A = {"CVE-1", "CVE-2"}
B = {"CVE-2", "CVE-3"}
result6 = A | B

# 7
admin = {"read", "write", "delete"}
user = {"read", "download"}
result7 = admin ^ user

# 8
all_passwords = ["123", "qwerty", "test", "123", "qwerty", "admin"]
blocked_pw = {"test"}
result8 = set(all_passwords) - blocked_pw

# 9
global_ips = {"10.0.0.1", "10.0.0.2", "192.168.1.1"}
local_ips = {"10.0.0.2", "10.0.0.3"}
local_ips.intersection_update(global_ips)
result9 = local_ips

# 10
logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
result10 = {cmd for cmd in logs if "debug" not in cmd}


"""
1. элементы множества уникальны и неупорядочены, доступ по индексу невозможен
2. нет, потому что элементы множества должны быть неизменяемыми
3. remove() выдаёт ошибку если элемента нет, discard() — не выдает
4. union() возвращает новое множество, оператор | делает то же самое, но в виде оператора
5. A ^ B возвращает симметрическую разность — элементы, которые есть только в одном из множеств
6. intersection_update() оставляет в множестве только элементы, которые есть и в другом множестве
7. модифицируют: add, remove, discard, pop, clear, update, intersection_update, difference_update
возвращают новое: union, intersection, difference, symmetric_difference
"""
