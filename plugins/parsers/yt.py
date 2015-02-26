from rdflib.parser import Parser
from rdflib.plugins.parsers.ytriples import YTriplesParser

__all__ = ['YTSink', 'YTParser']


class YTSink(object):
    def __init__(self, graph):
        self.graph = graph

    def triple(self, s, p, o):
        self.graph.add((s, p, o))


class YTParser(Parser):
    """parser for the ntriples format, often stored with the .nt extension

    See http://www.w3.org/TR/rdf-testcases/#ntriples"""

    def __init__(self):
        super(YTParser, self).__init__()

    def parse(self, source, sink, baseURI=None):
        f = source.getByteStream()  # TODO getCharacterStream?
        parser = YTriplesParser(YTSink(sink))
        parser.parse(f)
        f.close()
