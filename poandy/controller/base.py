from poandy.util.objectless import Objectless
from poandy.util.utils import Utils


class Controller(Objectless):
    _config = Utils.get_config()
    _headers = Utils.get_headers()
