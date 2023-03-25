# celery-test

oc create -f celery-worker-beat.yaml

oc new-app --template celeryapp-template -p BRANCH_NAME=main -p APP_GIT_URL=https://github.com/torvicvasil1993/celery-test -p PROJECT_NAME=torvicvasil-dev -p APP_NAME=celery-worker-beat

