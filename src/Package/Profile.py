import Package.ApiCall
import Package.Asci_art
import Package.Text
from tabulate import tabulate

def profile(Username):
    print(Package.Text.Designtext("P r o f i l e"))
    print(f"\n~~~ {Username}'s profile ~~~")
    Namereq(Username)
    following(Username)
    follower(Username)
    repoCount(Username)

def Namereq(user):
    try:
        response = Package.ApiCall.Apicall("users",user)
        if response:
            print("\n")
            print(response['login'])
            print(response['name'])
            print(response['company'])
            print(response['location'])
            print(response['bio'])
            res = (response['avatar_url'])
            Art = Package.Asci_art.Ascii_Art(res)
            print("profile Image: \n",Art)
            return

    except Exception as err:
        print(f"error {err}")

def following(user):
    following_count = 0
    Follow_list = []
    data = "Null"
    try:
        response = Package.ApiCall.Apicall("users",user,"","following")
        if response:
            print(f"\n{user} following: ")
            for Response in response:
                data = Response['login']
                if(data):
                    Follow_list.append(data)
                following_count += 1

            following_data = [["following", Follow_list],["count", following_count]]
            print(tabulate(following_data, headers=["following", "count"], tablefmt='plain'))
    except Exception as err:
        print(f"error {err}")

def follower(user):
    follower_count = 0
    Follower_list = []
    datas = "Null"
    try:
        response = Package.ApiCall.Apicall("users",user,"","followers")
        if response:
            print(f"\nfollowers of {user} : ")
            for Response in response:
                datas = Response['login']
                if datas:
                    Follower_list.append(datas)
                follower_count += 1

            follower_data = [["followers", Follower_list],["count", follower_count]]
            print(tabulate(follower_data, headers=["followers", "count"], tablefmt='plain'))
    except Exception as err:
        print(f"error {err}")

def repoCount(user):
    repo_Count = 0
    try:
        res = Package.ApiCall.Apicall("users",user,"","repos")
        if res:
            for Res in res:
                repo_Count += 1
        print(f"your repository: {repo_Count}")
    except Exception as err:
        print(f"error {err}")
