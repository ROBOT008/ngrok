import os
import sys

www = "robot86.top"

if __name__ == '__main__':
    httpPort = sys.argv[1]
    httpsPort = sys.argv[2]
    TunnelPort = sys.argv[3]
    cmd = "screen ./ngrokd -domain=" + www + " -httpAddr=:" + httpPort + " -httpsAddr=:" + httpsPort + " -tunnelAddr=:" + TunnelPort
    print(cmd)
    os.system(cmd)

