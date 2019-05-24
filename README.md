# powerdns-repro 

```bash
docker build -t pdns:repro -f Dockerfile .
docker run -it --name powerdns --rm pdns:repro
docker exec -it powerdns /bin/sh

$ dig _tcp.example.com -t srv @127.0.0.1
...
```

