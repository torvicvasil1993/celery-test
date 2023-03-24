from tasks import hello_world

for i in range(1000):
    hello_world.delay()
    
