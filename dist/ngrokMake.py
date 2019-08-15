import os
import sys

www = "robot86.top"


def writeCfg(tport):
    fname = "ngrok" + tport + ".cfg"
    fcontent = 'server_addr: "robot86.top:' + tport + '"'"\n"
    fcontent = fcontent + "trust_host_root_certs: false \n"
    print(fname)
    print(fcontent)
    f = open(fname, 'a+')
    f.write(fcontent)
    f.close()


if __name__ == '__main__':
    httpPort = sys.argv[1]
    httpsPort = sys.argv[2]
    TunnelPort = sys.argv[3]
    rootpath = os.path.abspath(os.path.dirname(os.getcwd()))
    ccmd = "screen cd " + rootpath + "/bin"
    cmd = "./ngrokd -domain=" + www + " -httpAddr=:" + httpPort + " -httpsAddr=:" + httpsPort + " -tunnelAddr=:" + TunnelPort
    cccmd = ccmd + " &&" + cmd
    rmfile = "sudo rm -rf *.cfg"
    os.system(rmfile)
    writeCfg(TunnelPort)
    os.system(cccmd)
