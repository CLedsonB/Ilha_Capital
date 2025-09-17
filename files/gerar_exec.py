import sys
from cx_Freeze import setup, Executable

build_exe_options = {
	'packages': ['os','time','random'],
	'includes': []
	}

setup (
	name = 'IlhaCapital',
	version = '0.5',
	description = 'Ganhe ou perca!!, compre e gaste em uma ilha',
	options = {'build_exe' : build_exe_options},
	executables = [Executable('ilha_capital.py')]
)
