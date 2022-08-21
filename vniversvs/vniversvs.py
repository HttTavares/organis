from devs.topos import Topos
from devs.kronos import Kronos
from devs.aleph import Aleph
from vniversvs.task import Task
import pandas as pd

class VNIVERSVS(dict):
    """
        vniversvs is where everything is and happens
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.objects = {
            ### PLACE EVERY CLASS HERE LIKE SO:
            # 'ClassName': class
            'Task': Task,
        }


    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__




##########################################################################################
# OBJECT HANDLING #########################################################################################
##########################################################################################

    def create_object( self, object_name, object_initialization_data ):
        try:
            object = self.objects[object_name](
                initialization_data = object_initialization_data,
            )
        except:
            object = self.objects[object_name]()
        if object_name not in self.topos:
            self.topos[object_name] = {}
        self.topos[object_name][object_initialization_data['name']] = object
        # print(self.topos[object_name][object_initialization_data['name']    ])
        self.devs.make_object_metadata(object)
        return object

    def read_object( self, object_id ):
        object = None
        for object_name in self.topos:
            if object_id in self.topos.object_name:
                object = self.topos.object_name[object_id]
        if object == None:
            print('read_object method returned None')
        return object

    # def update_object( self, object_id, new_object_data ):
    #     try:
    #         object = self.read_object( object_id )
    #         for attribute_name in new_object_data.keys():
    #             object.attribute = new_object_data[ attribute ]
    #     except:
    #         print('Could not find object', object_name)
    #
    # def delete_object( self, object_name ):
    #     try:
    #         for collection_name in self.collections.keys():
    #             if object_name in self.collections[collection_name].keys():
    #                 self.collections[collection_name].pop(object_name)
    #     except:
    #         print('could not find object', object_name)





#
