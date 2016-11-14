
import os
from lxml import etree
from bl.id import random_id
from bl.zip import ZIP
from .icml import ICML
import pubxml

class IDML(ZIP):
    POINTS_PER_EM = ICML.POINTS_PER_EM
    NS = ICML.NS

    @property
    def output_path(self):
        return os.path.splitext(self.fn)[0]

    def documents(self, path=None, **params):
        """return a collection of pub:documents from the stories in the .idml file"""
        if path is None: 
            path = self.output_path
        designmap = ICML(
            fn=os.path.join(path, 'designmap.xml'), 
            root=self.read('designmap.xml'))
        documents = []
        for story in designmap.root.xpath("idPkg:Story", namespaces=self.NS):
            # use a temporary file for the story source, just in case it's huge
            tfn = os.path.join(os.path.dirname(self.fn), random_id())
            with open(tfn, 'wb') as tf:
                tf.write(self.read(story.get('src')))
            root = etree.parse(tfn).getroot()
            os.remove(tfn)
            icml = ICML(root=root)
            document = icml.document(fn=os.path.join(path, story.get('src')))
            documents.append(document)
        # fix links between documents
        ids = {}
        for d in documents:
            for e in d.root.xpath("//*[@id]"):
                ids[e.get('id')] = d.fn
        for doc in documents:
            for e in doc.root.xpath("//pub:include[@id]", namespaces=pubxml.NS):
                if e.get('id') in ids:
                    id = e.attrib.pop('id')
                    targetfn = ids[id]
                    e.set('src', os.path.relpath(targetfn, os.path.dirname(doc.fn)) + '#' + id)
        return documents

    def stylesheet(self, fn=None, points_per_em=POINTS_PER_EM):
        """return a stylesheet from the .idml file's style definitions"""
        if fn is None:
            fn = os.path.join(self.output_path, os.path.basename(self.output_path)+'.css')
        return ICML(root=self.read('Resources/Styles.xml')).stylesheet(
            fn=fn, 
            points_per_em=points_per_em)
