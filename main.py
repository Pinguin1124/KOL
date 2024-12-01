C = int(input("Gib die Anzahl an C-Atomen in deinem Element ein ..."))
H = int(input("Gib die Anzahl an H-Atomen in deinem Element ein ..."))
C6 = C * 6
proton = C6 + H
neutron = C

g_proton = 1
g_neutron = 1
g_kern = proton + neutron
licht = 299792458

BE = ((proton * g_proton) + (neutron * g_neutron) - g_kern) * (licht * licht)

print("Die Bindungsenergie ist ...")
print(BE)

input("Enter zum beenden ...")