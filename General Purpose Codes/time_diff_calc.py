#Time Difference Calculator

#Values given as "day hour minute seconds" 

#Total seconds in a day
tot_sec_day = 24*60*60

# Assumption: x2 > x1
def time_diff(d1, h1, m1, s1, d2, h2, m2, s2):

    tot_sec_d1 = (d1*tot_sec_day) + h1*60*60 + m1*60 + s1
    tot_sec_d2 = (d2*tot_sec_day) + h2*60*60 + m2*60 + s2

    diff = tot_sec_d2 - tot_sec_d2

    #result
    d3 = int(diff / tot_sec_day)
    h3 = int((diff % tot_sec_day) / 60*60)
    m3 = int(((diff % tot_sec_day) % 60*60) / 60)
    s3 = int(diff % 60)

    print(f'{d3} {h3} {m3} {s3}')

