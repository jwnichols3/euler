"""
Test Results:
10 10 10 / 22
Test Passed

10 10 5 / 29

100 5 5 / 104
104 should equal 59

50 12 1 / 49
49 should equal 37

47.5 8 8 / 49
49 should equal 31
"""

def ecalc(i, j):
    return i - (i * j)

def evaporator(content, evap_per_day, threshold):
    print("---", content, evap_per_day, threshold, "---")
    threshold = content/threshold
    print("---", content, evap_per_day, threshold, "---")
    days = 0

    while (content > threshold) :
        content = ecalc(content, evap_per_day*.01)
        print(content)
        
        days = days + 1

    print("Days:",days)
    return days

evaporator(10, 10, 10)
evaporator(10, 5, 5)
evaporator(50, 12, 1)
evaporator(47.5,8,8)
#evaporator(10, 10, 10)
#evaporator(10, 10, 10)
#evaporator(10, 10, 10)

#s = 22111556677
#print(oddint(s))

#test.assert_equals(evaporator(10, 10, 10), 22)