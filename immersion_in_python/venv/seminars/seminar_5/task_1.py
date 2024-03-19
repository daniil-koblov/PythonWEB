s = "1/33/4/234/111"
v1, k1, k2, *v2 = map(int, s.split("/"))
print(ans := {k1: v1, k2: v2})