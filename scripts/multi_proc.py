#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess
import sys

NUM_PROCESSES = 2

def run_process(task_desc):
    p = subprocess.Popen(["./asset_conv"], stdin=subprocess.PIPE)
    p.communicate(input=task_desc.encode())



if __name__ == "__main__":
    pool = Pool(NUM_PROCESSES)

    queues = [ [] for i in range(NUM_PROCESSES) ]
    i = 0
    for line in sys.stdin:
        queues[i].append(line)
        i = (i + 1) % NUM_PROCESSES

    task_descs = []
    for q in queues:
        task_desc = '\n'.join(q)
        task_descs.append(task_desc)

    pool.map(run_process, task_descs)
    


