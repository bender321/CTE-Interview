from fce import is_even


def test_fce_odd():
    assert is_even(374935) is False
    assert is_even('374935') is False
    assert is_even('three hundred seventy-four thousand nine hundred thirty-five') is False
    assert is_even('Three Hundred Seventy-Four Thousand Nine Hundred Thirty-Five') is False
    assert is_even('THREE HUNDRED SEVENTY-FOUR THOUSAND NINE HUNDRED THIRTY-FIVE') is False


def test_fce_even():
    assert is_even(12) is True
    assert is_even(90) is True
    assert is_even('ninety') is True
    assert is_even('12') is True
    assert is_even('twelve') is True
    assert is_even('Twelve') is True
    assert is_even('TWELVE') is True
    assert is_even('EvEn') is True
    assert is_even('THREE HUNDRED SEVENTY-FOUR THOUSAND NINE HUNDRED THIRTY-Two') is True


def test_fce_nonsense():
    assert is_even('Ahoj') is None
    assert is_even('Even6') is None
    assert is_even('Even-6') is None
    assert is_even(',9,9,9,9,9,++,+sfasdfaba6') is None
