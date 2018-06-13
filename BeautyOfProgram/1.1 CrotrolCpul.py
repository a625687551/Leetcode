# coding: utf-8
import time

def run():
    for i in range(1000):
        for j in range(168000000):
            time.sleep(1/100)

run()