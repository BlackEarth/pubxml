
from bxml import XML
from . import NS    

class Document(XML):
    ROOT_TAG = "{%(pub)s}document" % NS
