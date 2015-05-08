from fabric.tasks import Task
from fabric.api import env, run, cd

def deploy_from_requirements():
    run("sed -n '/# development*/q;p' " + env["project_path"] + "requirements.txt > requirements_prod.txt") #remove dev dependencies
    run(env["virtualenv_path"] + "bin/pip install -r requirements_prod.txt")
    run("rm requirements_prod.txt")
    run("touch " + env["restart_trigger"])

def deploy():
    with cd(env["project_path"]):
        run("git pull origin master")
        
    run("rm -rf " + env["virtualenv_path"])
    run("virtualenv " + env["virtualenv_path"])
    deploy_from_requirements()
    