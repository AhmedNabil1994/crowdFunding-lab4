import re
import json
from itertools import count



 
print("welcome to Crowd -Funding app")
# print("-----------------------------")
class Human:
    def __init__(self, firstName, lastName, email, password, phoneNumber, projects=[]):

        self.firstName = firstName
        self.lastName =lastName
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.projects = projects


lastID = ""
with open("lastID.txt","r") as f:
    lastID = int(f.read())


class Project:
    _ids = count(lastID+1)
    def __init__(self, owner, title, details, target, startDate, endDate):
        self.owner     = owner
        self.title     = title
        self.details   = details
        self.target    = target
        self.startDate = startDate
        self.endDate   = endDate
        self.id        = next(self._ids)


def register():
        firstName = firstNameValidation()
        lastName  = lastNameValidation()
        email     = emailValidation()
        password  = passwordValidation()
        phoneNumber = phoneNumberValidation()


        user = Human(firstName, lastName, email, password, phoneNumber)
        userObject = user.__dict__

        userData(email, userObject)


def firstNameValidation() :

        firstName=input("Enter your first name:")
        while not (re.match("^[A-Za-z]{3,}$", firstName)) :
            return firstNameValidation()
        return firstName

def lastNameValidation() :

        lastName=input("Enter your last name:")
        while not (re.match("^[A-Za-z]{3,}$", lastName)) :
            return lastNameValidation()
        return lastName

def emailValidation() :

        email=input("Enter your email:")
        while not (re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})", email)) :
            return emailValidation()
        return email
        
def passwordValidation() :

        password = input("Enter Your Password : ")
        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -/:-@\[-`{-~]).{7,20}$", password):
            while True:
                confirmPassword = input("confirm Your Password : ")
                if confirmPassword == password:
                    break
                else:
                    print("Passwords don't match")
            return password
        else:
            print("Wrong Password")
        return passwordValidation()       
        
def phoneNumberValidation() :    
        
    phoneNumber=input("Enter your mobile phone:")
    while not (re.match("(201)[0-9]{9}", phoneNumber)) :
        return phoneNumberValidation()
    return phoneNumber 


def userData(userid, userObject) :
    data = {}
    with open("usersdata.json","r") as f:
        dataOld = json.load(f)
        dataOld[userid]=userObject
        data=dataOld

    with open("usersdata.json", "w") as f:
        json.dump(data, f)


def login() :
    data = {}
    with open("usersdata.json", "r") as f:
        data = json.load(f)

    email = input("Enter Your Email : ")
    try:
        userData = data[email]
        while True:
            userPassword = input("Enter your password : ")
            if userData["password"] == userPassword:
                print(f"Welcome {userData['firstName']} {userData['lastName']}")
                ownerName = f"{userData['firstName']} {userData['lastName']}"
                option   = input("1) View All Projects \n 2) Create Project \n 3) Edit Your Projects \n:" )
                if   option == "1":
                    viewAllProjects() 
                elif option == "2":
                    createProject(ownerName,userData)
                
                break
            else:
                print("Wrong Password .. try again")
    except KeyError:
        print('Email Not Found')
        option = input("1) To register type '1' \n 2) To Login type '2'\n : ")
        if option == "1":
            register()
        elif option == "2":
            login()
        else:
            print("Wrong Choice")


def viewAllProjects():
    with open("projects.json", "r") as f:
        projectData = json.load(f)
        for i in projectData :
            projectView = f"Project Title: {projectData[i]['title']} \n" \
                          f"Created by: {projectData[i]['owner']} \n" \
                          f"Target : {projectData[i]['target']}$ \n" \
                          f"From {projectData[i]['startDate']} to {projectData[i]['endDate']}$ \n" \
                          f"Details: {projectData[i]['details']}\n" \
            
            
            print(projectView)
        


def createProject(owner,user_dict):
    title     = input("Enter Ptoject title : ")
    details   = input("Enter project details : ")
    target    = input("Enter Project Targert : ")
    startDate = input("Enter the start date : ")
    endDate   = input("Enter the End Date : ")

    newProject = Project(owner, title, details, target, startDate, endDate)
    newProject_dict = newProject.__dict__

    updateProjectsData(newProject_dict["id"], newProject_dict)
    updateUserData(newProject_dict["id"], user_dict)

    with open("lastID.txt", "w") as f:
        f.write(str(newProject_dict["id"]))



def updateProjectsData(id , project_dict):
    data = {}
    with open("projects.json", "r") as f:
        dataOld = json.load(f)

        dataOld[id] = project_dict
        data = dataOld

    with open("projects.json", "w") as f:
        json.dump(data, f)
        
        
        
 
def updateUserData (id, user_dict):
    data = {}
    with open("usersdata.json", "r") as f:
        oldData = json.load(f)

        user_dict["projects"].append(id)

        userEmail = user_dict["email"]

        oldData[userEmail] = user_dict
        print("old After", oldData)
        data = oldData

    with open("usersdata.json", "w") as f:
        json.dump(data, f)       


def editProject(user_dict):
    projectIDs = user_dict["projects"]
    if len(projectIDs)==0:
        print("you have no projects")
    else:
        print("")








# register()
login()
# viewAllProjects()
