cmd_/home/seed/crypto-ns/lab5/netfilter/modules.order := {   echo /home/seed/crypto-ns/lab5/netfilter/seedFilter.ko; :; } | awk '!x[$$0]++' - > /home/seed/crypto-ns/lab5/netfilter/modules.order
