"""
Test Memcheck XML parsing functions.
"""
import memcheck_xml_aggregator as agg

def test_parse():
    a = agg.Aggregation.from_xml_file('./test/input/crash.xml')
    assert a.nb_errors == 7
    assert a.nb_invalid_frees == 1
    assert a.nb_invalid_jumps == 1
    assert a.nb_invalid_reads == 1
    assert a.nb_invalid_writes == 1
    assert a.nb_leaked_blocks == 0
    assert a.nb_leaked_bytes == 0
    assert a.nb_mismatched_frees == 1
    assert a.nb_uninit_uses == 2

    b = agg.Aggregation.from_xml_file('./test/input/leak.xml')
    assert b.nb_errors == 9
    assert b.nb_invalid_frees == 1
    assert b.nb_invalid_jumps == 0
    assert b.nb_invalid_reads == 1
    assert b.nb_invalid_writes == 1
    assert b.nb_leaked_blocks == 3
    assert b.nb_leaked_bytes == 75
    assert b.nb_mismatched_frees == 1
    assert b.nb_uninit_uses == 2
    assert b.to_json() == '''{"nb_errors": 9, "nb_invalid_frees": 1, "nb_invalid_jumps": 0, "nb_invalid_reads": 1, "nb_invalid_writes": 1, "nb_leaked_blocks": 3, "nb_leaked_bytes": 75, "nb_mismatched_frees": 1, "nb_uninit_uses": 2}'''
    assert repr(b) == b.to_json()

    assert a != b
    assert not (a == b)
    assert (a != 10)
    assert not (a == 10)

    f = open('./test/input/leak.xml', 'r')
    content = f.read()
    b2 = agg.Aggregation.from_xml_string(content)
    assert b2 == b
    assert not (b2 != b)
    assert b2.to_json() == b.to_json()
