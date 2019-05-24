#!/usr/bin/python -u

from sys import stdin, stdout, stderr


def run():
    data = stdin.readline()
    stdout.write("OK\tDumb pipe\n")
    stdout.flush()

    while True:
        data = stdin.readline().strip()
        stderr.write(data + "\n")
        kind, qname, qclass, qtype, id, ip = data.split("\t")

        if (qtype == "SOA"):
            response = "DATA\t{qname}\t{qclass}\tSOA\t86400\t-1\t pdns.example.com\t hostmaster.example.com\t 123456 1800 3600 604800 3600\n".format(
                qname=qname,
                qclass=qclass)
            stdout.write(response)

        if (qname == "_tcp.example.com" and qtype == "ANY"): 
            for i in xrange(1, 1000):
                server = "w{i}.example.com".format(i=i)

                content = "{priority}\t{weight} {port} {target}".format(
                    priority=5000,
                    weight=5000,
                    port=8080,
                    target=server)

                response = "DATA\t{qname}\t{qclass}\tSRV\t{ttl}\t-1\t{content}\n".format(
                    qname=qname,
                    qclass=qclass,
                    ttl= 60,
                    content=content)
                stderr.write(response)
                stdout.write(response)     

        stdout.write("END\n")
        stdout.flush()

if __name__ == "__main__":
    run()