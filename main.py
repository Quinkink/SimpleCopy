"""
Created on 17 Mar 2020

@author: Eleonore
"""

from controllers import applicationController
""":type: string"""
filename = 'settings.xml'

if __name__ == '__main__':
    app = applicationController.Application(filename)
    app.run()
