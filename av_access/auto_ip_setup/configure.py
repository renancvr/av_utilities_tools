import pandas as pd
import sys
import os
import time

file_path = sys.argv[1]

df = pd.read_excel(file_path)

ips = df.values.tolist()


for ip in ips:

    old_ip_addr = ip[0]
    new_ip_addr = ip[1]

    print(f"Changing ip {old_ip_addr} to {new_ip_addr}")
    for i in range(50):
        print('#', end='',flush=True)
        time.sleep(0.03)
    print('\n')


    os.system(f"python telnetclient.py {old_ip_addr} {new_ip_addr}")
