from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint
import time
from bs4 import BeautifulSoup
from cf.forms import *
import lxml.html as lh
import pandas as pd
from django.contrib.sites import requests
import requests, bs4, csv, json, time
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import matplotlib
import numpy
import json
from django.urls import reverse
from collections import Counter


def home(request):

    if request.method == "POST":
        print(request.POST)

        if 'search' in request.POST:
            return HttpResponseRedirect('/cf/'+str(request.POST['search']))
        elif 'name1' in request.POST:
            return HttpResponseRedirect('https://codeforces.com/profile/'+str(request.POST['name1']))
        elif 'name2' in request.POST:
            return HttpResponseRedirect('https://www.codechef.com/users/'+str(request.POST['name2']))
        elif 'name3' in request.POST:
            return HttpResponseRedirect('https://atcoder.jp/users/'+str(request.POST['name3']))

    url = 'https://codeforces.com/contests'
    response = requests.get(url)
    doc = lh.fromstring(response.content)
    tr_elements = doc.xpath('//tr')
    cf_con_list = []
    for i in tr_elements[1:]:
        c1 = i[0].text_content()
        t1 = i[2].text_content()
        if c1 == 'Name':
            break
        else:
            cf_con_list.append({'con': c1, 'time': t1})

    url2 = 'https://www.codechef.com/contests'
    response2 = requests.get(url2)
    doc = lh.fromstring(response2.content)
    tr_elements2 = doc.xpath('//tr')
    soup2 = bs4.BeautifulSoup(response2.text, "html.parser")
    result2 = soup2.find_all('tr')
    chef_list = []
    p = 0
    for i in result2[2:20]:
        s = i.text.split('\n')
        t = []
        u = {}
        for j in s:
            if j != '':
                t.append(j)

        if t[0].strip() == 'CODE':
            p += 1
        if p == 2:
            break
        if p == 1:
            u['code'] = t[0]
            u['org'] = t[1]
            u['st'] = t[2]
            chef_list.append(u)
            # print(u)

    chef_list = chef_list[1:]
    # print(chef_list)

    url3 = "https://atcoder.jp/contests/"
    response3 = requests.get(url3)
    soup3 = bs4.BeautifulSoup(response3.text, "html.parser")
    result3 = soup3.find("div", {"id": "contest-table-upcoming"})
    table3 = result3.find("table", {"class": "table table-default table-striped table-hover table-condensed "
                                             "table-bordered small"})
    atcoder_list = []
    for row in table3.findAll("tr"):
        dic = [0, 0, 0, 0]
        dic2 = {}
        all_col = row.findAll("td")
        if len(all_col) == 0:
            continue
        i = 0
        for da in all_col:
            dic[i] = da.text
            i += 1
        # print(dic)
        s = dic[0].split('+')
        dic[0] = s[0]
        dic2['con'] = dic[1]
        dic2['time'] = dic[0]
        atcoder_list.append(dic2)

    return render(request, 'main.html',
                  {'cf_con_list': cf_con_list, 'chef_list': chef_list, 'atcoder_list': atcoder_list})
