me = {}
me["이름"] = "김지안"
me["나이"] = "22살"
me["학번"] = "2021147xxx"
me["학과"] = "컴퓨터과학과"
me["생일"] = "20010608"

print(me)
print(len(me))
print()

del me["이름"]
del me["나이"] 
del me["학번"] 
del me["학과"]
del me["생일"]

print(me)
print(len(me))
print()

me =dict(이름="김지안", 나이="22살", 학번="2021147xxx", 학과 = "컴퓨터과학과", 생일="20010608")

print(me)
print(len(me))
print()

me.clear()
print(me)
print(len(me))