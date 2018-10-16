# dohq-teamcity
[![docs](https://img.shields.io/readthedocs/pip.svg)](https://devopshq.github.io/teamcity/)
[![build](https://travis-ci.org/devopshq/teamcity.svg?branch=master)](https://travis-ci.org/devopshq/teamcity)
[![pypi](https://img.shields.io/pypi/v/dohq-teamcity.svg)](https://pypi.python.org/pypi/dohq-teamcity)
[![license](https://img.shields.io/pypi/l/teamcity.svg)](https://github.com/devopshq/teamcity/blob/master/LICENSE)

`dohq-teamcity` is a Python package providing access to the JetBrains TeamCity server API.

## Installation
```
# Latest release
pip install dohq-teamcity

# Develop branch
git clone https://github.com/devopshq/teamcity
cd dohq-teamcity
python setup.py install
```


## Usage

```python
from dohq_teamcity import TeamCity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

# list all the projects
projects = tc.projects.get_projects()
# OR
# projects = tc.project_api.get_projects()
for project in projects:
   print(project)

# get the group with name = groupname
group = tc.group.get('name:groupname')
print(group)

# get the user with name = username
user = tc.user.get('username:devopshq')
print(user)

# create a new user and delete
from dohq_teamcity import User
new_user = User(name='New user', username='new_user')
new_user = tc.users.create_user(body=new_user)
new_user.delete()

# other way - create object, connect with exist instance and load it
import dohq_teamcity
bt = dohq_teamcity.BuildType(id='MyBuildTypeId', teamcity=tc)
bt = bt.read()
```

## What next?
See more examples and full documantation on page: https://devopshq.github.io/teamcity
