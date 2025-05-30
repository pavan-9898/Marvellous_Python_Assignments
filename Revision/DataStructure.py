def main():

    my_list=["apple","banana","orange"]
    print("Original List :",my_list)
    my_list.append("Grapes") 
    my_list.insert(1,"papaya")  # while inserting we need to provide index number inwhich position we waant to insert data .
    print(" List After Appending :",my_list)
    my_list1=["coconut","cherry"]
    my_list.extend(my_list1)
    print("List after extending :",my_list)
    my_list.remove("banana")
    print("List after removing  banana :",my_list)
    my_list.pop(3) # bydefault pop the last element if we not specify the index
    print("List after popped element :",my_list)
    print("Count in list is :",my_list.count("apple"))
    
    print("-------------------------------------------------------")

    my_tuple=(10,20,30,40,50)
    print("Original tuple is :",my_tuple)
    print("Fetching 3rd element in tuple :",my_tuple[3])
    print("Fetching last element in tuple :",my_tuple[-1])
    print("Slicing tuple:",my_tuple[1:3])
    print("Tuple Length :",len(my_tuple))


    my_set1={1,2,2,3,4,5,6,7}
    print(my_set1)
    my_set2={1,2,3,8,9,10}
    print(my_set1 | my_set2)  # Union
    print(my_set1 & my_set2)   #intersection
    print(my_set1-my_set2)    # difference

    my_set2.add(20)
    print(my_set2)

    print("--------------------------------------")


    my_dict={"name":"pavan","age":27,"Profession":"IT"}
    print(my_dict)
    print(my_dict["name"])
    my_dict["age"]=29
    print(my_dict)


if __name__ == "__main__":
    print()
    main()