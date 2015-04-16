#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import os
from bs4 import BeautifulSoup
import urllib
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i','--id',default='hasul',
        help='acmicpc.net id',dest='id')
(options, args) = parser.parse_args(sys.argv[1:])
acmicpc_id = options.id

fp = urllib.urlopen('https://www.acmicpc.net/user/'+acmicpc_id)
source = fp.read()
fp.close()

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
