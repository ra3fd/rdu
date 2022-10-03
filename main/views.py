
from django.shortcuts import render


import re
import random
import datetime
import time
from django.views.decorators.cache import cache_page
# import win32api

from .models import Entry
from .models import Cty


def base(request):
    return render(request, 'main/base.html', locals())


@cache_page(60)
def search(request):

    # win32api.LoadKeyboardLayout("00000409",1) # Переключение (?) раскладки клавиатуры

    t1 = time.time()

    # Заполнение таблицы 123 - 311 строчки

    qso_160cw = qso_80cw = qso_40cw = qso_30cw = qso_20cw = qso_17cw = qso_15cw = qso_12cw = qso_10cw = 0
    qso_160ssb = qso_80ssb = qso_40ssb = qso_20ssb = qso_17ssb = qso_15ssb = qso_12ssb = qso_10ssb = 0
    qso_160rtty = qso_80rtty = qso_40rtty = qso_30rtty = qso_20rtty = qso_17rtty = qso_15rtty = qso_12rtty = qso_10rtty = 0
    qso_160psk = qso_80psk = qso_40psk = qso_30psk = qso_20psk = qso_17psk = qso_15psk = qso_12psk = qso_10psk = 0
    qso_160ft4 = qso_80ft4 = qso_40ft4 = qso_30ft4 = qso_20ft4 = qso_17ft4 = qso_15ft4 = qso_12ft4 = qso_10ft4 = 0
    qso_160ft8 = qso_80ft8 = qso_40ft8 = qso_30ft8 = qso_20ft8 = qso_17ft8 = qso_15ft8 = qso_12ft8 = qso_10ft8 = 0

    qcw = Entry.objects.filter(mode='CW')
    qssb = Entry.objects.filter(mode='SSB')
    qrtty = Entry.objects.filter(mode='RTTY')
    qpsk = Entry.objects.filter(mode='PSK')
    qft4 = Entry.objects.filter(mode='MFSK')
    qft8 = Entry.objects.filter(mode='FT8')


    if 'q' in request.GET and request.GET['q']:

        data = request.GET['q']

        if re.match(r'[\w/]{4,18}|\D\d\D$', data):
            # if re.match(r'^(.+/)?%s(/.+)?$' % data, data):

            q1 = Entry.objects.filter(callsign__iregex=r'^(.+/)?%s(/.+)?$' % data).order_by('-datetime')
            qso = q1.count()

            dupe = []  #
            no_dupes_qso = []  # Band+mode - not dupes!

            for entry in q1:
                if str(entry.band) + str(entry.mode) not in dupe:
                    dupe.append(str(entry.band) + str(entry.mode))
                    b = int(entry.id)
                    no_dupes_qso.append(b)

            q2 = q1.filter(id__in=no_dupes_qso)  # Фильтр: no dupes band-mode qso

            if qso == 1 or qso == 0:
                qso_qsos = 'QSO'
            else:
                qso_qsos = 'QSOs'

            if qso:  # Если есть связь (связи)

                q_160 = q1.filter(band='2')
                if q_160:
                    qso_160cw = q_160.filter(mode='CW').count()
                    qso_160ssb = q_160.filter(mode='SSB').count()
                    qso_160rtty = q_160.filter(mode='RTTY').count()
                    qso_160psk = q_160.filter(mode='PSK').count()
                    qso_160ft4 = q_160.filter(mode='MFSK').count()
                    qso_160ft8 = q_160.filter(mode='FT8').count()

                q_80 = q1.filter(band='4')
                if q_80:
                    qso_80cw = q_80.filter(mode='CW').count()
                    qso_80ssb = q_80.filter(mode='SSB').count()
                    qso_80rtty = q_80.filter(mode='RTTY').count()
                    qso_80psk = q_80.filter(mode='PSK').count()
                    qso_80ft4 = q_80.filter(mode='MFSK').count()
                    qso_80ft8 = q_80.filter(mode='FT8').count()

                q_40 = q1.filter(band='7')
                if q_40:
                    qso_40cw = q_40.filter(mode='CW').count()
                    qso_40ssb = q_40.filter(mode='SSB').count()
                    qso_40rtty = q_40.filter(mode='RTTY').count()
                    qso_40psk = q_40.filter(mode='PSK').count()
                    qso_40ft4 = q_40.filter(mode='MFSK').count()
                    qso_40ft8 = q_40.filter(mode='FT8').count()

                q_30 = q1.filter(band='10')
                if q_30:
                    qso_30cw = q_30.filter(mode='CW').count()
                    qso_30rtty = q_30.filter(mode='RTTY').count()
                    qso_30psk = q_30.filter(mode='PSK').count()
                    qso_30ft4 = q_30.filter(mode='MFSK').count()
                    qso_30ft8 = q_30.filter(mode='FT8').count()

                q_20 = q1.filter(band='14')
                if q_20:
                    qso_20cw = q_20.filter(mode='CW').count()
                    qso_20ssb = q_20.filter(mode='SSB').count()
                    qso_20rtty = q_20.filter(mode='RTTY').count()
                    qso_20psk = q_20.filter(mode='PSK').count()
                    qso_20ft4 = q_20.filter(mode='MFSK').count()
                    qso_20ft8 = q_20.filter(mode='FT8').count()

                q_17 = q1.filter(band='18')
                if q_17:
                    qso_17cw = q_17.filter(mode='CW').count()
                    qso_17ssb = q_17.filter(mode='SSB').count()
                    qso_17rtty = q_17.filter(mode='RTTY').count()
                    qso_17psk = q_17.filter(mode='PSK').count()
                    qso_17ft4 = q_17.filter(mode='MFSK').count()
                    qso_17ft8 = q_17.filter(mode='FT8').count()

                q_15 = q1.filter(band='21')
                if q_15:
                    qso_15cw = q_15.filter(mode='CW').count()
                    qso_15ssb = q_15.filter(mode='SSB').count()
                    qso_15rtty = q_15.filter(mode='RTTY').count()
                    qso_15psk = q_15.filter(mode='PSK').count()
                    qso_15ft4 = q_15.filter(mode='MFSK').count()
                    qso_15ft8 = q_15.filter(mode='FT8').count()

                q_12 = q1.filter(band='25')
                if q_12:
                    qso_12cw = q_12.filter(mode='CW').count()
                    qso_12ssb = q_12.filter(mode='SSB').count()
                    qso_12rtty = q_12.filter(mode='RTTY').count()
                    qso_12psk = q_12.filter(mode='PSK').count()
                    qso_12ft4 = q_12.filter(mode='MFSK').count()
                    qso_12ft8 = q_12.filter(mode='FT8').count()

                q_10 = q1.filter(band='28')
                if q_10:
                    qso_10cw = q_10.filter(mode='CW').count()
                    qso_10ssb = q_10.filter(mode='SSB').count()
                    qso_10rtty = q_10.filter(mode='RTTY').count()
                    qso_10psk = q_10.filter(mode='PSK').count()
                    qso_10ft4 = q_10.filter(mode='MFSK').count()
                    qso_10ft8 = q_10.filter(mode='FT8').count()

                total_160 = qso_160cw + qso_160ssb + qso_160rtty + qso_160psk + qso_160ft4 + qso_160ft8
                total_80 = qso_80cw + qso_80ssb + qso_80rtty + qso_80psk + qso_80ft4 + qso_80ft8
                total_40 = qso_40cw + qso_40ssb + qso_40rtty + qso_40psk + qso_40ft4 + qso_40ft8
                total_30 = qso_30cw + qso_30rtty + qso_30psk + qso_30ft4 + qso_30ft8
                total_20 = qso_20cw + qso_20ssb + qso_20rtty + qso_20psk + qso_20ft4 + qso_20ft8
                total_17 = qso_17cw + qso_17ssb + qso_17rtty + qso_17psk + qso_17ft4 + qso_17ft8
                total_15 = qso_15cw + qso_15ssb + qso_15rtty + qso_15psk + qso_15ft4 + qso_15ft8
                total_12 = qso_12cw + qso_12ssb + qso_12rtty + qso_12psk + qso_12ft4 + qso_12ft8
                total_10 = qso_10cw + qso_10ssb + qso_10rtty + qso_10psk + qso_10ft4 + qso_10ft8

                total_cw = qso_160cw + qso_80cw + qso_40cw + qso_30cw + qso_20cw + qso_17cw + qso_15cw + qso_12cw + qso_10cw
                total_ssb = qso_160ssb + qso_80ssb + qso_40ssb + qso_20ssb + qso_17ssb + qso_15ssb + qso_12ssb + qso_10ssb
                total_rtty = qso_160rtty + qso_80rtty + qso_40rtty + qso_30rtty + qso_20rtty + qso_17rtty + qso_15rtty + qso_12rtty + qso_10rtty
                total_psk = qso_160psk + qso_80psk + qso_40psk + qso_30psk + qso_20psk + qso_17psk + qso_15psk + qso_12psk + qso_10psk
                total_ft4 = qso_160ft4 + qso_80ft4 + qso_40ft4 + qso_30ft4 + qso_20ft4 + qso_17ft4 + qso_15ft4 + qso_12ft4 + qso_10ft4
                total_ft8 = qso_160ft8 + qso_80ft8 + qso_40ft8 + qso_30ft8 + qso_20ft8 + qso_17ft8 + qso_15ft8 + qso_12ft8 + qso_10ft8

            else:
                pass

        # Определение страны по позывному.

        if re.match(r'[\w/]{4,18}|\D\d\D$', data):
            cl = []
            pref = []
            qc = Cty.objects.all()
            callsign = data

            callsign = str(callsign.upper())

            for i in range(1, len(callsign) + 1):
                call = callsign[:i].upper()
                for entry in qc:

                    line = entry.pref

                    if ' ' + str(call) + ',' in line or ',' + str(call) + ',' in line or ' ' + str(
                            call) + ':' in line or ',' + str(call) + ';' in line or ' ' + str(
                        call) + ';' in line or ',' + str(call) + '(' in line or '=' + str(
                        call) + '(' in line or '=' + str(call) + ',' in line or '=' + str(
                        call) + '[' in line or ',' + str(call) + '[' in line:

                        cll = str(entry.cty)

                        if cll not in cl:
                            cl.append(cll)
                            if callsign[:i] not in pref:
                                pref.append(callsign[:i])

                        if qso:
                            cname = cl.pop() + ','  # Добавляем запятую после, напр.: Kaliningrad,

                            cont_short = ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA', ]
                            cont_long = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania',
                                         'South America']
                            for l in range(len(cont_short)):
                                if entry.cont == cont_short[l]:
                                    cont = cont_long[l]
                                    cnam = cname[:-1]  # Убираем запятую
                                    if cname == 'European Russia,' or cname == 'European Turkey,' or cname == 'Asiatic Russia,' or cname == 'Asiatic Turkey,' or cname == 'South Africa,' or cname == 'Antarctica,':
                                        cname = cnam  # Не дублируем континент
                                        cont = ''

                    # Блок исключений - 2 шт.

                    if re.match(r'^[ru].+[8,9,0]$', callsign, re.I):  # /8, /9, /0 - Asiatic Russia
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA9')

                    if re.match(r'^[ru].+[1,3-7]$', callsign, re.I):  # /1,3-7 - European Russia
                        cll = 'European Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA')

                    if re.match(r'^[ru].+2$', callsign, re.I):
                        cll = 'Kaliningrad'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA2F')

                    if re.match(r'^(ta|tb|tc|ym).+/[0,2-9]$', callsign, re.I):  # 4
                        cll = 'Asiatic Turkey'
                        if qso:
                            cl.append(cll)
                            cname = cl.pop()

                    if re.match(r'^(ta|tb|tc|ym).+/1$', callsign, re.I):  # 5
                        cll = 'European Turkey'
                        if qso:
                            cl.append(cll)
                            cname = cl.pop()

                    if re.search(r'.+/ant$', callsign, re.I):  # 6
                        cll = 'Antarctica'
                        if qso:
                            cl.append(cll)
                            cname = cl.pop()
                            cont = ''

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/[0-7]$', callsign, re.I):  # 6
                        cll = 'Spain'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('EA')

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/8$', callsign, re.I):  # 7
                        cll = 'Canary Islands'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('EA8')

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/9$', callsign, re.I):  # 8
                        cll = 'Ceuta & Melilla'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('EA9')

                    if re.search(r'.+(/R3|/R4)$', callsign, re.I):  # 6
                        cll = 'European Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('R')

                    if re.search(r'.+(/R9|/R0|/R9Z)$', callsign, re.I):  # 6
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA9')

                    if re.search(r".+(/RA|/RA9[FG]|/R9[FG]|/UA9[FG])$", callsign, re.I):  # 6
                        cll = 'European Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA')

                    if re.search(r'.+(/RA9)$', callsign, re.I):  # 6
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        if qso:
                            cname = cl.pop()
                            pref.append('RA9')

                    pr = ['/TF', '/DU7', '/SV9', '/JD1', '/C6A', '/PT2', '/NH2', '/VY2', '/HI9', '/KH0', '/YU8', '/IH9',
                          '/OH0', '/EA6', '/KL7', '/KH6', '/I2', '/VE3', '/KH2', 'T00CW', 'T00SW', 'T00RM', '/VK9L',
                          '/ANT']

                    countrys = ['Iceland', 'Philippines', 'Crete', 'Ogasawara', 'Bahamas', 'Brazil', 'Guam', 'Canada',
                                'Dominican Republic', 'Mariana Islands', 'Kosovo', 'African Italy', 'Aland Islands',
                                'Balearic Islands', 'Alaska', 'Hawaii', 'Italy', 'Canada', 'Guam',
                                'Principality of Seborga, Europe', 'Principality of Seborga, Europe',
                                'Principality of Seborga, Europe', 'Lord Howe Island', 'Antarctica']

                    # print len(pr),len(countrys) # Длины списков должны совпадать!

                    for k in range(len(pr)):
                        if re.search(pr[k], callsign, re.I):
                            cll = countrys[k]
                            cl.append(cll)
                            if qso:
                                cname = cl.pop()
                                if 'T00' not in pr[k]:
                                    pref.append(pr[k][1:])  # Префикс показываем без знака "/"
                                else:
                                    pref.append(pr[k][0:])

            if pref:
                if qso:
                    prefix = pref.pop()
                    t2 = time.time()
                    t_search = str(t2 - t1)[:3] + " sec"

            else:
                pass

    return render(request, 'main/search.html', locals())


def new_calls_old(request):
    t1 = time.time()

    # ================================= 250 новых позывных 2013-10-14

    call_new = Entry.objects.all().order_by(
        '-datetime')  # Сортировка -datetime (чтобы посмотреть ПОСЛЕДНИЕ новые позывные)

    newcalls = []  # "Заготовка" списка новых позывных (последних, встречающихся один раз)
    newcalls_band = []
    newcalls_mode = []

    for i in range(0, len(call_new) - 1):  # Ограничиваем i общим числом связей

        if len(newcalls) < 250:  # Длина списка - 250 новых позывных

            z = Entry.objects.filter(callsign=call_new[i])  # Фильтрация общего списка по позывному.
            zc = z.count()  # Сколько раз позывной call_new[i] встречается в общем списке

            if zc == 1:  # Если позывной только один раз встречается в общем списке,

                for entry in z:
                    zb = entry.band
                    zm = entry.mode

                newcalls.append(str(call_new[i]) + '(' + str(zb) + str(
                    zm) + ')')  # Вносим этот позывной в список последних новых позывных
                newcalls_band.append(str(call_new[i]) + '(' + str(zb) + ')')
                newcalls_mode.append(str(call_new[i]) + '(' + str(zm) + ')')

    newcalls_random = [newcalls, newcalls_band, newcalls_mode]
    newcalls = random.choice(newcalls_random)

    # Дата первого нового позывного 2013-10-14:

    p = (newcalls[-1]).split('(')  # UA0AAA(20CW)- делаем split('(')
    q_z = Entry.objects.filter(callsign=p[0])  # Дату выделяем в html-редставлении (({{ entry.datetime|date:"Y-M-d" }}))

    # Дата последнего (из 250) нового позывного:
    pp = (newcalls[0]).split('(')
    q_zz = Entry.objects.filter(
        callsign=pp[0])  # Дату выделяем в html-редставлении (({{ entry.datetime|date:"Y-M-d" }}))

    # ================================= / 250 новых позывных

    t2 = time.time()
    tt = str(t2 - t1)[:4]
    date_new = datetime.datetime.now()

    return render(request, 'main/new_calls.html', locals())


# #@cache_page(60)
def new_calls(request):
    t1 = time.time()

    logorder = []
    logorder_one = []

    newcalls = Entry.objects.all().order_by('-datetime')

    for item in newcalls:
        logorder.append(item.callsign)
    for i in range(len(logorder) + 1):
        if len(logorder_one) <= 250:
            if logorder.count(logorder[i]) == 1:
                logorder_one.append(logorder[i])
    q_zz = Entry.objects.filter(callsign=logorder_one[0])
    q_z = Entry.objects.filter(callsign=logorder_one[250])

    t2 = time.time()
    tt = str(t2 - t1)[:4]
    date_new = datetime.datetime.now()

    return render(request, 'main/new_calls.html', locals())


def max_qso(request):
    t1 = time.time()

    all_calls = []
    diff_calls = []
    c_q = {}
    c_qq = []
    call = []
    call_value = []

    q_diff = Entry.objects.all()  # Список QSO

    for entry in q_diff:
        all_calls.append(entry.callsign)

        if entry.callsign not in diff_calls:
            diff_calls.append(entry.callsign)

    for item in diff_calls:
        c_q[item] = all_calls.count(item)  # Заполняем словарь - позывной(c_q[item])-количество
    t3 = time.time()

    pairs = map(None, c_q.values(), c_q.keys())  # Пара - количество-позывной
    pairs.sort()  # Сортировка по возрастанию
    pairs.reverse()  # Сортировка по убыванию
    pairs = pairs[:250]  # Ограничиваем список 250-ю позывными

    for item in pairs:
        c_qq.append(str(item[1]) + '(' + str(item[0]) + ')')  # Заносим в список: напр. UA0AAA(100)
    '''    call.append(str(item[1]))
        call_value.append(str(item[0]))
    for i in range(250):
        call.insert(2*i+1,'- '+call_value[i])'''

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_max = datetime.datetime.now()

    return render(request, 'max_qso.html', locals())


def qsls(request):
    x = 'LOTW'
    y = 'LOTW '*2
    z = 'LOTW '*3

    fq = [x, y, z]

    fqq1 = random.choice(fq)
    fqq2 = random.choice(fq)
    fqq3 = random.choice(fq)

    while fqq3 == fqq1 or fqq3 == fqq2 or fqq2 == fqq1:  # Делать случайные выборки до тех пор, пока значения x,y,z не будут различными:

        fqq1 = random.choice(fq)
        fqq2 = random.choice(fq)
        fqq3 = random.choice(fq)

    return render(request, 'main/qsls.html', locals())


def solar(request):
    today = datetime.datetime.now()

    t1 = time.time()
    t2 = time.time()
    tt = str(t2 - t1)[:5]

    return render(request, 'main/solar.html', locals())


def tv(request):
    return render(request, 'tvplayer.html', locals())


@cache_page(60*60)
def statistics(request):
    t1 = time.time()  # Первая отсечка времени (для обсчета времени, затраченного на операцию "статистика")

    diff_calls_160cw = []
    diff_calls_80cw = []
    diff_calls_40cw = []
    diff_calls_30cw = []
    diff_calls_20cw = []
    diff_calls_17cw = []
    diff_calls_15cw = []
    diff_calls_12cw = []
    diff_calls_10cw = []
    diff_cws = []

    diff_calls_160ssb = []
    diff_calls_80ssb = []
    diff_calls_40ssb = []
    diff_calls_30ssb = []
    diff_calls_20ssb = []
    diff_calls_17ssb = []
    diff_calls_15ssb = []
    diff_calls_12ssb = []
    diff_calls_10ssb = []
    diff_ssbs = []

    diff_calls_160rtty = []
    diff_calls_80rtty = []
    diff_calls_40rtty = []
    diff_calls_30rtty = []
    diff_calls_20rtty = []
    diff_calls_17rtty = []
    diff_calls_15rtty = []
    diff_calls_12rtty = []
    diff_calls_10rtty = []
    diff_rttys = []

    diff_calls_160psk = []
    diff_calls_80psk = []
    diff_calls_40psk = []
    diff_calls_30psk = []
    diff_calls_20psk = []
    diff_calls_17psk = []
    diff_calls_15psk = []
    diff_calls_12psk = []
    diff_calls_10psk = []
    diff_psks = []

    diff_calls_160ft4 = []
    diff_calls_80ft4 = []
    diff_calls_40ft4 = []
    diff_calls_30ft4 = []
    diff_calls_20ft4 = []
    diff_calls_17ft4 = []
    diff_calls_15ft4 = []
    diff_calls_12ft4 = []
    diff_calls_10ft4 = []
    diff_ft4s = []

    diff_calls_160ft8 = []
    diff_calls_80ft8 = []
    diff_calls_40ft8 = []
    diff_calls_30ft8 = []
    diff_calls_20ft8 = []
    diff_calls_17ft8 = []
    diff_calls_15ft8 = []
    diff_calls_12ft8 = []
    diff_calls_10ft8 = []
    diff_ft8s = []

    diff_calls_160 = []
    diff_calls_80 = []
    diff_calls_40 = []
    diff_calls_30 = []
    diff_calls_20 = []
    diff_calls_17 = []
    diff_calls_15 = []
    diff_calls_12 = []
    diff_calls_10 = []
    diff_calls = []

    # if len(diff_calls) <= 1: # Подсчет уникальных позывных

    q_diff = Entry.objects.all()  # Список QSO
    qso = 0  # Начальное значение
    diff_all = 1
    all_count = q_diff.count()  # Число записей в логе (Общее число QSO)

    # Заполнение таблицы

    q160 = []
    q80 = []
    q40 = []
    q30 = []
    q20 = []
    q17 = []
    q15 = []
    q12 = []
    q10 = []

    qcw = []
    qssb = []
    qrtty = []
    qpsk = []
    qft4 = []
    qft8 = []

    call_160cw = []
    call_80cw = []
    call_40cw = []
    call_30cw = []
    call_20cw = []
    call_17cw = []
    call_15cw = []
    call_12cw = []
    call_10cw = []

    call_160ssb = []
    call_80ssb = []
    call_40ssb = []
    call_20ssb = []
    call_17ssb = []
    call_15ssb = []
    call_12ssb = []
    call_10ssb = []

    call_160rtty = []
    call_80rtty = []
    call_40rtty = []
    call_30rtty = []
    call_20rtty = []
    call_17rtty = []
    call_15rtty = []
    call_12rtty = []
    call_10rtty = []

    call_160psk = []
    call_80psk = []
    call_40psk = []
    call_30psk = []
    call_20psk = []
    call_17psk = []
    call_15psk = []
    call_12psk = []
    call_10psk = []

    call_160ft4 = []
    call_80ft4 = []
    call_40ft4 = []
    call_30ft4 = []
    call_20ft4 = []
    call_17ft4 = []
    call_15ft4 = []
    call_12ft4 = []
    call_10ft4 = []

    call_160ft8 = []
    call_80ft8 = []
    call_40ft8 = []
    call_30ft8 = []
    call_20ft8 = []
    call_17ft8 = []
    call_15ft8 = []
    call_12ft8 = []
    call_10ft8 = []

    for entry in q_diff:

        if entry.band == '2':
            q160.append('1')
            if entry.mode == 'CW':
                call_160cw.append('1')
                if entry.callsign not in diff_calls_160cw:
                    diff_calls_160cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_160ssb.append('1')
                if entry.callsign not in diff_calls_160ssb:
                    diff_calls_160ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_160rtty.append('1')
                if entry.callsign not in diff_calls_160rtty:
                    diff_calls_160rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_160psk.append('1')
                if entry.callsign not in diff_calls_160psk:
                    diff_calls_160psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_160ft4.append('1')
                if entry.callsign not in diff_calls_160ft4:
                    diff_calls_160ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_160ft8.append('1')
                if entry.callsign not in diff_calls_160ft8:
                    diff_calls_160ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_160:
                diff_calls_160.append(entry.callsign)

        if entry.band == '4':
            q80.append('1')
            if entry.mode == 'CW':
                call_80cw.append('1')
                if entry.callsign not in diff_calls_80cw:
                    diff_calls_80cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_80ssb.append('1')
                if entry.callsign not in diff_calls_80ssb:
                    diff_calls_80ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_80rtty.append('1')
                if entry.callsign not in diff_calls_80rtty:
                    diff_calls_80rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_80psk.append('1')
                if entry.callsign not in diff_calls_80psk:
                    diff_calls_80psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_80ft4.append('1')
                if entry.callsign not in diff_calls_80ft4:
                    diff_calls_80ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_80ft8.append('1')
                if entry.callsign not in diff_calls_80ft8:
                    diff_calls_80ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_80:
                diff_calls_80.append(entry.callsign)

        if entry.band == '7':
            q40.append('1')
            if entry.mode == 'CW':
                call_40cw.append('1')
                if entry.callsign not in diff_calls_40cw:
                    diff_calls_40cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_40ssb.append('1')
                if entry.callsign not in diff_calls_40ssb:
                    diff_calls_40ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_40rtty.append('1')
                if entry.callsign not in diff_calls_40rtty:
                    diff_calls_40rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_40psk.append('1')
                if entry.callsign not in diff_calls_40psk:
                    diff_calls_40psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_40ft4.append('1')
                if entry.callsign not in diff_calls_40ft4:
                    diff_calls_40ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_40ft8.append('1')
                if entry.callsign not in diff_calls_40ft8:
                    diff_calls_40ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_40:
                diff_calls_40.append(entry.callsign)

        if entry.band == '10':
            q30.append('1')
            if entry.mode == 'CW':
                call_30cw.append('1')
                if entry.callsign not in diff_calls_30cw:
                    diff_calls_30cw.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_30rtty.append('1')
                if entry.callsign not in diff_calls_30rtty:
                    diff_calls_30rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_30psk.append('1')
                if entry.callsign not in diff_calls_30psk:
                    diff_calls_30psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_30ft4.append('1')
                if entry.callsign not in diff_calls_30ft4:
                    diff_calls_30ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_30ft8.append('1')
                if entry.callsign not in diff_calls_30ft8:
                    diff_calls_30ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_30:
                diff_calls_30.append(entry.callsign)

        if entry.band == '14':
            q20.append('1')
            if entry.mode == 'CW':
                call_20cw.append('1')
                if entry.callsign not in diff_calls_20cw:
                    diff_calls_20cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_20ssb.append('1')
                if entry.callsign not in diff_calls_20ssb:
                    diff_calls_20ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_20rtty.append('1')
                if entry.callsign not in diff_calls_20rtty:
                    diff_calls_20rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_20psk.append('1')
                if entry.callsign not in diff_calls_20psk:
                    diff_calls_20psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_20ft4.append('1')
                if entry.callsign not in diff_calls_20ft4:
                    diff_calls_20ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_20ft8.append('1')
                if entry.callsign not in diff_calls_20ft8:
                    diff_calls_20ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_20:
                diff_calls_20.append(entry.callsign)

        if entry.band == '18':
            q17.append('1')
            if entry.mode == 'CW':
                call_17cw.append('1')
                if entry.callsign not in diff_calls_17cw:
                    diff_calls_17cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_17ssb.append('1')
                if entry.callsign not in diff_calls_17ssb:
                    diff_calls_17ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_17rtty.append('1')
                if entry.callsign not in diff_calls_17rtty:
                    diff_calls_17rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_17psk.append('1')
                if entry.callsign not in diff_calls_17psk:
                    diff_calls_17psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_17ft4.append('1')
                if entry.callsign not in diff_calls_17ft4:
                    diff_calls_17ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_17ft8.append('1')
                if entry.callsign not in diff_calls_17ft8:
                    diff_calls_17ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_17:
                diff_calls_17.append(entry.callsign)

        if entry.band == '21':
            q15.append('1')
            if entry.mode == 'CW':
                call_15cw.append('1')
                if entry.callsign not in diff_calls_15cw:
                    diff_calls_15cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_15ssb.append('1')
                if entry.callsign not in diff_calls_15ssb:
                    diff_calls_15ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_15rtty.append('1')
                if entry.callsign not in diff_calls_15rtty:
                    diff_calls_15rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_15psk.append('1')
                if entry.callsign not in diff_calls_15psk:
                    diff_calls_15psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_15ft4.append('1')
                if entry.callsign not in diff_calls_15ft4:
                    diff_calls_15ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_15ft8.append('1')
                if entry.callsign not in diff_calls_15ft8:
                    diff_calls_15ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_15:
                diff_calls_15.append(entry.callsign)

        if entry.band == '25':
            q12.append('1')
            if entry.mode == 'CW':
                call_12cw.append('1')
                if entry.callsign not in diff_calls_12cw:
                    diff_calls_12cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_12ssb.append('1')
                if entry.callsign not in diff_calls_12ssb:
                    diff_calls_12ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_12rtty.append('1')
                if entry.callsign not in diff_calls_12rtty:
                    diff_calls_12rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_12psk.append('1')
                if entry.callsign not in diff_calls_12psk:
                    diff_calls_12psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_12ft4.append('1')
                if entry.callsign not in diff_calls_12ft4:
                    diff_calls_12ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_12ft8.append('1')
                if entry.callsign not in diff_calls_12ft8:
                    diff_calls_12ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_12:
                diff_calls_12.append(entry.callsign)

        if entry.band == '28':
            q10.append('1')
            if entry.mode == 'CW':
                call_10cw.append('1')
                if entry.callsign not in diff_calls_10cw:
                    diff_calls_10cw.append(entry.callsign)
            elif entry.mode == 'SSB':
                call_10ssb.append('1')
                if entry.callsign not in diff_calls_10ssb:
                    diff_calls_10ssb.append(entry.callsign)
            elif entry.mode == 'RTTY':
                call_10rtty.append('1')
                if entry.callsign not in diff_calls_10rtty:
                    diff_calls_10rtty.append(entry.callsign)
            elif entry.mode == 'PSK':
                call_10psk.append('1')
                if entry.callsign not in diff_calls_10psk:
                    diff_calls_10psk.append(entry.callsign)
            elif entry.mode == 'MFSK':
                call_10ft4.append('1')
                if entry.callsign not in diff_calls_10ft4:
                    diff_calls_10ft4.append(entry.callsign)
            elif entry.mode == 'FT8':
                call_10ft8.append('1')
                if entry.callsign not in diff_calls_10ft8:
                    diff_calls_10ft8.append(entry.callsign)
            if entry.callsign not in diff_calls_10:
                diff_calls_10.append(entry.callsign)

        if entry.mode == 'CW':
            qcw.append('1')
            if entry.callsign not in diff_cws:
                diff_cws.append(entry.callsign)

        elif entry.mode == 'SSB':
            qssb.append('1')
            if entry.callsign not in diff_ssbs:
                diff_ssbs.append(entry.callsign)

        elif entry.mode == 'RTTY':
            qrtty.append('1')
            if entry.callsign not in diff_rttys:
                diff_rttys.append(entry.callsign)

        elif entry.mode == 'PSK':
            qpsk.append('1')
            if entry.callsign not in diff_psks:
                diff_psks.append(entry.callsign)

        elif entry.mode == 'MFSK':
            qft4.append('1')
            if entry.callsign not in diff_ft4s:
                diff_ft4s.append(entry.callsign)

        elif entry.mode == 'FT8':
            qft8.append('1')
            if entry.callsign not in diff_ft8s:
                diff_ft8s.append(entry.callsign)

        if entry.callsign not in diff_calls:
            diff_calls.append(entry.callsign)

    len_160cw_diff = len(diff_calls_160cw)
    len_80cw_diff = len(diff_calls_80cw)
    len_40cw_diff = len(diff_calls_40cw)
    len_30cw_diff = len(diff_calls_30cw)
    len_20cw_diff = len(diff_calls_20cw)
    len_17cw_diff = len(diff_calls_17cw)
    len_15cw_diff = len(diff_calls_15cw)
    len_12cw_diff = len(diff_calls_12cw)
    len_10cw_diff = len(diff_calls_10cw)

    len_160ssb_diff = len(diff_calls_160ssb)
    len_80ssb_diff = len(diff_calls_80ssb)
    len_40ssb_diff = len(diff_calls_40ssb)
    len_20ssb_diff = len(diff_calls_20ssb)
    len_17ssb_diff = len(diff_calls_17ssb)
    len_15ssb_diff = len(diff_calls_15ssb)
    len_12ssb_diff = len(diff_calls_12ssb)
    len_10ssb_diff = len(diff_calls_10ssb)

    len_160rtty_diff = len(diff_calls_160rtty)
    len_80rtty_diff = len(diff_calls_80rtty)
    len_40rtty_diff = len(diff_calls_40rtty)
    len_30rtty_diff = len(diff_calls_30rtty)
    len_20rtty_diff = len(diff_calls_20rtty)
    len_17rtty_diff = len(diff_calls_17rtty)
    len_15rtty_diff = len(diff_calls_15rtty)
    len_12rtty_diff = len(diff_calls_12rtty)
    len_10rtty_diff = len(diff_calls_10rtty)

    len_160psk_diff = len(diff_calls_160psk)
    len_80psk_diff = len(diff_calls_80psk)
    len_40psk_diff = len(diff_calls_40psk)
    len_30psk_diff = len(diff_calls_30psk)
    len_20psk_diff = len(diff_calls_20psk)
    len_17psk_diff = len(diff_calls_17psk)
    len_15psk_diff = len(diff_calls_15psk)
    len_12psk_diff = len(diff_calls_12psk)
    len_10psk_diff = len(diff_calls_10psk)

    len_160ft4_diff = len(diff_calls_160ft4)
    len_80ft4_diff = len(diff_calls_80ft4)
    len_40ft4_diff = len(diff_calls_40ft4)
    len_30ft4_diff = len(diff_calls_30ft4)
    len_20ft4_diff = len(diff_calls_20ft4)
    len_17ft4_diff = len(diff_calls_17ft4)
    len_15ft4_diff = len(diff_calls_15ft4)
    len_12ft4_diff = len(diff_calls_12ft4)
    len_10ft4_diff = len(diff_calls_10ft4)

    len_160ft8_diff = len(diff_calls_160ft8)
    len_80ft8_diff = len(diff_calls_80ft8)
    len_40ft8_diff = len(diff_calls_40ft8)
    len_30ft8_diff = len(diff_calls_30ft8)
    len_20ft8_diff = len(diff_calls_20ft8)
    len_17ft8_diff = len(diff_calls_17ft8)
    len_15ft8_diff = len(diff_calls_15ft8)
    len_12ft8_diff = len(diff_calls_12ft8)
    len_10ft8_diff = len(diff_calls_10ft8)

    len_160_diff = len(diff_calls_160)
    len_80_diff = len(diff_calls_80)
    len_40_diff = len(diff_calls_40)
    len_30_diff = len(diff_calls_30)
    len_20_diff = len(diff_calls_20)
    len_17_diff = len(diff_calls_17)
    len_15_diff = len(diff_calls_15)
    len_12_diff = len(diff_calls_12)
    len_10_diff = len(diff_calls_10)

    qso_160cw = len(call_160cw)
    qso_80cw = len(call_80cw)
    qso_40cw = len(call_40cw)
    qso_30cw = len(call_30cw)
    qso_20cw = len(call_20cw)
    qso_17cw = len(call_17cw)
    qso_15cw = len(call_15cw)
    qso_12cw = len(call_12cw)
    qso_10cw = len(call_10cw)

    qso_160ssb = len(call_160ssb)
    qso_80ssb = len(call_80ssb)
    qso_40ssb = len(call_40ssb)
    qso_20ssb = len(call_20ssb)
    qso_17ssb = len(call_17ssb)
    qso_15ssb = len(call_15ssb)
    qso_12ssb = len(call_12ssb)
    qso_10ssb = len(call_10ssb)

    qso_160rtty = len(call_160rtty)
    qso_80rtty = len(call_80rtty)
    qso_40rtty = len(call_40rtty)
    qso_30rtty = len(call_30rtty)
    qso_20rtty = len(call_20rtty)
    qso_17rtty = len(call_17rtty)
    qso_15rtty = len(call_15rtty)
    qso_12rtty = len(call_12rtty)
    qso_10rtty = len(call_10rtty)

    qso_160psk = len(call_160psk)
    qso_80psk = len(call_80psk)
    qso_40psk = len(call_40psk)
    qso_30psk = len(call_30psk)
    qso_20psk = len(call_20psk)
    qso_17psk = len(call_17psk)
    qso_15psk = len(call_15psk)
    qso_12psk = len(call_12psk)
    qso_10psk = len(call_10psk)

    qso_160ft4 = len(call_160ft4)
    qso_80ft4 = len(call_80ft4)
    qso_40ft4 = len(call_40ft4)
    qso_30ft4 = len(call_30ft4)
    qso_20ft4 = len(call_20ft4)
    qso_17ft4 = len(call_17ft4)
    qso_15ft4 = len(call_15ft4)
    qso_12ft4 = len(call_12ft4)
    qso_10ft4 = len(call_10ft4)

    qso_160ft8 = len(call_160ft8)
    qso_80ft8 = len(call_80ft8)
    qso_40ft8 = len(call_40ft8)
    qso_30ft8 = len(call_30ft8)
    qso_20ft8 = len(call_20ft8)
    qso_17ft8 = len(call_17ft8)
    qso_15ft8 = len(call_15ft8)
    qso_12ft8 = len(call_12ft8)
    qso_10ft8 = len(call_10ft8)

    len_diff_cws = len(diff_cws)
    len_diff_ssbs = len(diff_ssbs)
    len_diff_rttys = len(diff_rttys)
    len_diff_psks = len(diff_psks)
    len_diff_ft4s = len(diff_ft4s)
    len_diff_ft8s = len(diff_ft8s)
    diff_calls_all = len(diff_calls)

    # qso total:

    if all_count != 0:
        total_160S = qso_160cw + qso_160ssb + qso_160rtty + qso_160psk + qso_160ft4 + qso_160ft8
        total_160 = str(round(float(total_160S) / float(all_count) * 100, 2))  # В процентах на 160
        total_80S = qso_80cw + qso_80ssb + qso_80rtty + qso_80psk + qso_80ft4 + qso_80ft8
        total_80 = str(round(float(total_80S) / float(all_count) * 100, 2))
        total_40S = qso_40cw + qso_40ssb + qso_40rtty + qso_40psk + qso_40ft4 + qso_40ft8
        total_40 = str(round(float(total_40S) / float(all_count) * 100, 2))
        total_30S = qso_30cw + qso_30rtty + qso_30psk + qso_30ft4 + qso_30ft8
        total_30 = str(round(float(total_30S) / float(all_count) * 100, 2))
        total_20S = qso_20cw + qso_20ssb + qso_20rtty + qso_20psk + qso_20ft4 + qso_20ft8
        total_20 = str(round(float(total_20S) / float(all_count) * 100, 2))
        total_17S = qso_17cw + qso_17ssb + qso_17rtty + qso_17psk + qso_17ft4 + qso_17ft8
        total_17 = str(round(float(total_17S) / float(all_count) * 100, 2))
        total_15S = qso_15cw + qso_15ssb + qso_15rtty + qso_15psk + qso_15ft4 + qso_15ft8
        total_15 = str(round(float(total_15S) / float(all_count) * 100, 2))
        total_12S = qso_12cw + qso_12ssb + qso_12rtty + qso_12psk + qso_12ft4 + qso_12ft8
        total_12 = str(round(float(total_12S) / float(all_count) * 100, 2))
        total_10S = qso_10cw + qso_10ssb + qso_10rtty + qso_10psk + qso_10ft4 + qso_10ft8
        total_10 = str(round(float(total_10S) / float(all_count) * 100, 2))

        # mode total:

        total_cws = qso_160cw + qso_80cw + qso_40cw + qso_30cw + qso_20cw + qso_17cw + qso_15cw + qso_12cw + qso_10cw
        total_cw = str(round(float(total_cws) / float(all_count) * 100, 2))
        total_ssbs = qso_160ssb + qso_80ssb + qso_40ssb + qso_20ssb + qso_17ssb + qso_15ssb + qso_12ssb + qso_10ssb
        total_ssb = str(round(float(total_ssbs) / float(all_count) * 100, 2))
        total_rttys = qso_160rtty + qso_80rtty + qso_40rtty + qso_30rtty + qso_20rtty + qso_17rtty + qso_15rtty + qso_12rtty + qso_10rtty
        total_rtty = str(round(float(total_rttys) / float(all_count) * 100, 2))
        total_psks = qso_160psk + qso_80psk + qso_40psk + qso_30psk + qso_20psk + qso_17psk + qso_15psk + qso_12psk + qso_10psk
        total_psk = str(round(float(total_psks) / float(all_count) * 100, 2))
        total_ft4s = qso_160ft4 + qso_80ft4 + qso_40ft4 + qso_30ft4 + qso_20ft4 + qso_17ft4 + qso_15ft4 + qso_12ft4 + qso_10ft4
        total_ft4 = str(round(float(total_ft4s) / float(all_count) * 100, 2))
        total_ft8s = qso_160ft8 + qso_80ft8 + qso_40ft8 + qso_30ft8 + qso_20ft8 + qso_17ft8 + qso_15ft8 + qso_12ft8 + qso_10ft8
        total_ft8 = str(round(float(total_ft8s) / float(all_count) * 100, 2))

        diff_calls_all_procent = str(round(float(diff_calls_all) / float(all_count) * 100, 2)) + '%'

    # Проценты в ячейках. CW:

    if qso_160cw != 0:
        procent_title_160cw = str(round(float(len_160cw_diff) / float(qso_160cw) * 100, 2))
    if qso_80cw != 0:
        procent_title_80cw = str(round(float(len_80cw_diff) / float(qso_80cw) * 100, 2))
    if qso_40cw != 0:
        procent_title_40cw = str(round(float(len_40cw_diff) / float(qso_40cw) * 100, 2))
    if qso_30cw != 0:
        procent_title_30cw = str(round(float(len_30cw_diff) / float(qso_30cw) * 100, 2))
    if qso_20cw != 0:
        procent_title_20cw = str(round(float(len_20cw_diff) / float(qso_20cw) * 100, 2))
    if qso_17cw != 0:
        procent_title_17cw = str(round(float(len_17cw_diff) / float(qso_17cw) * 100, 2))
    if qso_15cw != 0:
        procent_title_15cw = str(round(float(len_15cw_diff) / float(qso_15cw) * 100, 2))
    if qso_12cw != 0:
        procent_title_12cw = str(round(float(len_12cw_diff) / float(qso_12cw) * 100, 2))
    if qso_10cw != 0:
        procent_title_10cw = str(round(float(len_10cw_diff) / float(qso_10cw) * 100, 2))
    if total_cws != 0:
        procent_title_sum_cw = str(round(float(len_diff_cws) / float(total_cws) * 100, 2))

    # Проценты в ячейках. SSB:

    if qso_160ssb != 0:
        procent_title_160ssb = str(round(float(len_160ssb_diff) / float(qso_160ssb) * 100, 2))
    if qso_80ssb != 0:
        procent_title_80ssb = str(round(float(len_80ssb_diff) / float(qso_80ssb) * 100, 2))
    if qso_40ssb != 0:
        procent_title_40ssb = str(round(float(len_40ssb_diff) / float(qso_40ssb) * 100, 2))
    if qso_20ssb != 0:
        procent_title_20ssb = str(round(float(len_20ssb_diff) / float(qso_20ssb) * 100, 2))
    if qso_17ssb != 0:
        procent_title_17ssb = str(round(float(len_17ssb_diff) / float(qso_17ssb) * 100, 2))
    if qso_15ssb != 0:
        procent_title_15ssb = str(round(float(len_15ssb_diff) / float(qso_15ssb) * 100, 2))
    if qso_12ssb != 0:
        procent_title_12ssb = str(round(float(len_12ssb_diff) / float(qso_12ssb) * 100, 2))
    if qso_10ssb != 0:
        procent_title_10ssb = str(round(float(len_10ssb_diff) / float(qso_10ssb) * 100, 2))
    if total_ssbs != 0:
        procent_title_sum_ssb = str(round(float(len_diff_ssbs) / float(total_ssbs) * 100, 2))

    # Проценты в ячейках. RTTY:
    if qso_160rtty != 0:
        procent_title_160rtty = str(round(float(len_160rtty_diff) / float(qso_160rtty) * 100, 2))
    if qso_80rtty != 0:
        procent_title_80rtty = str(round(float(len_80rtty_diff) / float(qso_80rtty) * 100, 2))
    if qso_40rtty != 0:
        procent_title_40rtty = str(round(float(len_40rtty_diff) / float(qso_40rtty) * 100, 2))
    if qso_30rtty != 0:
        procent_title_30rtty = str(round(float(len_30rtty_diff) / float(qso_30rtty) * 100, 2))
    if qso_20rtty != 0:
        procent_title_20rtty = str(round(float(len_20rtty_diff) / float(qso_20rtty) * 100, 2))
    if qso_17rtty != 0:
        procent_title_17rtty = str(round(float(len_17rtty_diff) / float(qso_17rtty) * 100, 2))
    if qso_15rtty != 0:
        procent_title_15rtty = str(round(float(len_15rtty_diff) / float(qso_15rtty) * 100, 2))
    if qso_12rtty != 0:
        procent_title_12rtty = str(round(float(len_12rtty_diff) / float(qso_12rtty) * 100, 2))
    if qso_10rtty != 0:
        procent_title_10rtty = str(round(float(len_10rtty_diff) / float(qso_10rtty) * 100, 2))
    if total_rttys != 0:
        procent_title_sum_rtty = str(round(float(len_diff_rttys) / float(total_rttys) * 100, 2))

    # Проценты в ячейках. PSK:

    if qso_160psk != 0:
        procent_title_160psk = str(round(float(len_160psk_diff) / float(qso_160psk) * 100, 2))
    if qso_80psk != 0:
        procent_title_80psk = str(round(float(len_80psk_diff) / float(qso_80psk) * 100, 2))
    if qso_40psk != 0:
        procent_title_40psk = str(round(float(len_40psk_diff) / float(qso_40psk) * 100, 2))
    if qso_30psk != 0:
        procent_title_30psk = str(round(float(len_30psk_diff) / float(qso_30psk) * 100, 2))
    if qso_20psk != 0:
        procent_title_20psk = str(round(float(len_20psk_diff) / float(qso_20psk) * 100, 2))
    if qso_17psk != 0:
        procent_title_17psk = str(round(float(len_17psk_diff) / float(qso_17psk) * 100, 2))
    if qso_15psk != 0:
        procent_title_15psk = str(round(float(len_15psk_diff) / float(qso_15psk) * 100, 2))
    if qso_12psk != 0:
        procent_title_12psk = str(round(float(len_12psk_diff) / float(qso_12psk) * 100, 2))
    if qso_10psk != 0:
        procent_title_10psk = str(round(float(len_10psk_diff) / float(qso_10psk) * 100, 2))
    if total_psks != 0:
        procent_title_sum_psk = str(round(float(len_diff_psks) / float(total_psks) * 100, 2))

        # Проценты в ячейках. ft4:

        if qso_160ft4 != 0:
            procent_title_160ft4 = str(round(float(len_160ft4_diff) / float(qso_160ft4) * 100, 2))
        if qso_80ft4 != 0:
            procent_title_80ft4 = str(round(float(len_80ft4_diff) / float(qso_80ft4) * 100, 2))
        if qso_40ft4 != 0:
            procent_title_40ft4 = str(round(float(len_40ft4_diff) / float(qso_40ft4) * 100, 2))
        if qso_30ft4 != 0:
            procent_title_30ft4 = str(round(float(len_30ft4_diff) / float(qso_30ft4) * 100, 2))
        if qso_20ft4 != 0:
            procent_title_20ft4 = str(round(float(len_20ft4_diff) / float(qso_20ft4) * 100, 2))
        if qso_17ft4 != 0:
            procent_title_17ft4 = str(round(float(len_17ft4_diff) / float(qso_17ft4) * 100, 2))
        if qso_15ft4 != 0:
            procent_title_15ft4 = str(round(float(len_15ft4_diff) / float(qso_15ft4) * 100, 2))
        if qso_12ft4 != 0:
            procent_title_12ft4 = str(round(float(len_12ft4_diff) / float(qso_12ft4) * 100, 2))
        if qso_10ft4 != 0:
            procent_title_10ft4 = str(round(float(len_10ft4_diff) / float(qso_10ft4) * 100, 2))
        if total_ft4s != 0:
            procent_title_sum_ft4 = str(round(float(len_diff_ft4s) / float(total_ft4s) * 100, 2))

            # Проценты в ячейках. ft8:

            if qso_160ft8 != 0:
                procent_title_160ft8 = str(round(float(len_160ft8_diff) / float(qso_160ft8) * 100, 2))
            if qso_80ft8 != 0:
                procent_title_80ft8 = str(round(float(len_80ft8_diff) / float(qso_80ft8) * 100, 2))
            if qso_40ft8 != 0:
                procent_title_40ft8 = str(round(float(len_40ft8_diff) / float(qso_40ft8) * 100, 2))
            if qso_30ft8 != 0:
                procent_title_30ft8 = str(round(float(len_30ft8_diff) / float(qso_30ft8) * 100, 2))
            if qso_20ft8 != 0:
                procent_title_20ft8 = str(round(float(len_20ft8_diff) / float(qso_20ft8) * 100, 2))
            if qso_17ft8 != 0:
                procent_title_17ft8 = str(round(float(len_17ft8_diff) / float(qso_17ft8) * 100, 2))
            if qso_15ft8 != 0:
                procent_title_15ft8 = str(round(float(len_15ft8_diff) / float(qso_15ft8) * 100, 2))
            if qso_12ft8 != 0:
                procent_title_12ft8 = str(round(float(len_12ft8_diff) / float(qso_12ft8) * 100, 2))
            if qso_10ft8 != 0:
                procent_title_10ft8 = str(round(float(len_10ft8_diff) / float(qso_10ft8) * 100, 2))
            if total_ft8s != 0:
                procent_title_sum_ft8 = str(round(float(len_diff_ft8s) / float(total_ft8s) * 100, 2))

    # Проценты в ячейках. SUM_band:

    if total_160S != 0:
        procent_title_sum160 = str(round(float(len_160_diff) / float(total_160S) * 100, 2))
    if total_80S != 0:
        procent_title_sum80 = str(round(float(len_80_diff) / float(total_80S) * 100, 2))
    if total_40S != 0:
        procent_title_sum40 = str(round(float(len_40_diff) / float(total_40S) * 100, 2))
    if total_30S != 0:
        procent_title_sum30 = str(round(float(len_30_diff) / float(total_30S) * 100, 2))
    if total_20S != 0:
        procent_title_sum20 = str(round(float(len_20_diff) / float(total_20S) * 100, 2))
    if total_17S != 0:
        procent_title_sum17 = str(round(float(len_17_diff) / float(total_17S) * 100, 2))
    if total_15S != 0:
        procent_title_sum15 = str(round(float(len_15_diff) / float(total_15S) * 100, 2))
    if total_12S != 0:
        procent_title_sum12 = str(round(float(len_12_diff) / float(total_12S) * 100, 2))
    if total_10S != 0:
        procent_title_sum10 = str(round(float(len_10_diff) / float(total_10S) * 100, 2))

    # Дата последней в логе qso:

    qs = q_diff.all().order_by('-id')[0]
    log_update = qs.datetime.date()

    # Дата первой в логе qso:

    qs = q_diff.all().order_by('id')[0]  # Вместо 01, 02 выводим Jan, Feb ...
    log_start = qs.datetime.date()

    # Если количество qso по диопазонам-видам и общее количество qso СОВПАДАЕТ, то печатаем:  coincidence = '*'

    coincidence = '**'

    if qso_160cw + qso_80cw + qso_40cw + qso_30cw + qso_20cw + qso_17cw + qso_15cw + qso_12cw + qso_10cw + \
            qso_160ssb + qso_80ssb + qso_40ssb + qso_20ssb + qso_17ssb + qso_15ssb + qso_12ssb + qso_10ssb + \
            qso_160rtty + qso_80rtty + qso_40rtty + qso_30rtty + qso_20rtty + qso_17rtty + qso_15rtty + qso_12rtty + qso_10rtty + \
            qso_160psk + qso_80psk + qso_40psk + qso_30psk + qso_20psk + qso_17psk + qso_15psk + qso_12psk + qso_10psk + \
            qso_160ft4 + qso_80ft4 + qso_40ft4 + qso_30ft4 + qso_20ft4 + qso_17ft4 + qso_15ft4 + qso_12ft4 + qso_10ft4 + \
            qso_160ft8 + qso_80ft8 + qso_40ft8 + qso_30ft8 + qso_20ft8 + qso_17ft8 + qso_15ft8 + qso_12ft8 + qso_10ft8 == all_count:

        coincidence = '*'

        # Что вверху - заполнение таблицы 123 - 311 строчки

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_stat = datetime.datetime.now()

    return render(request, 'main/statistics.html', locals())


@cache_page(60*60)
def qso_period(request):

    t1 = time.time()
    dtc1994 = []
    dtc1995 = []
    dtc1996 = []
    dtc1997 = []
    dtc1998 = []
    dtc1999 = []
    dtc2000 = []
    dtc2001 = []
    dtc2002 = []
    dtc2003 = []
    dtc2004 = []
    dtc2005 = []
    dtc2006 = []
    dtc2007 = []
    dtc2008 = []
    dtc2009 = []
    dtc2010 = []
    dtc2011 = []
    dtc2012 = []
    dtc2013 = []
    dtc2014 = []
    dtc2015 = []
    dtc2016 = []
    dtc2017 = []
    dtc2018 = []
    dtc2019 = []
    dtc2020 = []
    dtc2021 = []
    dtc2022 = []

    q_diff = Entry.objects.all()  # Список QSO
    dtf1994 = q_diff.filter(datetime__year='1994')
    dtf1995 = q_diff.filter(datetime__year='1995')
    dtf1996 = q_diff.filter(datetime__year='1996')
    dtf1997 = q_diff.filter(datetime__year='1997')
    dtf1998 = q_diff.filter(datetime__year='1998')
    dtf1999 = q_diff.filter(datetime__year='1999')
    dtf2000 = q_diff.filter(datetime__year='2000')
    dtf2001 = q_diff.filter(datetime__year='2001')
    dtf2002 = q_diff.filter(datetime__year='2002')
    dtf2003 = q_diff.filter(datetime__year='2003')
    dtf2004 = q_diff.filter(datetime__year='2004')
    dtf2005 = q_diff.filter(datetime__year='2005')
    dtf2006 = q_diff.filter(datetime__year='2006')
    dtf2007 = q_diff.filter(datetime__year='2007')
    dtf2008 = q_diff.filter(datetime__year='2008')
    dtf2009 = q_diff.filter(datetime__year='2009')
    dtf2010 = q_diff.filter(datetime__year='2010')
    dtf2011 = q_diff.filter(datetime__year='2011')
    dtf2012 = q_diff.filter(datetime__year='2012')
    dtf2013 = q_diff.filter(datetime__year='2013')
    dtf2014 = q_diff.filter(datetime__year='2014')
    dtf2015 = q_diff.filter(datetime__year='2015')
    dtf2016 = q_diff.filter(datetime__year='2016')
    dtf2017 = q_diff.filter(datetime__year='2017')
    dtf2018 = q_diff.filter(datetime__year='2018')
    dtf2019 = q_diff.filter(datetime__year='2019')
    dtf2020 = q_diff.filter(datetime__year='2020')
    dtf2021 = q_diff.filter(datetime__year='2021')
    dtf2022 = q_diff.filter(datetime__year='2022')

    for entry in dtf1994:
        if entry.callsign not in dtc1994:
            dtc1994.append(entry.callsign)
    dtcl_1994 = len(dtc1994)

    for entry in dtf1995:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995:
            dtc1995.append(entry.callsign)
    dtcl_1995 = len(dtc1995)

    for entry in dtf1996:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996:
            dtc1996.append(entry.callsign)
    dtcl_1996 = len(dtc1996)

    for entry in dtf1997:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997:
            dtc1997.append(entry.callsign)
    dtcl_1997 = len(dtc1997)

    for entry in dtf1998:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998:
            dtc1998.append(entry.callsign)
    dtcl_1998 = len(dtc1998)

    for entry in dtf1999:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999:
            dtc1999.append(entry.callsign)
    dtcl_1999 = len(dtc1999)

    for entry in dtf2000:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000:
            dtc2000.append(entry.callsign)
    dtcl_2000 = len(dtc2000)

    for entry in dtf2001:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001:
            dtc2001.append(entry.callsign)
    dtcl_2001 = len(dtc2001)

    for entry in dtf2002:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002:
            dtc2002.append(entry.callsign)
    dtcl_2002 = len(dtc2002)

    for entry in dtf2003:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003:
            dtc2003.append(entry.callsign)
    dtcl_2003 = len(dtc2003)

    for entry in dtf2004:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004:
            dtc2004.append(entry.callsign)
    dtcl_2004 = len(dtc2004)

    for entry in dtf2005:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005:
            dtc2005.append(entry.callsign)
    dtcl_2005 = len(dtc2005)

    for entry in dtf2006:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006:
            dtc2006.append(entry.callsign)
    dtcl_2006 = len(dtc2006)

    for entry in dtf2007:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007:
            dtc2007.append(entry.callsign)
    dtcl_2007 = len(dtc2007)

    for entry in dtf2008:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008:
            dtc2008.append(entry.callsign)
    dtcl_2008 = len(dtc2008)

    for entry in dtf2009:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009:
            dtc2009.append(entry.callsign)
    dtcl_2009 = len(dtc2009)

    for entry in dtf2010:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010:
            dtc2010.append(entry.callsign)
    dtcl_2010 = len(dtc2010)

    for entry in dtf2011:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011:
            dtc2011.append(entry.callsign)
    dtcl_2011 = len(dtc2011)

    for entry in dtf2012:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012:
            dtc2012.append(entry.callsign)
    dtcl_2012 = len(dtc2012)

    for entry in dtf2013:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013:
            dtc2013.append(entry.callsign)
    dtcl_2013 = len(dtc2013)

    for entry in dtf2014:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014:
            dtc2014.append(entry.callsign)
    dtcl_2014 = len(dtc2014)

    for entry in dtf2015:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015:
            dtc2015.append(entry.callsign)
    dtcl_2015 = len(dtc2015)

    for entry in dtf2016:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016:
            dtc2016.append(entry.callsign)
    dtcl_2016 = len(dtc2016)

    for entry in dtf2017:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017:
            dtc2017.append(entry.callsign)
    dtcl_2017 = len(dtc2017)

    for entry in dtf2018:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017 and entry.callsign not in dtc2018:
            dtc2018.append(entry.callsign)
    dtcl_2018 = len(dtc2018)

    for entry in dtf2019:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017 and entry.callsign not in dtc2018 and entry.callsign not in dtc2019:
            dtc2019.append(entry.callsign)
    dtcl_2019 = len(dtc2019)

    for entry in dtf2020:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017 and entry.callsign not in dtc2018 and entry.callsign not in dtc2019 and entry.callsign not in dtc2020:
            dtc2020.append(entry.callsign)
    dtcl_2020 = len(dtc2020)

    for entry in dtf2021:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017 and entry.callsign not in dtc2018 and entry.callsign not in dtc2019 and entry.callsign not in dtc2020 and entry.callsign not in dtc2021:
            dtc2021.append(entry.callsign)
    dtcl_2021 = len(dtc2021)

    for entry in dtf2022:
        if entry.callsign not in dtc1994 and entry.callsign not in dtc1995 and entry.callsign not in dtc1996 and entry.callsign not in dtc1997 and entry.callsign not in dtc1998 and entry.callsign not in dtc1999 and entry.callsign not in dtc2000 and entry.callsign not in dtc2001 and entry.callsign not in dtc2002 and entry.callsign not in dtc2003 and entry.callsign not in dtc2004 and entry.callsign not in dtc2005 and entry.callsign not in dtc2006 and entry.callsign not in dtc2006 and entry.callsign not in dtc2007 and entry.callsign not in dtc2008 and entry.callsign not in dtc2009 and entry.callsign not in dtc2010 and entry.callsign not in dtc2011 and entry.callsign not in dtc2012 and entry.callsign not in dtc2013 and entry.callsign not in dtc2014 and entry.callsign not in dtc2015 and entry.callsign not in dtc2016 and entry.callsign not in dtc2017 and entry.callsign not in dtc2018 and entry.callsign not in dtc2019 and entry.callsign not in dtc2020 and entry.callsign not in dtc2021 and entry.callsign not in dtc2022:
            dtc2022.append(entry.callsign)
    dtcl_2022 = len(dtc2022)

    all_count = q_diff.count()

    dty = []
    dtm = []
    dtt = []
    diff_calls_period = []

    for entry in q_diff:

        dty.append(str(entry.datetime.year))
        dtm.append(str(entry.datetime.month))
        dtt.append(str(entry.datetime.hour))
        if entry.callsign not in diff_calls_period:
            diff_calls_period.append(entry.callsign)
    diff_calls_period = len(diff_calls_period)

    dty1994 = dty.count('1994')
    dty1995 = dty.count('1995')
    dty1996 = dty.count('1996')
    dty1997 = dty.count('1997')
    dty1998 = dty.count('1998')
    dty1999 = dty.count('1999')
    dty2000 = dty.count('2000')
    dty2001 = dty.count('2001')
    dty2002 = dty.count('2002')
    dty2003 = dty.count('2003')
    dty2004 = dty.count('2004')
    dty2005 = dty.count('2005')
    dty2006 = dty.count('2006')
    dty2007 = dty.count('2007')
    dty2008 = dty.count('2008')
    dty2009 = dty.count('2009')
    dty2010 = dty.count('2010')
    dty2011 = dty.count('2011')
    dty2012 = dty.count('2012')
    dty2013 = dty.count('2013')
    dty2014 = dty.count('2014')
    dty2015 = dty.count('2015')
    dty2016 = dty.count('2016')
    dty2017 = dty.count('2017')
    dty2018 = dty.count('2018')
    dty2019 = dty.count('2019')
    dty2020 = dty.count('2020')
    dty2021 = dty.count('2021')
    dty2022 = dty.count('2022')

    if dty1994 != 0:
        procent_ncalls_1994 = str(round(float(dtcl_1994) / float(dty1994) * 100, 1))
    if dty1995 != 0:
        procent_ncalls_1995 = str(round(float(dtcl_1995) / float(dty1995) * 100, 1))
    if dty1996 != 0:
        procent_ncalls_1996 = str(round(float(dtcl_1996) / float(dty1996) * 100, 1))
    if dty1997 != 0:
        procent_ncalls_1997 = str(round(float(dtcl_1997) / float(dty1997) * 100, 1))
    if dty1998 != 0:
        procent_ncalls_1998 = str(round(float(dtcl_1998) / float(dty1998) * 100, 1))
    if dty1999 != 0:
        procent_ncalls_1999 = str(round(float(dtcl_1999) / float(dty1999) * 100, 1))
    if dty2000 != 0:
        procent_ncalls_2000 = str(round(float(dtcl_2000) / float(dty2000) * 100, 1))
    if dty2001 != 0:
        procent_ncalls_2001 = str(round(float(dtcl_2001) / float(dty2001) * 100, 1))
    if dty2002 != 0:
        procent_ncalls_2002 = str(round(float(dtcl_2002) / float(dty2002) * 100, 1))
    if dty2003 != 0:
        procent_ncalls_2003 = str(round(float(dtcl_2003) / float(dty2003) * 100, 1))
    if dty2004 != 0:
        procent_ncalls_2004 = str(round(float(dtcl_2004) / float(dty2004) * 100, 1))
    if dty2005 != 0:
        procent_ncalls_2005 = str(round(float(dtcl_2005) / float(dty2005) * 100, 1))
    if dty2006 != 0:
        procent_ncalls_2006 = str(round(float(dtcl_2006) / float(dty2006) * 100, 1))
    if dty2007 != 0:
        procent_ncalls_2007 = str(round(float(dtcl_2007) / float(dty2007) * 100, 1))
    if dty2008 != 0:
        procent_ncalls_2008 = str(round(float(dtcl_2008) / float(dty2008) * 100, 1))
    if dty2009 != 0:
        procent_ncalls_2009 = str(round(float(dtcl_2009) / float(dty2009) * 100, 1))
    if dty2010 != 0:
        procent_ncalls_2010 = str(round(float(dtcl_2010) / float(dty2010) * 100, 1))
    if dty2011 != 0:
        procent_ncalls_2011 = str(round(float(dtcl_2011) / float(dty2011) * 100, 1))
    if dty2012 != 0:
        procent_ncalls_2012 = str(round(float(dtcl_2012) / float(dty2012) * 100, 1))
    if dty2013 != 0:
        procent_ncalls_2013 = str(round(float(dtcl_2013) / float(dty2013) * 100, 1))
    if dty2014 != 0:
        procent_ncalls_2014 = str(round(float(dtcl_2014) / float(dty2014) * 100, 1))
    if dty2015 != 0:
        procent_ncalls_2015 = str(round(float(dtcl_2015) / float(dty2015) * 100, 1))
    if dty2016 != 0:
        procent_ncalls_2016 = str(round(float(dtcl_2016) / float(dty2016) * 100, 1))
    if dty2017 != 0:
        procent_ncalls_2017 = str(round(float(dtcl_2017) / float(dty2017) * 100, 1))
    if dty2018 != 0:
        procent_ncalls_2018 = str(round(float(dtcl_2018) / float(dty2018) * 100, 1))
    if dty2019 != 0:
        procent_ncalls_2019 = str(round(float(dtcl_2019) / float(dty2019) * 100, 1))
    if dty2020 != 0:
        procent_ncalls_2020 = str(round(float(dtcl_2020) / float(dty2020) * 100, 1))
    if dty2021 != 0:
        procent_ncalls_2021 = str(round(float(dtcl_2021) / float(dty2021) * 100, 1))
    if dty2022 != 0:
        procent_ncalls_2022 = str(round(float(dtcl_2022) / float(dty2022) * 100, 1))

    dtm1 = dtm.count('1')
    dtm2 = dtm.count('2')
    dtm3 = dtm.count('3')
    dtm4 = dtm.count('4')
    dtm5 = dtm.count('5')
    dtm6 = dtm.count('6')
    dtm7 = dtm.count('7')
    dtm8 = dtm.count('8')
    dtm9 = dtm.count('9')
    dtm10 = dtm.count('10')
    dtm11 = dtm.count('11')
    dtm12 = dtm.count('12')

    dtt0 = dtt.count('3')
    dtt1 = dtt.count('4')
    dtt2 = dtt.count('5')
    dtt3 = dtt.count('6')
    dtt4 = dtt.count('7')
    dtt5 = dtt.count('8')
    dtt6 = dtt.count('9')
    dtt7 = dtt.count('10')
    dtt8 = dtt.count('11')
    dtt9 = dtt.count('12')
    dtt10 = dtt.count('13')
    dtt11 = dtt.count('14')
    dtt12 = dtt.count('15')
    dtt13 = dtt.count('16')
    dtt14 = dtt.count('17')
    dtt15 = dtt.count('18')
    dtt16 = dtt.count('19')
    dtt17 = dtt.count('20')
    dtt18 = dtt.count('21')
    dtt19 = dtt.count('22')
    dtt20 = dtt.count('23')
    dtt21 = dtt.count('0')
    dtt22 = dtt.count('1')
    dtt23 = dtt.count('2')

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_hour = datetime.datetime.now()

    return render(request, 'main/qso_period.html', locals())


def rand(request):
    t1 = time.time()

    diff = ['OD5PL']

    qso = 0

    # Случайный выбор из следующего набора:

    fc = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'S', 'T', 'V', 'W', 'Y', 'Z']

    rfc = random.choice(fc)

    qd = Entry.objects.filter(callsign__iregex=r'^%s' % rfc)
    for entry in qd:

        if entry.callsign not in diff:
            diff.append(entry.callsign)

    random_ = random.choice(diff)  # Выбор случайного позывного из списка diff

    qcw = Entry.objects.filter(mode='CW')
    qssb = Entry.objects.filter(mode='SSB')
    qrtty = Entry.objects.filter(mode='RTTY')
    qpsk = Entry.objects.filter(mode='PSK')
    qft4 = Entry.objects.filter(mode='MFSK')
    qft8 = Entry.objects.filter(mode='FT8')

    data = random_

    if re.match(r'[\w/]{4,18}|\D\d\D$', data):

        q1 = Entry.objects.filter(callsign__iregex=r'^(.+/)?%s(/.+)?$' % data).order_by('-datetime')
        qso = q1.count()

        dupe = []  #
        no_dupes_qso = []  # Band+mode - not dupes!
        for entry in q1:
            if str(entry.band) + str(entry.mode) not in dupe:
                dupe.append(str(entry.band) + str(entry.mode))
                b = int(entry.id)
                no_dupes_qso.append(b)
        q2 = q1.filter(
            id__in=no_dupes_qso)  # Неповторяющиеся комбинации band-mode (количество уникальных (band-mode) QSO)

        if qso == 1 or qso == 0:
            qso_qsos = 'QSO'
        else:
            qso_qsos = 'QSOs'

        qso_160cw = qso_80cw = qso_40cw = qso_30cw = qso_20cw = qso_17cw = qso_15cw = qso_12cw = qso_10cw = 0
        qso_160ssb = qso_80ssb = qso_40ssb = qso_20ssb = qso_17ssb = qso_15ssb = qso_12ssb = qso_10ssb = 0
        qso_160rtty = qso_80rtty = qso_40rtty = qso_30rtty = qso_20rtty = qso_17rtty = qso_15rtty = qso_12rtty = qso_10rtty = 0
        qso_160psk = qso_80psk = qso_40psk = qso_30psk = qso_20psk = qso_17psk = qso_15psk = qso_12psk = qso_10psk = 0
        qso_160ft4 = qso_80ft4 = qso_40ft4 = qso_30ft4 = qso_20ft4 = qso_17ft4 = qso_15ft4 = qso_12ft4 = qso_10ft4 = 0
        qso_160ft8 = qso_80ft8 = qso_40ft8 = qso_30ft8 = qso_20ft8 = qso_17ft8 = qso_15ft8 = qso_12ft8 = qso_10ft8 = 0

        if qso:

            q_160 = q1.filter(band='2')
            if q_160:
                qso_160cw = q_160.filter(mode='CW').count()
                qso_160ssb = q_160.filter(mode='SSB').count()
                qso_160rtty = q_160.filter(mode='RTTY').count()
                qso_160psk = q_160.filter(mode='PSK').count()
                qso_160ft4 = q_160.filter(mode='MFSK').count()
                qso_160ft8 = q_160.filter(mode='FT8').count()

            q_80 = q1.filter(band='4')
            if q_80:
                qso_80cw = q_80.filter(mode='CW').count()
                qso_80ssb = q_80.filter(mode='SSB').count()
                qso_80rtty = q_80.filter(mode='RTTY').count()
                qso_80psk = q_80.filter(mode='PSK').count()
                qso_80ft4 = q_80.filter(mode='MFSK').count()
                qso_80ft8 = q_80.filter(mode='FT8').count()

            q_40 = q1.filter(band='7')
            if q_40:
                qso_40cw = q_40.filter(mode='CW').count()
                qso_40ssb = q_40.filter(mode='SSB').count()
                qso_40rtty = q_40.filter(mode='RTTY').count()
                qso_40psk = q_40.filter(mode='PSK').count()
                qso_40ft4 = q_40.filter(mode='MFSK').count()
                qso_40ft8 = q_40.filter(mode='FT8').count()

            q_30 = q1.filter(band='10')
            if q_30:
                qso_30cw = q_30.filter(mode='CW').count()
                qso_30rtty = q_30.filter(mode='RTTY').count()
                qso_30psk = q_30.filter(mode='PSK').count()
                qso_30ft4 = q_30.filter(mode='MFSK').count()
                qso_30ft8 = q_30.filter(mode='FT8').count()

            q_20 = q1.filter(band='14')
            if q_20:
                qso_20cw = q_20.filter(mode='CW').count()
                qso_20ssb = q_20.filter(mode='SSB').count()
                qso_20rtty = q_20.filter(mode='RTTY').count()
                qso_20psk = q_20.filter(mode='PSK').count()
                qso_20ft4 = q_20.filter(mode='MFSK').count()
                qso_20ft8 = q_20.filter(mode='FT8').count()

            q_17 = q1.filter(band='18')
            if q_17:
                qso_17cw = q_17.filter(mode='CW').count()
                qso_17ssb = q_17.filter(mode='SSB').count()
                qso_17rtty = q_17.filter(mode='RTTY').count()
                qso_17psk = q_17.filter(mode='PSK').count()
                qso_17ft4 = q_17.filter(mode='MFSK').count()
                qso_17ft8 = q_17.filter(mode='FT8').count()

            q_15 = q1.filter(band='21')
            if q_15:
                qso_15cw = q_15.filter(mode='CW').count()
                qso_15ssb = q_15.filter(mode='SSB').count()
                qso_15rtty = q_15.filter(mode='RTTY').count()
                qso_15psk = q_15.filter(mode='PSK').count()
                qso_15ft4 = q_15.filter(mode='MFSK').count()
                qso_15ft8 = q_15.filter(mode='FT8').count()

            q_12 = q1.filter(band='25')
            if q_12:
                qso_12cw = q_12.filter(mode='CW').count()
                qso_12ssb = q_12.filter(mode='SSB').count()
                qso_12rtty = q_12.filter(mode='RTTY').count()
                qso_12psk = q_12.filter(mode='PSK').count()
                qso_12ft4 = q_12.filter(mode='MFSK').count()
                qso_12ft8 = q_12.filter(mode='FT8').count()

            q_10 = q1.filter(band='28')
            if q_10:
                qso_10cw = q_10.filter(mode='CW').count()
                qso_10ssb = q_10.filter(mode='SSB').count()
                qso_10rtty = q_10.filter(mode='RTTY').count()
                qso_10psk = q_10.filter(mode='PSK').count()
                qso_10ft4 = q_10.filter(mode='MFSK').count()
                qso_10ft8 = q_10.filter(mode='FT8').count()

            total_160 = qso_160cw + qso_160ssb + qso_160rtty + qso_160psk + qso_160ft4 + qso_160ft8
            total_80 = qso_80cw + qso_80ssb + qso_80rtty + qso_80psk + qso_80ft4 + qso_80ft8
            total_40 = qso_40cw + qso_40ssb + qso_40rtty + qso_40psk + qso_40ft4 + qso_40ft8
            total_30 = qso_30cw + qso_30rtty + qso_30psk + qso_30ft4 + qso_30ft8
            total_20 = qso_20cw + qso_20ssb + qso_20rtty + qso_20psk + qso_20ft4 + qso_20ft8
            total_17 = qso_17cw + qso_17ssb + qso_17rtty + qso_17psk + qso_17ft4 + qso_17ft8
            total_15 = qso_15cw + qso_15ssb + qso_15rtty + qso_15psk + qso_15ft4 + qso_15ft8
            total_12 = qso_12cw + qso_12ssb + qso_12rtty + qso_12psk + qso_12ft4 + qso_12ft8
            total_10 = qso_10cw + qso_10ssb + qso_10rtty + qso_10psk + qso_10ft4 + qso_10ft8

            total_cw = qso_160cw + qso_80cw + qso_40cw + qso_30cw + qso_20cw + qso_17cw + qso_15cw + qso_12cw + qso_10cw
            total_ssb = qso_160ssb + qso_80ssb + qso_40ssb + qso_20ssb + qso_17ssb + qso_15ssb + qso_12ssb + qso_10ssb
            total_rtty = qso_160rtty + qso_80rtty + qso_40rtty + qso_30rtty + qso_20rtty + qso_17rtty + qso_15rtty + qso_12rtty + qso_10rtty
            total_psk = qso_160psk + qso_80psk + qso_40psk + qso_30psk + qso_20psk + qso_17psk + qso_15psk + qso_12psk + qso_10psk
            total_psk = qso_160ft4 + qso_80ft4 + qso_40ft4 + qso_30ft4 + qso_20ft4 + qso_17ft4 + qso_15ft4 + qso_12ft4 + qso_10ft4
            total_psk = qso_160ft8 + qso_80ft8 + qso_40ft8 + qso_30ft8 + qso_20ft8 + qso_17ft8 + qso_15ft8 + qso_12ft8 + qso_10ft8
            # Определение страны по позывному.

            if re.match(r'[\w/]{4,18}|\D\d\D$', data):
                cl = []
                pref = []
                qc = Cty.objects.all()
                callsign = data

                callsign = str(callsign.upper())

                for i in range(1, len(callsign) + 1):
                    call = callsign[:i]
                    for entry in qc:

                        line = entry.pref

                        if ' ' + str(call) + ',' in line or ',' + str(call) + ',' in line or ' ' + str(
                                call) + ':' in line or ',' + str(call) + ';' in line or ' ' + str(
                            call) + ';' in line or ',' + str(call) + '(' in line or '=' + str(
                            call) + '(' in line or '=' + str(call) + ',' in line or '=' + str(
                            call) + '[' in line or ',' + str(call) + '[' in line:

                            cll = str(entry.cty)

                            if cll not in cl:
                                cl.append(cll)
                                if callsign[:i] not in pref:
                                    pref.append(callsign[:i])
                            cname = cl.pop() + ','

                            cont_short = ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA', ]
                            cont_long = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania',
                                         'South America']
                            for l in range(len(cont_short)):
                                if entry.cont == cont_short[l]:
                                    cont = cont_long[l]
                                    cnam = cname[:-1]
                                    if cname == 'European Russia,' or cname == 'European Turkey,' or cname == 'Asiatic Russia,' or cname == 'Asiatic Turkey,' or cname == 'South Africa,' or cname == 'Antarctica,':
                                        cname = cnam
                                        cont = ''

                    # Блок исключений - 2 шт.

                    if re.match(r'^[ru].+[8,9,0]$', callsign, re.I):  # 1 call/9 - Asiatic Russia
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA9')

                    if re.match(r'^[ru].+[1,3-7]$', callsign, re.I):  # 2 /1
                        cll = 'European Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA')

                    if re.match(r'^(r|u).+2$', callsign, re.I):  # 3 /R2
                        cll = 'Kaliningrad'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA2F')

                    if re.match(r'^(ta|tb|tc|ym).+/[0,2-9]$', callsign, re.I):  # 4 /0
                        cll = 'Asiatic Turkey'
                        cl.append(cll)
                        cname = cl.pop()

                    if re.match(r'^(ta|tb|tc|ym).+/1$', callsign, re.I):  # 5 /1
                        cll = 'European Turkey'
                        cl.append(cll)
                        cname = cl.pop()

                    if re.search(r'.+/ant$', callsign, re.I):  # 6 /ant
                        cll = 'Antarctica'
                        cl.append(cll)
                        cname = cl.pop()
                        cont = ''

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/[0-7]$', callsign, re.I):  # 6
                        cll = 'Spain'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('EA')

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/8$', callsign, re.I):  # 7
                        cll = 'Canary Islands'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('EA8')

                    if re.match(r'^(am|an|ao|ea|eb|ec|ed|ee|ef|eg|eh).+/9$', callsign, re.I):  # 8
                        cll = 'Ceuta & Melilla'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('EA9')

                    if re.search(r'.+(/R3|/R4)$', callsign, re.I):  # 6 /r3, /r4
                        cll = 'European Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('R')

                    if re.search(r'.+(/R9|/R0|/R9Z)$', callsign, re.I):  # 6
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA9')

                    if re.search(r'.+(/RA|/RA9(F|G)|/R9(F|G)|/UA9(F|G))$', callsign, re.I):  # 6
                        cll = 'European Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA')

                    if re.search(r'.+(/RA9)$', callsign, re.I):  # 6
                        cll = 'Asiatic Russia'
                        cl.append(cll)
                        cname = cl.pop()
                        pref.append('RA9')

                    pr = ['/TF', '/DU7', '/SV9', '/JD1', '/C6A', '/PT2', '/NH2', '/VY2', '/HI9', '/KH0', '/YU8', '/IH9',
                          '/OH0', '/EA6', '/KL7', '/KH6', '/I2', '/VE3', '/KH2', 'T00CW', 'T00SW', 'T00RM', '/VK9L',
                          '/ANT']

                    countrys = ['Iceland', 'Philippines', 'Crete', 'Ogasawara', 'Bahamas', 'Brazil', 'Guam', 'Canada',
                                'Dominican Republic', 'Mariana Islands', 'Kosovo', 'African Italy', 'Aland Islands',
                                'Balearic Islands', 'Alaska', 'Hawaii', 'Italy', 'Canada', 'Guam',
                                'Principality of Seborga, Europe', 'Principality of Seborga, Europe',
                                'Principality of Seborga, Europe', 'Lord Howe Island', 'Antarctica']

                    # print len(pr),len(countrys) # Длины списков должны совпадать!

                    for k in range(len(pr)):
                        if re.search(pr[k], callsign, re.I):
                            cll = countrys[k]
                            cl.append(cll)
                            if qso:
                                cname = cl.pop()
                                if 'T00' not in pr[k]:
                                    pref.append(pr[k][1:])  # Префикс показываем без знака "/"
                                else:
                                    pref.append(pr[k][0:])

                if pref:
                    prefix = pref.pop()
                    t2 = time.time()
                    t_random = str(t2 - t1)[:4] + ' sec'
                else:
                    pass

    return render(request, 'main/random.html', locals())


''' def my_image(request):

    from django.http import HttpResponse
    image_data = open('1.png', "rb").read()
    return HttpResponse(image_data, content_type="image/png") '''

'''import csv

UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,
281,304,203, 134, 147]
def unruly_passengers_csv(request):

    response - HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename^unruly.csv'

    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2007), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response'''


# @cache_page(60)
def call_allbands(request):
    t1 = time.time()

    diff_calls = []
    call_on160 = []
    call_on80 = []
    call_on40 = []
    call_on20 = []
    call_on15 = []
    call_on10 = []
    call_allbands = []

    q_diff = Entry.objects.all()  # Список QSO

    cl_160 = q_diff.filter(band='2')
    for entry in cl_160:
        if entry.callsign not in call_on160:
            call_on160.append(entry.callsign)

    cl_80 = q_diff.filter(band='4')
    for entry in cl_80:
        if entry.callsign not in call_on80:
            call_on80.append(entry.callsign)

    cl_40 = q_diff.filter(band='7')
    for entry in cl_40:
        if entry.callsign not in call_on40:
            call_on40.append(entry.callsign)

    cl_20 = q_diff.filter(band='14')
    for entry in cl_20:
        if entry.callsign not in call_on20:
            call_on20.append(entry.callsign)

    cl_15 = q_diff.filter(band='21')
    for entry in cl_15:
        if entry.callsign not in call_on15:
            call_on15.append(entry.callsign)

    cl_10 = q_diff.filter(band='28')
    for entry in cl_10:
        if entry.callsign not in call_on10:
            call_on10.append(entry.callsign)

    for item in call_on160:
        if item in call_on80 and item in call_on40 and item in call_on20 and item in call_on15 and item in call_on10:
            call_allbands.append(item)
    call_allbands.sort()
    len_call_allbands = len(call_allbands)

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_max = datetime.datetime.now()

    return render(request, 'main/call_allbands.html', locals())


# @cache_page(60)
def call_allmode(request):
    t1 = time.time()

    diff_calls = []
    call_oncw = []
    call_onssb = []
    call_onrtty = []
    call_onpsk = []
    call_onft4 = []
    call_onft8 = []
    call_allmode = []

    q_diff = Entry.objects.all()  # Список QSO

    cl_cw = q_diff.filter(mode='CW')
    for entry in cl_cw:
        if entry.callsign not in call_oncw:
            call_oncw.append(entry.callsign)

    cl_ssb = q_diff.filter(mode='SSB')
    for entry in cl_ssb:
        if entry.callsign not in call_onssb:
            call_onssb.append(entry.callsign)

    cl_rtty = q_diff.filter(mode='RTTY')
    for entry in cl_rtty:
        if entry.callsign not in call_onrtty:
            call_onrtty.append(entry.callsign)

    cl_psk = q_diff.filter(mode='PSK')
    for entry in cl_psk:
        if entry.callsign not in call_onpsk:
            call_onpsk.append(entry.callsign)

    cl_ft4 = q_diff.filter(mode='MFSK')
    for entry in cl_ft4:
        if entry.callsign not in call_onft4:
            call_onft4.append(entry.callsign)

    cl_ft8 = q_diff.filter(mode='FT8')
    for entry in cl_ft8:
        if entry.callsign not in call_onft8:
            call_onft8.append(entry.callsign)

    for item in call_onpsk:
        if item in call_oncw and item in call_onssb and item in call_onrtty and item in call_onft4 and item in call_onft8:
            call_allmode.append(item)
    call_allmode.sort()
    len_call_allmode = len(call_allmode)

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_max = datetime.datetime.now()

    return render(request, 'main/call_allmode.html', locals())


# @cache_page(60) # 60сек
def call_allbands_mode(request):
    t1 = time.time()

    call_allbands_mode = []

    diff_calls = []
    call_oncw = []
    call_onssb = []
    call_onrtty = []
    call_onpsk = []
    call_onft4 = []
    call_onft8 = []
    call_allmode = []

    q_diff = Entry.objects.all()  # Список QSO

    cl_cw = q_diff.filter(mode='CW')
    for entry in cl_cw:
        if entry.callsign not in call_oncw:
            call_oncw.append(entry.callsign)

    cl_ssb = q_diff.filter(mode='SSB')
    for entry in cl_ssb:
        if entry.callsign not in call_onssb:
            call_onssb.append(entry.callsign)

    cl_rtty = q_diff.filter(mode='RTTY')
    for entry in cl_rtty:
        if entry.callsign not in call_onrtty:
            call_onrtty.append(entry.callsign)

    cl_psk = q_diff.filter(mode='PSK')
    for entry in cl_psk:
        if entry.callsign not in call_onpsk:
            call_onpsk.append(entry.callsign)

    cl_ft4 = q_diff.filter(mode='MFSK')
    for entry in cl_ft4:
        if entry.callsign not in call_onft4:
            call_onft4.append(entry.callsign)

    cl_ft8 = q_diff.filter(mode='FT8')
    for entry in cl_ft8:
        if entry.callsign not in call_onft8:
            call_onft8.append(entry.callsign)

    for item in call_onpsk:
        if item in call_oncw and item in call_onssb and item in call_onrtty and item in call_onft4 and item in call_onft8:
            call_allmode.append(item)
    call_allmode.sort()

    len_call_allmode = len(call_allmode)

    diff_calls = []
    call_on160 = []
    call_on80 = []
    call_on40 = []
    call_on20 = []
    call_on15 = []
    call_on10 = []
    call_allbands = []

    q_diff = Entry.objects.all()  # Список QSO

    cl_160 = q_diff.filter(band='2')
    for entry in cl_160:
        if entry.callsign not in call_on160:
            call_on160.append(entry.callsign)

    cl_80 = q_diff.filter(band='4')
    for entry in cl_80:
        if entry.callsign not in call_on80:
            call_on80.append(entry.callsign)

    cl_40 = q_diff.filter(band='7')
    for entry in cl_40:
        if entry.callsign not in call_on40:
            call_on40.append(entry.callsign)

    cl_20 = q_diff.filter(band='14')
    for entry in cl_20:
        if entry.callsign not in call_on20:
            call_on20.append(entry.callsign)

    cl_15 = q_diff.filter(band='21')
    for entry in cl_15:
        if entry.callsign not in call_on15:
            call_on15.append(entry.callsign)

    cl_10 = q_diff.filter(band='28')
    for entry in cl_10:
        if entry.callsign not in call_on10:
            call_on10.append(entry.callsign)

    for item in call_on160:
        if item in call_on80 and item in call_on40 and item in call_on20 and item in call_on15 and item in call_on10:
            call_allbands.append(item)
    call_allbands.sort()
    len_call_allbands = len(call_allbands)

    for item in call_allmode:
        if item in call_allbands:
            call_allbands_mode.append(item)

    len_call_allbands_mode = len(call_allbands_mode)

    t2 = time.time()
    tt = str(t2 - t1)[:5]
    date_max = datetime.datetime.now()

    return render(request, 'main/call_allbands_mode.html', locals())
