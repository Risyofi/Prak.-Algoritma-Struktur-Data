from class_stackLL import StackLL

def cetakBiner(d):
    f = StackLL()
    if d == 0: f.push(0);
    while d != 0:
        sisa = d%2
        d = d // 2
        f.push(sisa)
    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    return st

print(cetakBiner(11))
print(cetakBiner(53))
