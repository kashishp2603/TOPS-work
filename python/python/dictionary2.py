emp_data ={
    "sem1" :{"name" : "nandini",
    "salary" : 23000 ,"incentive": [5000,6000,7000]},
    "sem2" : {"name" : "kashish",
    "salary" : 25000 ,"incentive": [7000,6000,8000]},
    "sem3" : {"name" : "divya",
    "salary" : 22000,"incentive" : [3000,6000,5000]},
    "sem4" : {"name" : "sneha",
    "salary" : 24000,"incentive" : [5000,8000,2000]}
} 

for k,v in emp_data.items():
    total= 0

    for i in v["incentive"]:
        total+=i
    print(f"{v['name']} has total incentive {total}"),

    #for i in v["salary"]:
       # total+=i
   # print(f"{v['name']} has total salary {total}")
