from sum_from_input import sum_from_string


def test_sum_from_input():
    assert sum_from_string('3.14f5') == 22
    assert sum_from_string('') == 0
    assert sum_from_string('dawd!~^aw&*(ndodi') == 0
    assert sum_from_string('dawd!~^2aw&*(ndodi') == 2
    assert sum_from_string('10da00wd00!~^212aw4.4.5&*(111ndodi30') == 376
