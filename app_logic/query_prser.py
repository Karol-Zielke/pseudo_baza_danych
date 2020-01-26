import re

# CREATE DOCUMENT nazwa_dokumentu (kolumna1, kolumna2...)
# ADD (wartosc1, wartosc2...) TO nazwa_dokumentu
# SELECT (kolumna/*) FROM nazwa_dokumentu
from app_logic.app_commands import COMMANDS


class QueryParser:
    def parse(self, query):
        for key, value in COMMANDS.items():
            parsed = re.findall(value['regex'], query)
            if len(parsed) == 0:
                continue
            object_to_return = {
                'command': key,
            }
            parsed = parsed[0]
            for index in range(len(parsed)):
                object_to_return[value['order'][index]] = parsed[index]
            return object_to_return
