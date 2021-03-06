import os
import json

def gen_months(months, year, timetable):
    for mdate,mname in enumerate(months, start=1):
        m = f'{mdate}_{mname}_{year}'
        os.mkdir(m)
        d = 1

        for i in range(4):
            with open(f'{m}/{i}.json', 'w') as file:
                file.write(json.dumps(timetable(f"2021-{mdate}-{d}", f"2021-{mdate}-{d+6}")))
            d+=1+6


def gen_month(mname, mdate, year, timetable):
    m=f'{mname}_{mdate}_{year}'
    os.mkdir(m)

    for i in range(4):
        d = 1
        with open(f'{m}/{i}.json', 'w') as file:
            file.write(json.dumps(timetable(f"{year}-{mdate}-{d}", f"{year}-{mdate}-{d+6}")))
        d+=1+6
