from tabulate import tabulate
import Package.ApiCall
import Package.Profile
import Package.Text

GitHub_name = Package.Text.Designtext("G i t h u b . p y")
def Main():
    while(True):
        print(f"\n \n {GitHub_name} \n")
        print("\n ~~~ options ~~~ \n 1.profile data \n 2.repo data \n")
        choice = int(input("enter your choice: "))
        Condition(choice)

def Condition(Choice):
    if (Choice == 1):
        userName = input("enter the Username (Git-Hub): ")
        print(f"\n user: {userName} \n \n")
        Package.Profile.profile(userName)
        return 1
    
    else:
        UName = input("enter the username of the repo-owner: ")

        if(UName == ""):
            print("enter the username and reponame !")
            return 0
        
        print(f"\nuser: {UName} \n \n")
        repoFinder(UName)

def repoFinder(UserName):
    try:
        repos = Package.ApiCall.Apicall("users",UserName,"","repos")
        print("~~~ Repositories ~~~ \n ")
        for Repo in repos:
            print(Repo['name'])
        individual = input("\nwant to view individual repo [name of repo]: ")
        if individual:
            IndividualRepo(individual, UserName)
            return 1
        return 1

    except Exception as err:
        print(f"\n Error {err}")

def IndividualRepo(repo, username):
    table_data = []

    try:
        Url = Package.ApiCall.Apicall("repos", username, repo)
        if (Url):
            branch = Url['default_branch']
            license = Url['license']
            if(license):
               table_data.append(["license", Url['license']])
               return 1
            
            print(f"\n~~~ {repo}[{branch}] ~~~")
            Languages(username, repo)
            Stars(repo, username)
            print("\n")
            table_data = [
                ["Created At", Url['created_at']],
                ["Updated At", Url['updated_at']],
                ["Pushed At", Url['pushed_at']],
                ["Language", Url['language']],
                ["size", Url['size']],
            ]
            print(tabulate(table_data, headers=["context", "data"], tablefmt="plain"))
            print(f"\n~~~ contributors of {repo} ~~~\n")
            contributors(username, repo)

    except Exception as err:
        print(f"\n error {err}")

def Languages(user,repo):
    try:
        response = Package.ApiCall.Apicall("repos",user,repo,"languages")
        if(response):
            print(f"\nlanuages used in {repo}: -")
            for Response in response:
                print(Response)

    except Exception as err:
        print(f"\n error {err}")

def Stars(repo,name):
    stars_count = 0
    namestars = "Null"
    nameArray =[]
    
    try:
        response = Package.ApiCall.Apicall("repos",name,repo,"stargazers")
        if(response):
            print(f"\n~~~ stars of {repo} ~~~")
            print("\n total stars: ")
            for Response in response:
                namestars = Response['login']
                if(namestars):
                    nameArray.append(namestars)
                stars_count+=1

            star_data_tabel = [["Username",nameArray],["stars",stars_count]]
            print(tabulate(star_data_tabel,  headers=["user", "starcount"], tablefmt='plain'))
    except Exception as err:
        print(f"\n error {err}")

def contributors(user,repo):
    Const_Data = []
    const_mainData = []
    try:
        resp = Package.ApiCall.Apicall("repos", user, repo, "contributors")
        if(resp):
            for response in resp:
                mainCont = response['login']
                if(mainCont):
                    const_mainData.append(mainCont)
                    Const_Data.append(["Contributor", const_mainData])
                Const_Data.append(["Contribution Count", response['contributions']])
            
            print(tabulate(Const_Data, headers=["context","data"], tablefmt='plain'))
            return 1
        
    except Exception as err:
        print(f"error {err}")


Main()