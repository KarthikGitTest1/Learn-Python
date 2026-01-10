Tlist=[1,2,2,3,4,5,6,9,6,7,8,9,10]
Tlist[4]=16
# print(Tlist)
# Tlist.append(11)
# # Tlist.insert(2,'A')
# # Tlist.insert(20,'K')
# #print(Tlist[0:5])

# #print(Tlist)
# Tlist.remove(6)
# print(Tlist)
# pop_value=Tlist.pop(4)
# Tlist.extend([12,13])
# print(pop_value)
# print(Tlist)
# #Tlist.reverse()
# Tlist.sort()
# print(Tlist)
m_tuple=(1,2,3,4,5)
n_tp=(7,8,9)
#print(m_tuple[1:3])

# p_tp=m_tuple+n_tp
# print(p_tp)
# b_tp=(n_tp*3)
# n_tp[1]=10
# print(n_tp)
a_tp=(1,1.5,'Test','V')
a,b,c,d=a_tp
a=50
print(a,b,c,d)

model_dic={
        "Name":"Lingaiah",
        "Gender":"Male",
        "Height":167,
        "Weight":70,
        "Number":9182531460
}

print(model_dic["Name"])
print(model_dic)

my_set1=[1,1,1,2,2,2.5,2.2,2.2,3,4,5,6]
my_un=set(my_set1)
print(my_un)
my_un.add(7)
#print(my_un)
my_un.remove(1)
print(my_un)
if not 8 in my_un:
    print("Yes")

