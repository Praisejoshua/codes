#defining a function
def changeme (mylist):
    mylist.append([1,2,3,4]);
    print("values inside the functions",mylist)
    return
#calling my functioin
mylist = [10,20,30];
changeme(mylist);
print("values outside the functions", mylist)