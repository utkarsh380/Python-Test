#Setup a dict structure like this in python
di = {"Q":73,"R":85,"S":44}
def maxDect(di):
    d=dict()
    max_key = max(di, key=di.get)
    d[max_key]=di[max_key]
    return d
print(maxDect(di))
