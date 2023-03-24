# celery-test

oc new-app --name=celery-workers https://github.com/torvicvasil1993/celery-test.git --strategy=docker

oc scale deployment celery-workers --replicas=3

