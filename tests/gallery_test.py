import pytest
import datetime


def test_get_next_img_date():
    from modules.gallery import get_next_img_date
    reference_date = datetime.datetime.fromisoformat("2006-01-02T15:04:05")
    filename  = get_next_img_date(ref=reference_date)
    assert "2006-01-02_15-04-05.png" == filename


def test_get_next_img_seq():
    from modules.gallery import get_next_img_seq

    filename  = get_next_img_seq(subctrl=0)
    assert "1.png" == filename


def test_get_next_img_seq_conflict(app_root):
    from modules.gallery import get_next_img_seq

    existing_file = app_root / "img2img" / "1.png"
    existing_file.touch()

    filename  = get_next_img_seq(subctrl=1)
    assert "2.png" == filename