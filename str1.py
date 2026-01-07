name="Hello world how is the day"

rev=" ".join(word[::-1] for word in name.split())
print(rev)

from collections import Counter
print(Counter(name))

dup={ch:ch for ch in name if name.count(ch)>1}
print("Duplocates are ",dup)
#Using Sets ddd
counts=Counter(name)
duplicates={ch: name.count(ch) for ch in set(name) if name.count(ch)>1}
print(duplicates)
#Using Collections Counter
counts=Counter(name)
duplii={ch:cnt for ch,cnt in counts.items() if cnt>1 }
print(duplii)
rname="Orrrangee"
result="".join(dict.fromkeys(rname))
print("removed duplicates chars: ",result)
