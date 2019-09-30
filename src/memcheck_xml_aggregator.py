"""
Aggregate information from Valgrind's Memcheck XML output.
"""
import json
import xml.etree.ElementTree as ET

class Aggregation:
    """An aggregation of one or several Memcheck executions."""

    def __init__(self):
        self.nb_errors = 0
        self.nb_invalid_frees = 0
        self.nb_invalid_jumps = 0
        self.nb_invalid_reads = 0
        self.nb_invalid_writes = 0
        self.nb_leaked_blocks = 0
        self.nb_leaked_bytes = 0
        self.nb_mismatched_frees = 0
        self.nb_uninit_uses = 0

    @staticmethod
    def parse(root):
        agg = Aggregation()
        for error in root.iter('error'):
            agg.nb_errors = agg.nb_errors + 1
            kind = error.findtext('kind')

            if kind.startswith('Uninit'):
                agg.nb_uninit_uses += 1
            elif kind.startswith('Leak_'):
                xwhat = error.find('xwhat')
                agg.nb_leaked_bytes += int(xwhat.findtext('leakedbytes'))
                agg.nb_leaked_blocks += int(xwhat.findtext('leakedblocks'))
            elif kind == 'InvalidFree':
                agg.nb_invalid_frees += 1
            elif kind == 'InvalidJump':
                agg.nb_invalid_jumps += 1
            elif kind == 'InvalidRead':
                agg.nb_invalid_reads += 1
            elif kind == 'InvalidWrite':
                agg.nb_invalid_writes += 1
            elif kind == 'MismatchedFree':
                agg.nb_mismatched_frees += 1

        return agg

    @staticmethod
    def from_xml_string(string):
        root = ET.fromstring(string)
        return Aggregation.parse(root)

    @staticmethod
    def from_xml_file(filename):
        root = ET.parse(filename).getroot()
        return Aggregation.parse(root)

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True)

    def __repr__(self):
        return self.to_json()

