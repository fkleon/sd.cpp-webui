def test_get_next_media_seq(app_root) -> None:
    from modules.gallery import get_next_media

    filename = get_next_media(media_out_dir=str(app_root / "img2img"), subctrl=0)
    assert "1.png" == filename


def test_get_next_media_seq_conflict(app_root):
    from modules.gallery import get_next_media

    existing_file = app_root / "img2img" / "1.png"
    existing_file.touch()

    filename = get_next_media(media_out_dir=str(app_root / "img2img"), subctrl=1)
    assert "2.png" == filename
