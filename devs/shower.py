class Shower(dict):
    """
        Tester is DEVS' tool of testing stuff in the universe
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
