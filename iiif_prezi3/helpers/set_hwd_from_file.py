from ..loader import monkeypatch_schema
from ..skeleton import Canvas, ResourceItem
from PIL import Image


class SetHeightWidthDurationFileHelper:
    """Introspect a file and set the height, width, and duration properties
    of a Canvas or Content Resource object, allowing nulls

    Args:
        file_path_or_object (filepath or fileobject): the file path or file object to introspect

    Returns:
        None
    """

    def set_hwd_from_file(self, file_path_or_object):
        tmp_image = Image.open(file_path_or_object)
        w, h = tmp_image.size
        self.set_hwd(h, w, None)
        tmp_image.close()

    def set_hwd(self, h, w, d):
        # stub preparing for Issue #54
        self.width = w
        self.height = h
        self.duration = d


monkeypatch_schema(Canvas, SetHeightWidthDurationFileHelper)
