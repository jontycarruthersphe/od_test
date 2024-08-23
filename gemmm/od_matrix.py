# -*- coding: utf-8 -*-


class OriginDestination:
    def __new__(cls, msoas=None, day_type=None, path=None):
        if path is not None:
            #print('Loading existing sample')
            return super().__new__(ODLoader)
            
        elif (msoas is not None) & (day_type is not None):
            #print('Generating samples')
            return super().__new__(ODSampler)
            
        else:
            raise ValueError('Either provide a path to existing samples or a list of MSOAs and day_type to generate new samples.')

            
            
class ODSampler(OriginDestination):    
    def __init__(self, msoas, day_type):
        '''
        msoas (list): A list of MSOAs to generate numbers of journeys between
        day_type (str): either 'weekday' or 'weekend'
        '''
        self.message = 'I am a sampler'
        
        
        
class ODLoader(OriginDestination):
     def __init__(self, path):
        '''
        path (str or pathlib.Path): path to the directory where the samples are saved
        '''
        self.message = 'I am a loader'
