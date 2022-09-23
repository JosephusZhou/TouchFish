import sxtwl
from datetime import datetime, timedelta
from itertools import accumulate


# 求时间差
def calculate(dateStr):
    date = datetime.strptime(dateStr, '%Y-%m-%d')
    now = datetime.now()
    diff = date - now
    return diff.days

# 农历转国历
def lunar_to_national(year, month, day):
    day = sxtwl.fromLunar(year, month, day)
    return f'{day.getSolarYear()}-{day.getSolarMonth()}-{day.getSolarDay()}'

# 假期时间差
def holiday_diffs(year):
    holidays = {
        '元旦' : f'{year}-01-01',
        '春节' : lunar_to_national(year, 1, 1),
        '清明' : f'{year}-04-05',
        '五一' : f'{year}-05-01',
        '端午' : lunar_to_national(year, 5, 5),
        '中秋' : lunar_to_national(year, 8, 15),
        '国庆' : f'{year}-10-01'
    }
    diffs = {}
    for key, value in holidays.items():
        diffs[key] = calculate(value)
    return diffs

def now():
    now = datetime.now()
    return now.date()

def now_time():
    now = datetime.now()
    time = now.time().hour
    if time < 6:
        return "凌晨好"
    if 6 <= time <= 12:
        return "早上好"
    if 12 < time <= 13:
        return "中午好"
    if 13 < time <= 18:
        return "下午好"
    if 18 < time < 23:
        return "晚上好"

def week_diff():
    now = datetime.now()
    dayOfWeek = now.isoweekday()
    diff = 5 - dayOfWeek
    if diff < 0:
        print('都他么周末了你还玩这个？？？')
        exit(0)
    else:
        return diff


def fish():

    cur_year = datetime.now().year
    next_year = datetime.now().year + 1

    cur_diffs = holiday_diffs(cur_year)
    next_diffs = holiday_diffs(next_year)

    diffs = {}
    for key, value in cur_diffs.items():
        if value < 0:
            diffs[key] = next_diffs[key]
        else:
            diffs[key] = cur_diffs[key]
    diffs = {k: v for k, v in sorted(diffs.items(), key=lambda item: item[1])}

    holidays_str = ''
    for key, value in diffs.items():
        holidays_str += '距离' + key + '假期还有' + str(value) + '天\n'

    print("""【摸鱼办】提醒您：
""" + str(now()) +  str(now_time()) +"""，摸鱼人！
工作再累，一定不要忘记摸鱼哦！
有事没事起身去茶水间，去厕所，去廊道走走
别老在工位上坐着，钱是老板的,但命是自己的

距离周末还有""" + str(week_diff()) + """天
""" + holidays_str + """
小tips1：上班害怕摸鱼的人,永远在山下徘徊(⑉･̆-･̆⑉)
小tips2：以前摸鱼是偷懒，现在摸鱼是偷生！

上班是帮老板赚钱，摸鱼是赚老板的钱！
眼观六路，耳听八方，随时注意同事动态，领导动态，优雅喝水，从容拉屎。
摸鱼，高深且莫测，重点在于你的中二晚期有多严重，想象力有多大，胆子有多肥，
只要胆子大天天寒暑假不是没有道理的，只要混的棒摸鱼都不怕。

最后，祝愿天下所有摸鱼人，都能愉快的渡过每一天""")