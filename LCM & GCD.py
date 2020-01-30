# how to calculate LCM?
def lcm_calc(a,b,c,d):
    abcd=a*b*c*d
    z=abcd+1
    initial=[x for x in range(1,z)]
    lcm_list=[x for x in initial if x%a==0 and x%b==0 and x%c==0 and x%d==0]
    lcm=min(lcm_list)
    return lcm
print(lcm_calc(25,34,78,90))

# how to calculate GCD?
import math
print(math.gcd(23,78))