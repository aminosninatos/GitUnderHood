Python Virtual environments
---------------------------------------------------------------------------------
In your project direcoty we gonna create a folder env:
1- To use it: ~> python3 -m venv env
2- To activate it: ~> source env/bin/activate
3- To desactivate it: ~> deactivate 
4- To show packages with version in your env: ~> pip list
To work with that in vs code all you have to do is to reload your vs code 
then click in the botton left the python version and choose the one in env folder.


Pipenv
-----------------------------------------------------
the new way to use virtual environments
- Install pipenv: ~>pip3 install pipenv
- Activate: ~>pipenv shell
- Check version of Python:  ~>python --version
- Install a package: ~>pipenv install package_name
- Check local packages: ~>pipenv lock -r
- Uninstall a package: ~>pipenv uninstall package_name
- Install a dev package: ~>pipenv install package_name --dev



