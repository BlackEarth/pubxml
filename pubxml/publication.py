
from bxml import XML
from . import NS    

class Publication(XML):
    ROOT_TAG = "{%(pub)s}publication" % NS
