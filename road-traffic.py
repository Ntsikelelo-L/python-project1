Current_Speed = int(input("please enter speed in km/h"))
Average_Speed = int(input("please enter speed in km/h"))
calc = Current_Speed - Average_Speed
Demerits = calc//5
print("point: ", Demerits)
if (Demerits > 12):
    print("Time to go to Jail")
elif (0 <= Demerits <=12):
    print("OK")
