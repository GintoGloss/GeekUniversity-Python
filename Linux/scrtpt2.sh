#Изменить скрипт мониторинга лога, используя утилиту tailf, чтобы он выводил сообщения при попытке неудачной аутентификации пользователя /var/log/auth.log,
#отслеживая сообщения примерно такого вида:
#May 16 19:45:52 vlamp login[102782]: FAILED LOGIN (1) on '/dev/tty3' FOR 'user', Authentication failure

#!/bin/bash

msg="failure"

while true
do
        tail -n2 -f /var/log/auth.log | grep "$msg"
done
