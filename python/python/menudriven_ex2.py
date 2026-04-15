emp_data={
    101:{"name":"kashish","email":"kashish@gmail.com","salary":27000,"city":"ahmedabad"},
    102:{"name":"riya","email":"riya@gmail.com","salary":26000,"city":"ahmedabad"},
    103:{"name":"divya","email":"divya@gmail.com","salary":24000,"city":"baroda"},
    104:{"name":"diya","email":"diya@gmail.com","salary":25000,"city":"jaipur"}
}

print(emp_data)

while True:

  print("1 Add Employee")
  print("2 Search Employee id")
  print("3 Display All Employee")
  print("4. Update Employee ")
  print("5. Delete")
  print("6. Search by Salary")
  print("7. Search by City ")
  print("8. Exit")

  choice=int(input("Enter choice "))

  match choice:
     case 1:
        emp_id=int(input("enter the employee id"));
        name=input("enter the name");
        email=input("enter the email");
        salary=int(input("enter the salary"));
        emp_data[emp_id]={"name":name,"email":email,"salary":salary}
        city=input("enter the city");
        emp_data[emp_id]={"name":name,"email":email,"salary":salary,"city":city}
        
        print(emp_data); 
      
     case 2:
         emp_id=int(input("enter the employee id"));
         for k,v in emp_data.items():
            if emp_id==k:
               for k1,v1 in v.items():
                  print(k1,v1)

     case 3:
         for k,v in emp_data.items():
            print(k)
            for k1,v1 in v.items():
                  print("\t",k1,v1);          
    
     case 4:
        
        emp_id=int(input("enter the employee id"));

        if emp_id in emp_data.keys():
          newsalary=int(input("enter the salary"));
          emp_data[emp_id]["salary"]=newsalary
        print(emp_data[emp_id])
        
     case 5:
        emp_id=int(input("enter the employee id"));
        del emp_data[emp_id]
        print("employee deleted")
        print(emp_data)
        
     case 6:
        newsalary=int(input("enter the salary"));

        for k,v in emp_data.items():
           if v["salary"] == newsalary:
              print(k,v)

     case 7:
        newcity=input("enter the city");

        for k,v in emp_data.items():
           if v["city"] == newcity:
              print(k,v)
                  
     case 8:   break          
          
                 
            