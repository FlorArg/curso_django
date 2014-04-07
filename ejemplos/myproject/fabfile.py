from fabric.api import *

env.user = 'gscalone'
env.home = "/home/%s" % env.user
env.project = 'myproject'
env.project_dir = '/home/{user}/websites/{project}'.format(**env)
env.venv_prefix = 'source /home/{user}/.virtualenvs/{project}/bin/activate'.format(**env)
env.hosts = ['192.241.235.13']
env.use_ssh_config = True

@task
def instalar_proyecto():

    # run('mkdir -p ~/websites/{project}'.format(
    #     **env))
    local('pip freeze >requirements.txt')
    put('requirements.txt',
        '~/websites/{project}/requirements.txt'.format(
        **env))
    run('mkvirtualenv {project}'.format(
        **env))
    with cd(env.project_dir):
        with prefix(env.venv_prefix):
            run('pip install -r requirements.txt')


@task
def runserver(puerto=8888):
    with cd(env.project_dir):
        with prefix(env.venv_prefix):
            run('python manage.py runserver 0:{}'.format(puerto))
    # put('.', '~/websites/{project}'.format(
    #     **env))


