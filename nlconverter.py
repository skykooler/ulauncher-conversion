import re

prefixes = {
    "yocto": 0.000000000000000000000001,
    "zepto": 0.000000000000000000001,
    "atto": 0.000000000000000001,
    "femto": 0.000000000000001,
    "pico": 0.000000000001,
    "nano": 0.000000001,
    "micro": 0.000001,
    "milli": 0.001,
    "centi": 0.01,
    "deci": 0.1,
    "deca": 10,
    "hecto": 100,
    "kilo": 1000,
    "mega": 1000000,
    "giga": 1000000000,
    "tera": 1000000000000,
    "peta": 1000000000000000,
    "exa": 1000000000000000000,
    "zetta": 1000000000000000000000,
    "yotta": 1000000000000000000000000
}

def convert(query):
    result = re.match(r'([\d\.\-]+) ?(.*) to (.*)', query)
    if result:
        value, start, end = result.group(1), result.group(2), result.group(3)
    else:
        return None
    prefix = 1
    #for i in prefixes:
    #    if start.startswith(i):
    #        start = start[len(i):]
    #        prefix *= prefixes[i]

    output = 
    print ("Start: %s, end: %s" %(start, end))
