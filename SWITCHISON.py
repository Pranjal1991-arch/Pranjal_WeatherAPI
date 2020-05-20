fo = open("switch.txt", "r+")
status = int(fo.read(1))

if status == 1:

    switch_status = "ON"
    fo.seek(0)
    fo.write("0")
else:
    switch_status = "OFF"
    fo.seek(0)
    fo.write("1")
print(switch_status)
fo.close()
