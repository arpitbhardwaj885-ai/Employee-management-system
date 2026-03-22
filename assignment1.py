Emp_data={}
def add_employee():
        empid=int(input("emp_id: "))
        name=input("name: ")
        age=int(input("Enter the age: "))
        department=input("department: ")
        if empid in Emp_data:
            print("Already exists")
        else:
            Emp_data[empid]={"Name":name,
                             "age":age,
                             "department":department}
            print("Employee added successful")

def view():
     if not Emp_data:
          print("NO employee available")
     else:
        print(Emp_data)
def search():
     id=int(input("Enter the id to search: "))
     if id in Emp_data:
          print(Emp_data[id])
     else:
          print("Employee not found")
            
while True:
    print("1.Add Employee")
    print("2.View All Employees")
    print("3.Search for Employee")
    print("4.Exit")
    task=int(input("Enter the choice:"))
    if task==1:
        add_employee()
    elif task==2:
         view()
    elif task==3:
         search()
    elif task==4:
        print("Thank you")
        break    
    else:
         print("Invalid number")
    

