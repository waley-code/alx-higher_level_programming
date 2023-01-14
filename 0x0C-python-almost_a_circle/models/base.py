#!/usr/bin/python3
"""This is the base class module"""
import json
import csv

class Base:
    """The Base class"""
    __nb_objects = 0

    
    def __init__(self, id=None):
        """Instantiate id vairable"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries or list_dictionaries != None:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])
    
    @staticmethod
    def from_json_string(json_string):
        if json_string or json_string != None:
            return json.load(json_string)
        else:
            return json.load([])

    @classmethod
    def save_to_file(cls, list_objs):
        xY = []
        if list_objs != None and len(list_objs) > 0:
            for i in list_objs:
                    xY.append(type(i).to_dictionary(i))
            with open(cls.__name__+".json",'w') as fp:
                fp.write(Base.to_json_string(xY))
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        with open(cls.__name__+".json",'r', encoding="utf-8") as fp:
            return Base.from_json_string(fp)
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        formatOfCsv = []
        with open(cls.__name__+".csv",'w') as fp:
            if cls.__name__ == "Rectangle":
                formatOfCsv = ["id", "width", "height", "x", "y"]
            if cls.__name__ == "Square":
                formatOfCsv = ["id", "size", "x", "y"]
            writer = csv.DictWriter(fp, fieldnames=formatOfCsv)
            for i in list_objs:
                writer.writerow(i.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        formatOfCsv = []
        try:
            with open(cls.__name__+".csv",'r') as fp:
                if cls.__name__ == "Rectangle":
                    formatOfCsv = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    formatOfCsv = ["id", "size", "x", "y"]
                writer = csv.DictReader(fp, fieldnames=formatOfCsv)
                new = [dict([ke , value] for ke , value in g.items()) for g in writer]
                return [cls.create(**i) for i in new]
        except Exception:
            return []