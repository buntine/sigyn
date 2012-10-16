
from twisted.internet import task
from twisted.internet import reactor

from lib import sigyn, config

# Read main config.
conf = config.Conf()
conf.read("main")

# Start event loop.
s = sigyn.Sigyn()
t = task.LoopingCall(s.check)
t.start(conf.get("interval", 60))
reactor.run()
