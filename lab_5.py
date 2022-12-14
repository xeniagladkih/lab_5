from tkinter import filedialog
from tkinter import Tk
import os
import json
import pandas as pd

Tk().withdraw()

def choose_file():
    filename = filedialog.askopenfilename(
            title="Choose a file",
            filetypes=(("All Files", "*.*"),
                        ("JSON Files", "*.json"))
            )
    return filename

def read_file(path):
    with open (path, "r") as f:
        temp = json.load(f)
        df = pd.DataFrame.from_dict(pd.json_normalize(temp), orient='columns')
        print(df)

def add_data(path):
    item_data = {}
    with open (path, "r") as f:
        temp = json.load(f)

    company = item_data["company"] = input("Company: ")
    city = item_data["city"] = input("City: ")
    name = item_data["name"] = input("name: ")
    designation = item_data["designation"] = input("Designation: ")
    age = item_data["age"] = input("Age: ")
    salary = item_data["salary"] = input("Salary: ")

    temp.append({"company": company, "city": city,"info":{"name": name, "designation": designation, "age": int(age), "salary": int(salary)}})

    with open(path,"w") as f:
        json.dump(temp, f, indent = 4)

def edit_data(path):
    read_file(path)
    new_data = []
    with open (path, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("\nWhich index number would you like to edit?")
    edit_option = input(f"\nSelect a number 0-{data_length} ")
    i=0
    for entry in temp:
        if i == int(edit_option):
            company = entry["company"]
            city = entry["city"]
            name=entry["info"]["name"]
            designation=entry["info"]["designation"]
            age=entry["info"]["age"]
            salary=entry["info"]["salary"]

            print(f"\nCurrent Company : {company}")
            print("You can not change company")

            print(f"\nCurrent City : {city}")
            print("You can not change city")

            print(f"\nCurrent Name : {name}")
            name=input("What would you like the new name to be? ")

            print(f"\nCurrent Designation : {designation}")
            designation=input("What would you like the new designation to be? ")

            print(f"\nCurrent Age : {age}")
            print("You can not change age")

            print(f"\nCurrent Salary : {salary}")
            specialty=input("What would you like the new salary to be? ")

            new_data.append({"company": company, "city": city,"info":{"name": name, "designation": designation, "age": int(age), "salary": int(salary)}})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open(path,"w") as f:
        json.dump(new_data,f,indent=4)

def delete_data(path):
    read_file(path)
    new_data = []
    with open (path, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("\nWhich index number would you like to delete?")
    delete_option = input(f"Select a number 0-{data_length}: ")
    i=0
    for entry in temp:
        if i == int(delete_option):
            pass
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open(path,"w") as f:
        json.dump(new_data,f,indent=4)

def save_file(path):
    with open (path, "r") as f:
        temp = json.load(f)
    out_file = open("myfile.json", "w")
    json.dump(temp, out_file, indent = 4)
    out_file.close()
        
def main():
    print("-----------------------------------------------")
    print("           JSON File Manager")
    print("-----------------------------------------------")

    choice = input("Do you want to open a file? y/n: ")

    if choice == "y":
        file = choose_file()
        os.startfile(file)
    else:
        exit()

    while True:
        print("\nEnter one of the following options to continue:")
        print("1 - Read a file (Deserialization)")
        print("2 - Edit Data")
        print("3 - Add Data")
        print("4 - Delete Data")
        print("5 - Save Data in a file (Serialization)")
        print("6 - Exit")

        options = [i for i in range(1, 7)]
        choice = ""
        while choice not in options:
            choice = int(input("\nEnter your choice (1-6): "))

            if choice == 1:
                read_file(file)
            elif choice == 2:
                edit_data(file)
            elif choice == 3:
                add_data(file)
            elif choice == 4:
                delete_data(file)
            elif choice == 5:
                save_file(file)
            elif choice == 6:
                exit()
            else:
                print("You did not select a number, please read more carefully.")

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)

        cont = input("Enter q to quit:")
        if cont == "q":
            break