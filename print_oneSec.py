import signal


def printer(signum, frame):
    print(":-)")


signal.signal(signal.SIGALRM, printer)
signal.setitimer(signal.ITIMER_REAL, 0.1, 3.0)


while True:
    signal.pause()


# while True:
    # signal.signal(signal.SIGALRM,handler())
    #handler =signal.signal(enum_to_int(signalnum), enum_to_int(handler))
   #   signal.SIGALRM
    #  signal.alarm(handler())

    # signal.alarm(1)
