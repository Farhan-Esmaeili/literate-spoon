time = input("Please enter your time in hh:mm:ss type :") 
hour = int(time[0:2])
min = int(time[3:5])
sec = int(time[6:8])
t_sec = 3600*hour + 60*min + sec
print(t_sec)