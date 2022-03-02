import subprocess
import platform


def netstat():
    with open('scanOutput.csv', 'w') as f:
        netScan = subprocess.run(['netstat', '-nafo'], stdout=f, text=True)
        f.close()

    print(netScan)
netstat()


