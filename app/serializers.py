import json


class Serializer(object):
    @classmethod
    def get(cls, obj):
        return json.dumps(obj, indent=4)
