import math
sa = 0.0
arr = [-45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

itarray = [0.0] * 106

itarray2 = [0.0] * 90

max_radiation = 0.0

print("Enter the latitude angles in degrees")
l = float(input())
l1 = math.radians(l)

print("Enter the day in number")
N = float(input())
print("Enter S for south, N for north, E for east, and W for west facing")
sa0 = input().upper()
if sa0 == 'S':
    sa = 0.0
elif sa0 == 'N':
    sa = math.pi
elif sa0 == 'E':
    sa = -math.pi / 2
elif sa0 == 'W':
    sa = math.pi / 2 
t = math.pi / 2
ref = 0.6

d = math.radians(360 * (284 + N) / 365)
dd1 = 23.47 * math.sin(d)
d1 = math.radians(dd1)
fws1 = (1 + math.cos(t)) / 2
fwg1 = ref * (1 - math.cos(t)) / 2

fws = math.radians((1 + math.cos(t)) / 2)

fwg = math.radians(ref * (1 - math.cos(t)) / 2)
s2 = math.cos(math.radians(N * 360 / 365))
A = 1162.12 + (77.0323 * s2)

B = 0.171076 - (0.0348944 * s2)

C = 0.0897334 - (0.0412439 * s2)


for i in range(106):

    w = math.radians(arr[i])


    za2 = (math.cos(l1) * math.cos(w) * math.cos(d1)) + (math.sin(l1) * math.sin(d1))
    za1 = math.acos(za2)

    za = za1 - (math.pi / 2) if za1 > math.pi / 2 else za1
    
    inc2 = (math.cos(l1) * math.cos(t) + math.sin(l1) * math.sin(t) * math.cos(sa)) * (math.cos(d1) * math.cos(w)) + math.cos(d1) * math.sin(w) * math.sin(t) * math.sin(sa) + math.sin(d1) * (math.sin(l1) * math.cos(t) - math.cos(l1) * math.sin(t) * math.cos(sa))
    inc1 = math.acos(inc2)
    inc = inc1 - math.pi if inc1 > math.pi / 2 else inc1
    rb = math.cos(inc) / math.cos(za)
    IDN = A * (math.exp((0 - B) / math.cos(za)))
    Id = C * IDN
    Ib = IDN * math.cos(za)

    It = Ib * rb + Id * fws1 + (Ib + Id) * fwg1
    itarray[i] = It
    max_radiation = max(It, max_radiation)
    print(itarray[i])


print("Maximum radiation =", max_radiation)


for j in range(106):

    if max_radiation == itarray[j]:

        P = j


        w = math.radians(arr[P])

        TILTarr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
        23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
        
        45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
        67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
        89, 90]


for j in range(90):

    t = math.radians(TILTarr[j])


    za2 = (math.cos(l1) * math.cos(w) * math.cos(d1)) + (math.sin(l1) * math.sin(d1))
    za1 = math.acos(za2)

    za = za1 - (math.pi / 2) if za1 > math.pi / 2 else za1



    inc2 = (math.cos(l1) * math.cos(t) + math.sin(l1) * math.sin(t) * math.cos(sa)) * (math.cos(d1) * math.cos(w)) + math.cos(d1) * math.sin(w) * math.sin(t) * math.sin(sa) + math.sin(d1) * (math.sin(l1) * math.cos(t) - math.cos(l1) * math.sin(t) * math.cos(sa))
    inc1 = math.acos(inc2)
    inc = inc1 - math.pi if inc1 > math.pi / 2 else inc1
    rb = math.cos(inc) / math.cos(za)
    IDN = A * (math.exp((0 - B) / math.cos(za)))
    Id = C * IDN
    Ib = IDN * math.cos(za)

    It = Ib * rb + Id * fws1 + (Ib + Id) * fwg1
    itarray2[j] = It
    max_radiation = max(It, max_radiation)

    print(f"Radiation for {TILTarr[j]} degree tilt angle =", itarray2[j])
 
print("Maximum radiation =", max_radiation)


for j in range(90):

    if max_radiation == itarray2[j]:

        P = j


print(f"Maximum radiation of {max_radiation} is at tilt angle = {TILTarr[P]}")
