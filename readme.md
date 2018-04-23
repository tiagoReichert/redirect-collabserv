# Redirect any subdomain to collabserv

[![Build Status](https://travis-ci.org/tiagoReichert/redirect-collabserv.svg?branch=master)](https://travis-ci.org/tiagoReichert/redirect-collabserv)

###### Container created to redirect from any of your subdomain to https://mail.notes.na.collabserv.com

1. Point your subdomain to this container;
2. The container will redirect to https://mail.notes.na.collabserv.com.

This is a workaround because the collabserv doesn't support CNAME mapping directly from DNS


**Example:**

docker run -d -p 80:80 -v /etc/localtime:/etc/localtime:ro -e VIRTUAL_HOST=mail.lb2.com.br --name redirect-collabserv tiagoreichert/redirect-collabserv

- **-d:** Run in background
- **-p:** Expose port 80
- **--name:** Container name
- **VIRTUAL_HOST:** Used with jwilder/nginx-proxy for container reserve proxy


