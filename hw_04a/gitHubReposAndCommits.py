import requests
import json
from brand import my_brand

my_brand("HW 04a - Develop with the Perspective of the Tester in mind")
#Function for getting gitHub username as input
def gitHubUsernameInput():
    username_input = input("Enter the username for gitHub: ")
    return username_input

#Function for getting response from gitHub repos fetching API     
def responseFromGitHubAPIForRepoAndCommits(gitHubUsername):
    #Initialing declared variables
    repoList = []
    numberOfCommit = 0
    numberOfCommitForEachRepo = {}

    #Hitting all the repo details fetching API
    api_url_repo = "https://api.github.com/users/"+gitHubUsername+"/repos"
    responseOfGitHubRepoAPI = requests.get(api_url_repo)
    if responseOfGitHubRepoAPI.status_code == 200:
        responseOfGitHubRepoAPIJson = responseOfGitHubRepoAPI.json()
        for repo in responseOfGitHubRepoAPIJson:
            #Getting the name of all the repos for the input username
            repoList.append(repo['name'])
        #return responseOfGitHubRepoAPI.status_code
    
    #Fetching the number of commits for each repo
    for repoName in repoList:
        api_url_commits = "https://api.github.com/repos/"+gitHubUsername+"/"+repoName+"/commits"
        responseOfGitHubCommitsAPI = requests.get(api_url_commits)
        if responseOfGitHubCommitsAPI.status_code == 200:
            numberOfCommit = len(responseOfGitHubCommitsAPI.json())
            numberOfCommitForEachRepo[repoName] = str(numberOfCommit)
            print("Repo: "+repoName+" Number of Commits: "+str(numberOfCommit))
        if numberOfCommit>0:
            numberOfCommitFlag = True
            #return responseOfGitHubCommitsAPI.status_code
    return responseOfGitHubRepoAPI.status_code, responseOfGitHubCommitsAPI.status_code, numberOfCommitFlag
    
    #for key, value in numberOfCommitForEachRepo.items():
        #print("Repo: "+key+" Number of Commits: "+value)


#Calling the functions
#gitHubUsername = gitHubUsernameInput()
#responseFromGitHubAPIForRepoAndCommits(gitHubUsername)
my_brand("HW 04a - Develop with the Perspective of the Tester in mind")
