from fabric.api import run

import fablib
from fablib import init, deploy, rollback, before_init, before_deploy, before_rollback, after_rollback, after_deploy, after_init, clear


fablib.before_init.append(lambda: run('echo "hello from before init" >> hello.txt'))
fablib.before_deploy.append(lambda: run('echo "Hello from deploy" >> hello.txt'))
fablib.before_rollback.append(lambda: run('echo "Hello from rollback" >> hello.txt'))

fablib.after_init.append(lambda: run('echo "Bye from init" >> bye.txt'))
fablib.after_deploy.append(lambda: run('echo "Bye from deploy" >> bye.txt'))
fablib.after_rollback.append(lambda: run('echo "Bye from rollback" >> bye.txt'))


