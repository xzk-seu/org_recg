
a = []
with open('noncompany_feature.txt','r') as f:
    for l in f.readlines():
        a.append(l)

a.sort()
with open('noncompany_feature.txt','w') as f:
    for l in a:
        f.writelines(l)
