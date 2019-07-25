from setuptools import setup, find_packages

execfile('ymod/version.py')

def params():
	name = 'ymod'  # This is the name of your PyPI-package.
	version = __version__
	# scripts = ['helloworld']  # The name of your scipt, and also the command you'll be using for calling it
	description = "A command line interface to read and manipulate YAML files. Based on python, distributed as pip."
	author = "Hai Dam"
	author_email = "haidv.ict@gmail.com"
	url = "https://github.com/naviat/ymod"
	# license = "proprietary"

	packages = find_packages()
	zip_safe = False # ?

	install_requires = [
		"PyYAML",
		"argparse"
	]

	entry_points = {
		"console_scripts": {
			"ymod = ymod.__init__:run"
		}
	}

	# non python files need to be specified in MANIFEST.in
	include_package_data = True

	return locals()

setup(**params())