import time


class StopWatch:

    def __init__(self):
        ''' Initialises a StopWatch object'''
        self.start_time = None
        self.end_time = None

    def __repr__(self):
        '''Represents the object in a readable format'''
        return 'Time Elapsed: %r' % ':'.join((self.convertSeconds(self.result)))

    def start(self):
        ''' Start the StopWatch '''
        self.start_time = time.time()

    def stop(self):
        ''' Stop the StopWatch'''
        self.end_time = time.time()
        pass

    def split(self):
        '''Starts a split timer'''
        self.split_start_time = time.time()
        pass

    def unsplit(self):
        '''Stops the split timer, returns time elapsed since split'''
        self.result = time.time() - self.split_start_time
        return self.__repr__()

    def time_elapsed(self):
        '''Time elapsed since last start'''
        self.result = time.time() - self.start_time
        return self.__repr__()

    def total_runtime(self):
        '''Time elapsed between Start and Stop'''
        self.result = self.end_time - self.start_time
        return self.__repr__()

    def convertSeconds(self, seconds):
        '''Converts seconds into hours and minutes'''
        h = int(seconds//(60*60))
        m = int((seconds-h*60*60)//60)
        s = round(seconds-(h*60*60)-(m*60), 2)
        
        h = str(h) + 'h'
        m = str(m) + 'm'
        s = str(s) + 's'
        
        return h.strip('.'), m.strip('.'), s
