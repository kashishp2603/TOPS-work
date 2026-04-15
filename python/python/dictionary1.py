student_data ={
    "sem1" :{"name" : "nandini",
    "marks" : [160,180,170] },
    "sem2" : {"name" : "kashish",
    "marks" : [180,190,170] },
    "sem3" : {"name" : "divya",
    "marks": [120,20,30]},
    "sem4" : {"name" : "sneha",
    "marks": [150,160,170]}
} 

for k,v in student_data.items():
    total=0
    for i in v["marks"]:
        total+=i
    print(f"{v['name']} has total marks {total}")
   
 
   