from config.celery import app
import os

# app = Celery('tasks', broker="amqp://guest:guest@localhost:5672//", backend="redis://localhost:6379")
#
@app.task
def add(x,y):
    return x + y

#
# # result = add(4, 4)
# result = add.apply_async((4, 4))
# # print("Task ID:", result.id)
# #
# import time
# while not result.ready():
#     print("Waiting for task to complete... Current State:", result.state)
#     time.sleep(1)
#
# print("Final State:", result.state)
# print("Task Result:", result.get(timeout=10))