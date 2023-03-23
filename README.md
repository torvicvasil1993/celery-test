# celery-test

oc new-app --name=celery-test https://github.com/torvicvasil1993/celery-test.git --context-dir=celery-test --strategy=docker

oc scale dc celery-test --replicas=3

