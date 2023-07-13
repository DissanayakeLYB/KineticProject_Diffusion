import math

#C_infinity = Equilibrium concentration of outer layer (or inner layer)
#C_note = initial concentration of extracellular
#t1 = time when the first concentration value is calculated
#t2 = time when the second concentration value is calculated
#C1 = extracellular concentration of K+ @ time t1
#C2 = extracellular concentration of K+ @ time t2

C_infinity = int(input("Equilibrium concentration : "))
C_note = int(input("Initital extracellular concentration of K+ : "))
t1 = input("Military time when the first concentration value is calculated (0000h) : ")
t2 = input("Military time when the second concentration value is calculated (0000h) : ")
C1 = float(input("Extracellular concentration of K+ at time t1 : "))
C2 = float(input("Extracellular concentration of K+ at time t2 : "))

def time_gap_calc(t1,t2):
    #hour gap calculation
    hour1 = int(t1[0:2])
    min1 = int(t1[2:4])
    
    #minutes gap calculation
    hour2 = int(t2[0:2])
    min2 = int(t2[2:4])

    #total time gap of concentration calculation
    hour_gap = (hour2 - hour1)
    min_gap = (min2 - min1)
    time_gap = (hour_gap * 60) + min_gap
    return time_gap


def find_k(C_infinity,C1,C2,time_gap):
    constant = -(1/time_gap)
    ln_func = math.log((C_infinity - C1)/(C_infinity - C2))

    #equation for k value
    ans = constant * ln_func
    return ans


def find_t(C_infinity,C1,k_val):
    constant = (1/k_val)
    ln_func = math.log((C_infinity - C1)/(C_infinity - C_note))

    #equation for time taken
    time_diff = constant*ln_func
    return time_diff


time_gap = time_gap_calc(t1,t2)
k_val = find_k(C_infinity,C1,C2,time_gap)
time = (find_t(C_infinity,C1,k_val))/60

time_hours = int(time)
time_minutes = int((time % 1) * 60)

print("The time since death is", time_hours , "hours and", time_minutes ,"minutes")
