"""
Thanks to the effects of El Nino this year my holiday snorkelling trip was akin to being in a washing machine... Not fun at all.

Given a string made up of '~' and '_' representing waves and calm respectively, your job is to check whether a person would become seasick.

Remember, only the process of change from wave to calm (and vice versa) will add to the effect (really wave peak to trough but this will do). Find out how many changes in level the string has and if that figure is more than 20% of the string, return "Throw Up", if less, return "No Problem".

"""

def sea_sick(sea):
    l = len(sea)
    turb = 0
    w2 = sea[0]
    for w in range(1, l):
        if w2 != sea[w]:
            turb = turb + 1
        w2 = sea[w]
#    turblevel = turb/l
#    print (turblevel)
    if turb/l > .20:
        return "Throw Up"
    else:
        return "No Problem"

print(sea_sick("~"), "No Problem")
print(sea_sick("_~~~~~~~_~__~______~~__~~_~~"), "Throw Up")
print(sea_sick("______~___~_"), "Throw Up")
print(sea_sick("____"), "No Problem")
print(sea_sick("_~~_~____~~~~~~~__~_~"), "Throw Up")
print(sea_sick("~~~~~_~~~~"), "No Problem")

"""
Test.describe("Basic tests")
Test.assert_equals(sea_sick("~"), "No Problem")
Test.assert_equals(sea_sick("_~~~~~~~_~__~______~~__~~_~~"), "Throw Up")
Test.assert_equals(sea_sick("______~___~_"), "Throw Up")
Test.assert_equals(sea_sick("____"), "No Problem")
Test.assert_equals(sea_sick("_~~_~____~~~~~~~__~_~"), "Throw Up")
"""
