def isIsomer(s, t):
    if len(set(s)) == len(set(t)):
        m = {}
        for i in range(len(s)):
            if m.get(s[i]):
                if m[s[i]] != t[i]:
                    return False
            else:
                m[s[i]] = t[i]
        return True
    return False

s = "foo"
t = "bar"
print(isIsomer(s, t))