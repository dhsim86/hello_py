#!/usr/bin/env python

from rx.subjects import Subject

print("---------------------")
print("subject subscribe")

stream = Subject()
stream.on_next(41)

d = stream.subscribe(lambda x: print("Got: %s" % x))
stream.on_next(42)

d.dispose()
stream.on_next(43)
