# USE THIS COMMAND
# TERMINAL > conda install -c conda-forge cx_freeze
# TERMINAL >python setup.py bdist_msi
# decompyle3 -o path_for_save filename.pyc filename.pyc ...
# RUN >msiexec /i "SMSAPI-1.009-amd64.msi" /L*V "log.txt"


from cx_Freeze import setup, Executable
import sys
import os
import shutil

# ALSO IN settings.xml
status = 'BETA'
application_name = 'SimpleCopy'
current_version = '1.0'
description_short = ''
description_long = ''

author = 'Mark LEWIS'
email = 'kingston.lewis@gmail.com.fr'
project_url = 'https://github.com/Quinkink'
project_download = 'https://github.com/Quinkink/releases'

product_guid = '5623cf9e-bfc3-4d4c-baec-13fc15402230'
upgrade_guid = 'cc172009-e909-471f-b52b-c4fb6c522684'

# DELETE PREVIOUS BUILDS
for folder in ('./build/bdist.win-amd64', './build/exe.win-amd64-3.8', './build/bdist.win32', './build/exe.win32-3.10'):
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(folder + " deleted")
    else:
        print(folder + " does not exist")

# MSI shortcut table
directory_table = [
    (
        "ProgramMenuFolder",
        "TARGETDIR",
        ".",
    ),
    (
        application_name + "ProgramMenuFolder",
        "ProgramMenuFolder",
        application_name,
    ),
]

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     application_name,  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]" + application_name.lower() + ".exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("ProgramMenuShortcut",  # Shortcut
     application_name + "ProgramMenuFolder",  # Directory_
     application_name,  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]" + application_name.lower() + ".exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    # ("ProgramMenuShortcut",  # Shortcut
    #  application_name + "ProgramMenuFolder",  # Directory_
    #  "ReadMe.txt",  # Name
    #  "TARGETDIR",  # Component_
    #  "[TARGETDIR]ReadMe.txt",  # Target
    #  None,  # Arguments
    #  None,  # Description
    #  None,  # Hotkey
    #  None,  # Icon
    #  None,  # IconIndex
    #  None,  # ShowCmd
    #  'TARGETDIR'  # WkDir
    #  ),
]

msi_data = {"Directory": directory_table,
            "Shortcut": shortcut_table}

# Dependencies are automatically detected, but it might need
# fine tuning.
build_Options = dict(packages=["models", "controllers", "views", "lib"],
                     include_files=["data", "src", "ReadMe.txt", "LICENSE"],
                     excludes=["asyncio", "concurrent", "ctypes", "distutils", "html",
                               "lib2to3", "logging", "test", "unittest", "xmlrpc"],
                     add_to_path=False,
                     include_msvcr=True,
                     optimize=2,
                     silent=True)

buildMSI_Options = dict(install_icon="src/app.ico",
                        target_name=application_name + '-' + current_version,
                        initial_target_dir=r'[ProgramFilesFolder]\%s' % application_name,
                        product_code="{" + product_guid + "}",
                        upgrade_code="{"+ upgrade_guid + "}",
                        data=msi_data)

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py',
               base=base,
               target_name=application_name.lower(),
               icon="src/app.ico",
               copyright="GNU/GPL")
]

classifiers = [
    'Development Status :: ' + status + ' ' + current_version,
    'Environment :: Windows GUI',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Topic :: Communications :: *'
]

setup(name=application_name,
      version=current_version,
      author=author,
      author_email=email,
      url=project_url,
      download_url=project_download,
      # about='A simple API interface for SMS',
      description=description_short,
      long_description=description_long,
      keywords=[],
      license='GNU GENERAL PUBLIC LICENSE',
      options=dict(build_exe=build_Options,
                   bdist_msi=buildMSI_Options),
      classifiers=classifiers,
      executables=executables)
