records={"name":[],"English":[],"Maths":[],"Sciece":[]}
n=int(input("Enter number of students: "))

for i in range(1,n+1):
    print(f"enter details of student {i}")
    for key in records:
        if key=="name":
            records[key].append(input(f"enter {key} : "))
        else:
            records[key].append(int(input(f"enter {key} : ")))


#uncomment the next line for simple test
#records={"name":["abc","cat","xyz"],"English":[10,100,100],"Maths":[10,100,99],"Sciece":[10,100,99]}



def percentx( id ):
    "prints the percentage of the student with name"
    sum=0
    for key in records:
            if key != "name":
                sum+=records[key][id]

    Percent=sum/3 #3 is the total number of subjects
    name=records["name"][id]
    print(f"Percentage of {name} is {Percent}")

for i in range(n):
    percentx(i)

#prints the highest marks in easch subject along with name
for key in records:
    if key!="name":
        highz=max(records[key])
        idx=[i for i,x in enumerate(records[key]) if x ==(max(records[key]))]
        for i in idx:
            name=records["name"][i]
            print(f"Highest marks in {key} are {highz} of {name}")
