import pytest
from mach1py.mach1file import mach1file, mach1filevalidator


def test_check_wrong_inputs():

    with pytest.raises(TypeError):
        obj = mach1filevalidator(file_path=1.0)

    with pytest.raises(TypeError):
        obj = mach1filevalidator(file_path="test", fdata=1.0)


def test_valid_mach1_file():

    with pytest.raises(ValueError):
        obj = mach1file("./tests/test_no_header.txt")


def test_file_load():

    obj = mach1file("./tests/test_correct.txt")

    assert obj.info["Date"] == "Mon, May 06, 2024"
    assert obj.info["Time"] == "12:27:19.434"
    assert obj.info["Load Cell Calibration Date"] == "2024-05-06"
    assert obj.info["Action"] == "Move Absolute"


def test_data_parse():

    obj = mach1file("./tests/test_correct.txt")

    assert obj.data.keys()[0] == "Time, s"
    assert obj.data.keys()[0] == "Position (z), mm"
    assert obj.data.keys()[0] == "Fz, gf"

    assert obj.data.iloc[0, 0] == 0.00
    assert obj.data.iloc[0, 1] == 0.00
    assert obj.data.iloc[0, 2] == 25.348794
