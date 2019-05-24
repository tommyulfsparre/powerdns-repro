FROM tcely/powerdns-server

RUN apk update && apk add -u python bind-tools

COPY pipe.py /usr/local/bin/pipe.py
COPY pdns.conf /etc/pdns/pdns.conf
EXPOSE 53/tcp 53/udp

ENTRYPOINT ["/usr/local/sbin/pdns_server", "--disable-syslog"]