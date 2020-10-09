#coding: utf-8
import os
import git
import sys
import traceback
import shutil

def CloneRepository(remote_repository_path, local_repository_path):
    print "Cloning:", local_repository_path
    while True:
        try:
            git.Repo.clone_from(remote_repository_path, local_repository_path)
            break
        except Exception as exception:
            print traceback.format_exc()
            if os.path.exists(local_repository_path):
                shutil.rmtree(local_repository_path)
          
def PullRepository(remote_repository_path, local_repository_path):
    if not os.path.exists(local_repository_path):
        CloneRepository(remote_repository_path, local_repository_path)
    else:
        try:
            print "Start Load Local Repository:", local_repository_path
            local_repository = git.Repo(local_repository_path)
            print "Start Pull:", local_repository_path
            if local_repository.is_dirty():
                local_repository.index.checkout(force = True)
            origin = local_repository.remotes.origin
            origin.pull()
        except Exception as exception:
            print traceback.format_exc()
            if os.path.exists(local_repository_path):
                shutil.rmtree(local_repository_path)
            CloneRepository(remote_repository_path, local_repository_path)

assert len(sys.argv) == 3
remote_repository_path = sys.argv[1]
local_repository_path = sys.argv[2]
PullRepository(remote_repository_path, local_repository_path)