import unittest
from brand import my_brand
from gitHubReposAndCommits import gitHubUsernameInput, responseFromGitHubAPIForRepoAndCommits


my_brand_here = False
my_brand("HW 04a - Develop with the Perspective of the Tester in mind")
#gitHubUsername = gitHubUsernameInput()

class TestgitHubReposAndCommits(unittest.TestCase):
    #def setUp(self):
    #    self.gitHubUsername = gitHubUsername

    def test_repoResponseStatusCodeFailed(self):
        self.assertEqual(responseFromGitHubAPIForRepoAndCommits("pyadav6"), (200, 200, True), "Fetching the repositories failed")

    def test_commitResponseStatusCodeFailed(self):
        self.assertEqual(responseFromGitHubAPIForRepoAndCommits("pyadav6"), (200, 200, True), "Fetching the commit details for repositories failed")

    def test_numberOfCommits(self):
        self.assertEqual(responseFromGitHubAPIForRepoAndCommits("pyadav6"), (200, 200, True), "No commits found in the repository.")
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)

if not my_brand_here:
    my_brand("HW 04a - Develop with the Perspective of the Tester in mind")