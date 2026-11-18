import json
import xml.etree.ElementTree as ET

def decode(body, headers):
    return [{'key': str(x['id']), 'value': x} for x in json.loads(body)['value']]
