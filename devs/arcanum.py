arcanorum = open('devs/arcanorum.txt').read()

class Arcanum(dict):
    """
        ProjectSecret is the class to handle all of the secrets
        such as passwords, links, ids, etc..
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.remote_url = ''
        self.local_folder = ''

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



#
