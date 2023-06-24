from utils.main import number_encryption, formate_date


def test_number_encryption():
    assert number_encryption("Счет 72082042523231456215") == "Счет **6215"
    assert number_encryption("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert number_encryption("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert number_encryption("MasterCard 7158300734726758") == "MasterCard 7158 07** **** 6758"

def test_formate_date():
    assert formate_date("2018-08-19T04:27:37.904916")=="19.08.2018"
