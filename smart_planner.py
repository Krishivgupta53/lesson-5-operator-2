print("===Smart school day planner===")
day=input( "What day is it ? (Monday to Sunday)").strip().capitalize()
weather=input("What is the weather ? (sunny/rainy/cloudy)").strip().lower()
homework=input("Is your homework done ? (yes/no)").strip().lower()

print()
print("=====Your plan for {day}=====")
print("-"*35)

#if elif else classify the day

if day in ("Saturday","Sunday"):
    print("day type   :Weekend -enjoy your free time")
elif day=="Monday":
    print("Day type   : first day of the week. Pack your weekly planner")
elif day=="Friday":
    print("Day type   :last day of school return library books ")
elif day==("Tuesday","Wednesday","Thursday"):
    print("Day type   : regular school days stay focused")
else:
    print("day not recognized please check the speelings")

#and operators sunny and homework done

if weather=="sunny" and homework=="done":
    print("after school  head to the park weather is good and homework is done")

#or operator check if the weather is rainy or weather is cloudy

if weather=="cloudy" or weather=="rainy":
    print("weather tip pack an umbrella it may get wet outside")

# not operator

if not (homework== "yes"):
    print("homework   :not done yet .Finish it before going out")

# Combining if elif else +or+and+not

if weather=="rainy" and not (homework== "yes"):
    print("best plan    : stay at home finish your homework.Watch your favorite film")
elif weather=="sunny" and homework=="yes" and  not (day in("Saturday","Sunday")):
    print("best plan     : all set .Ready for a great school day")
elif day in ("Saturday","Sunday") and( homework=="yes"):
    print("best plan   : weekend day and homework is done .Go out and have fun")
else:
    print("do it step by step .You have got this")

print()
print("planner complete")

