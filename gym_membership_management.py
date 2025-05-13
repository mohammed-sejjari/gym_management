#--Gym_membership_management--
#-----------------------------

import time
import os

#--function for clear screen--

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#--Function for create object for members
class Member():
    def __init__(self,f_name,l_name,membership_id,status):
        self.f_name = f_name
        self.l_name = l_name
        self.membership_id = membership_id
        self.status = status

    def display_member(self):
        print(f"\nFirst Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"Membership ID: {self.membership_id}")
        print(f"Membership Status: {self.status}")
        print("-" * 24)
        
        
#--Function for cearte list of members
def create_member():
    clear_screen()
    f_name = input("\nEnter first name: ")
    l_name = input("Enter last name: ")
    membership_id = input("Enter membership ID: ")
    status = input("Enter membership status, or click enter: ")
    if not status :
        status = "inactive"
    print("\nMember added successfully!")
    time.sleep(2)
    
    return Member(f_name,l_name,membership_id,status)

#--function of search


def search_member(members):
    clear_screen()
    print("\nSearch by:")
    print("\n1. Membership ID")
    print("2. First Name")
    print("3. Membership Status")

    choice = input("\nEnter your choice: ")
    found_members = []
    if choice == "1":
        id = input("\nEnter the membership ID to search: ")
        for x in members:
            if x.membership_id == id:
                found_members.append(x)
                break
        
    elif choice == "2":
        first_n = input("\nEnter the first name: ")
        for x in members:
            if x.f_name.lower() == first_n.lower():
                found_members.append(x)

    elif choice == "3":
        status = input("\nEnter the membership status to search(active/inactive): ")
        for x in members:
            if x.status.lower() == status.lower():
                found_members.append(x)

    if found_members:
        clear_screen()
        print("Members found displaying...")
        time.sleep(1)
        for x in found_members:
            x.display_member()
        time.sleep(4)
    else:
        print("\nMember not found!")
        time.sleep(2)



members = []
#--loop system--
while True:
    clear_screen()
    print("\nWelcome to Gym Membership Management")
    print("\n\nChosse an Action:")
    print("\n1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        # create_member()
        members.append(create_member())

    elif choice == "2":
        if members:
            clear_screen()
            print("\nDisplaying all members...")
            time.sleep(1)
            for x in members:
                x.display_member()
            time.sleep(2)
        else:
            print("\nSorry, didn't find any member to display.!!")
            time.sleep(1)

    elif choice =="3":
        if members:
            search_member(members)

        else:
            print("\nSorry, i didn't find any member to search.!!")
            time.sleep(2)

    elif choice == "4":
        print("\nExiting...")
        time.sleep(0.5)
        break
