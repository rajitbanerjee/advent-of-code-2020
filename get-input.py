#!/usr/bin/env python
"""
Usage
-----

1. Make directory containing day number, e.g. `./2020/day-<day>-<problem-name>`
2. Run `$ ./get-input 2020` to download all input so far for given year.
3. Alternatively, run script without arguments `$ ./get-input` to download the current year's input by default.

"""

from datetime import datetime
from pathlib import Path
import os
import sys

import requests

# remember to store session cookie as environment var before running script
SESSION_COOKIE = os.environ['AOC_COOKIE']


def getInput(year, day):
    try:
        for d in Path(f'./{year}/').iterdir():
            if str(day) in str(d)[4:]:
                folder = d
                break
        outpath = folder/Path(f'day{day}.in')

        if not outpath.exists():
            url = f'https://adventofcode.com/{year}/day/{day}/input'
            headers = {'Cookie': f'session={SESSION_COOKIE}'}

            r = requests.get(url, headers=headers)
            with open(outpath, 'wb') as f:
                f.write(r.content)

            print(f'Input downloaded: {outpath}')
        else:
            print(f'Input file already exists: {outpath}')

    except:
        print(f'{year}, day {day}: Error! Check if cookie is valid, input is available, and problem folder has been created.')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
    else:
        year = datetime.today().year

    for day in range(1, 26):
        if datetime(year=year, month=12, day=day) <= datetime.today():
            getInput(year, day)
