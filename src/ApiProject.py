import requests

print("\n \n This is a place where u can get the github data \n")

def Method():
    while(True):
        print("\n ~~~ options ~~~ \n 1.user data \n 2.repo data \n")
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
        
        print(f"\n user: {UName} \n \n")
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
            individual = input("\nwant to view individual repo [name of repo]")
            IndividualRepo(individual,UserName)
            return 1

    except Exception as err:
        print(f"\n Error {err}")

def IndividualRepo(repo, username):
    indRepo_url = f"https://api.github.com/repos/{username}/{repo}"

    try:
        res = requests.get(indRepo_url)
        if (res):
            print(f"~~~ {repo} ~~~")
            Languages(username, repo)
            Stars(repo, username)

    except Exception as err:
        print(f"\n error {err}")

def Languages(user,repo):
    Lang_url = f"https://api.github.com/repos/{user}/{repo}/languages"
    try:
        response = requests.get(Lang_url)
        if(response):
            print(f"\n~~~ lanuages used in {repo} ~~~")
            for Response in response:
                print("\n",Response)

    except Exception as err:
        print(f"\n error {err}")

def Stars(repo,name):
    star_url = f"https://api.github.com/repos/{name}/{repo}/stargazers"
    try:
        response = requests.get(star_url)
        if(response):
            res = response.json()
            print(f"\n~~~ stars of {repo} ~~~")
            for Response in res:
                print("\n",Response['login'])

    except Exception as err:
        print(f"\n error {err}")


Method()