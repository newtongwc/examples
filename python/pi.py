# This computes the Leibniz formula for pi
# pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...
# It is a very slowly converging series.
# 10000 terms gets us 3.141(wrong digits after)

one_fourth_pi = 0.0
for term in range(10000):
    denominator = 2*term + 1
    fraction = 1.0/denominator
    if term % 2 == 0:
        one_fourth_pi += fraction
    else:
        one_fourth_pi -= fraction
print 4*one_fourth_pi
