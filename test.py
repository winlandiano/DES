import random

st = ""
for x in range(64):
    st = st + str(random.randint(0, 1))+", "
    if x % 8 == 0:
        st = st + "\n"
print(st)
