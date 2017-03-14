import threading

class Racer(threading.Thread):
	
  def __init__(self, name, start_signal):
    threading.Thread.__init__(self, name=name)
    self.start_signal = start_signal
	
  def run(self):
    self.start_signal.wait()
    print("I, {}, got to the goal!".format(self.name))
	
class Race:

  def __init__(self, racer_names):
    """If the internal flag is true on entry, return immediately. Otherwise,
	block until another thread calls set() to set the flag to true, or 
	until the optional timeout occurs. When the timeout argument is present
	and not None, it should be a floating point number specifying a timeout
	for the operation in seconds (or fractions thereof). This method returns the
	internal flag on exit, so it will always return True except if a timeout
	is given and the operation times out.
	"""
    self.start_signal = threading.Event()
    self.racers = [Racer(name, self.start_signal) for name in racer_names]
    for racer in self.racers:
      racer.start()

  def start(self):
    self.start_signal.set()

def __main__():
  race = Race(["rabbit", "turtle", "cheetah", "monkey", "cow", "horse", "tiger", "lion"])
  race.start()    

if __name__ == "__main__":
  __main__()
