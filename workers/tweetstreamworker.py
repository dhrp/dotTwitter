__author__ = 'thatcher'

import tweetstream

### sample 1, works!
#stream = tweetstream.SampleStream("dhr_p", "Portishead")
#for tweet in stream:
#    print tweet
### end of sample 1

### sample 2, works!

### end of sample 2



#!/usr/bin/env python

import sys
import time
import signal

# Callback called when you run `supervisorctl stop'
def sigterm_handler(signum, frame):
    print >> sys.stderr, "Kaboom Baby!"
    sys.exit(0)

def main():
    words = ["Climate"]
    people = [123,124,125]
    locations = ["-122.75,36.8", "-121.75,37.8"]

    #with tweetstream.FilterStream("dhr_p", "Portishead", track=words, follow=people, locations=locations) as stream:
    with tweetstream.FilterStream("dhr_p", "Portishead", track=words) as stream:
        for tweet in stream:
            print tweet["text"] + "\n"
#            print "Got interesting tweet:", tweet


#    while True:
#        print >> sys.stderr, "Tick"
#        time.sleep(1)

# Bind our callback to the SIGTERM signal and run the daemon:
signal.signal(signal.SIGTERM, sigterm_handler)
main()