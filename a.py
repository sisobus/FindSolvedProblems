#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import json
import datetime
import commands
import time
import sys

from utils import download_source
from optparse import OptionParser
from bs4 import BeautifulSoup

parser = OptionParser()
parser.add_option('-i','--id',default='hasul',
                help='acmicpc.net id',dest='id')
(options, args) = parser.parse_args(sys.argv[1:])
acmicpc_id = options.id

url = 'http://www.acmicpc.net/signin'
values = {
        'login_user_id' : 'javava',
        'login_password' : 'tkdrmsld123',
        'auto_login' : 'on',
        'next' : 'problem/1016',
        }
headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Connection' : 'keep-alive',
        }
(source,cookie_jar) =  download_source(url,values,headers,None)

url = 'http://www.acmicpc.net/user/'+acmicpc_id
(source,cookie_jar) = download_source(url,values,headers,cookie_jar)

soup = BeautifulSoup(source)
problem_info = soup.find(id='problem_info')

panel_bodys = problem_info.findAll('div','panel-body')
solved_problem_numbers = panel_bodys[0].findAll('span','problem_number')
solved_problem_titles  = panel_bodys[0].findAll('span','problem_title')

failed_problem_numbers = panel_bodys[1].findAll('span','problem_number')
failed_problem_titles  = panel_bodys[1].findAll('span','problem_number')

ans = {'solved':[],'failed':[]}
for i in xrange(len(solved_problem_titles)):
    problem_number = solved_problem_numbers[i].a.string
    problem_title  = solved_problem_titles[i].a.string
    ans['solved'].append({
        'problem_number':problem_number, 
        'problem_title':problem_title})

for i in xrange(len(failed_problem_titles)):
    problem_number = failed_problem_numbers[i].a.string
    problem_title  = failed_problem_titles[i].a.string
    ans['failed'].append({
        'problem_number':problem_number, 
        'problem_title':problem_title})

with open(acmicpc_id+'.json','w') as fp:
    fp.write(json.dumps(ans))
