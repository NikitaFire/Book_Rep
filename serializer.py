import json
import xml.etree.ElementTree as et

class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='UTF-8', method='xml').decode('utf-8')


class SerializerFactory:
    def get_serializer(self, format):
        serializers = {
            'JSON': JsonSerializer,
            'XML': XmlSerializer
        }
        serializer_class = serializers.get(format)
        if serializer_class:
            return serializer_class()
        else:
            raise ValueError(f"Unsupported format: {format}")


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

