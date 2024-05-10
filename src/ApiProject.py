import requests
from tabulate import tabulate
from pyfiglet import figlet_format

GitHub_name = figlet_format("G i t h u b . p y")
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
        return 1
    
    else:
        UName = input("enter the username of the repo-owner: ")

        if(UName == ""):
            print("enter the username and reponame !")
            return 0
        
        print(f"\nuser: {UName} \n \n")
        repoFinder(UName)

def repoFinder(UserName):
    RepoFinder_Url = f"https://api.github.com/users/{UserName}/repos"
    try:
        ApiRes = requests.get(RepoFinder_Url)
        if(ApiRes):
            repos = ApiRes.json()
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
    indRepo_url = f"https://api.github.com/repos/{username}/{repo}"

    try:
        res = requests.get(indRepo_url).json()
        if (res):
            branch = res['default_branch']
            license = res['license']
            if(license):
               table_data.append(["license", res['license']])
               return 1
            
            print(f"\n~~~ {repo}[{branch}] ~~~")
            Languages(username, repo)
            Stars(repo, username)
            print("\n")
            table_data = [
                ["Created At", res['created_at']],
                ["Updated At", res['updated_at']],
                ["Pushed At", res['pushed_at']],
                ["Language", res['language']],
                ["size", res['size']],
            ]
            print(tabulate(table_data, headers=["context", "data"], tablefmt="plain"))
            print(f"\n~~~ contributors of {repo} ~~~\n")
            contributors(username, repo)

    except Exception as err:
        print(f"\n error {err}")

def Languages(user,repo):
    Lang_url = f"https://api.github.com/repos/{user}/{repo}/languages"
    try:
        response = requests.get(Lang_url).json()
        if(response):
            print(f"\nlanuages used in {repo}: \n")
            for Response in response:
                print(Response)

    except Exception as err:
        print(f"\n error {err}")

def Stars(repo,name):
    stars_count = 0
    namestars = "Null"
    nameArray =[]
    
    star_url = f"https://api.github.com/repos/{name}/{repo}/stargazers"
    try:
        response = requests.get(star_url)
        if(response):
            res = response.json()
            print(f"\n~~~ stars of {repo} ~~~")
            print("\n total stars: ")
            for Response in res:
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
    Cont_url = f"https://api.github.com/repos/{user}/{repo}/contributors"
    try:
        resp = requests.get(Cont_url).json()
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