# Py-Fi - Simple Vulnerable Python Server
A simple python HTTP server made from the ground up. To make this a bit harder, I decided to implement multithreading & logging as well!
This server is vulnerable to an extremely simple exploit.

## Old Purpose
This repo is for me to learn the basics of HTTP a little better. Credit to João Ventura (https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842) for hosting a fantastic blog to help!

## New and Improved Purpose
The same as before, but with added malice! (Red team always wins)

### Objectives
A list of objectives/"things" I found valuable:
- Building a simple HTTP server from python to learn sockets, basic HTTP, and basic programming
- Pentesting the server with tools like burpsuite
    - Being able to see the back-end or "Blue team" side of a pentest
        - Specifically, seeing how manual testing differs in network traffic than vulnerability scanning
    - Logging the attacks in a simple text file
- Provide an open source and secure way of running this lab
- Analyze the source code and explain why it's vulnerable

## Setup
If you want to go in and manually test this lab, I have added a DEPLOY.md file. Since running the file locally will result in a vulnerable service running on your host machine, I have dockerized the server!

Simple setup: (for Linux, duh)
```
cat DEPLOY.md | sudo sh
```

## Conclusion
As of updating this GitHub, I have completed this project and only need to format a report with a full description of the vulnerability and detecting it manually vs using an automated scanner. To complete this project, I used Python, Docker, and some Linux Fu to make it more interesting. Report coming soon!
