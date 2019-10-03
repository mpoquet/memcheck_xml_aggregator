"""
Test Memcheck XML parsing functions.
"""
import pytest
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

    c = a + b
    assert c.nb_errors == a.nb_errors + b.nb_errors
    assert c.nb_invalid_frees == a.nb_invalid_frees + b.nb_invalid_frees
    assert c.nb_invalid_jumps == a.nb_invalid_jumps + b.nb_invalid_jumps
    assert c.nb_invalid_reads == a.nb_invalid_reads + b.nb_invalid_reads
    assert c.nb_invalid_writes == a.nb_invalid_writes + b.nb_invalid_writes
    assert c.nb_leaked_blocks == a.nb_leaked_blocks + b.nb_leaked_blocks
    assert c.nb_leaked_bytes ==  a.nb_leaked_bytes + b.nb_leaked_bytes
    assert c.nb_mismatched_frees == a.nb_mismatched_frees + b.nb_mismatched_frees
    assert c.nb_uninit_uses == a.nb_uninit_uses + b.nb_uninit_uses

    with pytest.raises(ValueError):
        a + 10

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
