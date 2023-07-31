#!/bin/python3

import subprocess

print('''

[..                                  [.......                                          
[..                                  [..    [..               [..                      
[..         [..    [.... [..[..   [..[..    [..[..  [.. [.... [..        [..    [. [...
[..       [..  [..      [..  [.. [.. [.......  [..  [..[..    [. [.    [.   [..  [..   
[..      [..   [..    [..      [...  [..       [..  [..  [... [..  [..[..... [.. [..   
[..      [..   [..   [..        [..  [..       [..  [..    [..[.   [..[.         [..   
[........  [.. [...[........   [..   [..         [..[..[.. [..[..  [..  [....   [...   
                             [..     Don't Be So Lazy to Push Your Code on Git Repo!

Developed by Th3 BlackHol3
https://twitter.com/Th3BlackHol3_
https://www.linkedin.com/in/th3blackhol3/

Disclaimer: Imagine You Didn't Push Your Code and Found Next Day Your Device Crashed!

''')

def run_git_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr

# Pull latest changes from the remote repository
run_git_command('git pull')

# Initialize a new Git repository
run_git_command('git init')

# Add all files to the staging area
run_git_command('git add .')

# Get the commit message from the user
commit_message = input("Enter the commit message: ")

# Commit changes with the provided message
success, output = run_git_command(f'git commit -m "{commit_message}"')
if not success:
    print("Commit failed:", output)
    exit(1)

# Ask for the branch name to be created or modified (e.g., "main", "development", etc.)
branch_name = input("Enter the branch name: ")

# Rename the branch to the specified branch name (for newer versions of Git)
run_git_command(f'git branch -M {branch_name}')

# Check if the remote repository URL is already set
remote_url_command = "git remote get-url origin"
current_remote_url = run_git_command(remote_url_command)

# If the remote URL is not set, ask for it as input
if not current_remote_url:
    remote_url = input("Enter the remote repository URL: ")
    run_git_command(f'git remote add origin {remote_url}')

# Push changes to the remote repository
success, output = run_git_command(f'git push -u origin {branch_name}')
if success:
    print("Success: Code pushed to the remote repository.")
else:
    print("Error:", output)

