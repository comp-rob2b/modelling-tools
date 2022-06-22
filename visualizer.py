import rdflib
from rdflib.tools.rdf2dot import rdf2dot

if __name__ == "__main__":
    g = rdflib.ConjunctiveGraph()

    TUTORIAL = "../modelling-tutorial/models"
    g.parse(TUTORIAL + "/skeleton.json", format="json-ld")
    g.parse(TUTORIAL + "/spatial-relations.json", format="json-ld")
    g.parse(TUTORIAL + "/cartesian-coordinates.json", format="json-ld")
    g.parse(TUTORIAL + "/joint-coordinates.json", format="json-ld")
    g.parse(TUTORIAL + "/chain.json", format="json-ld")
    g.parse(TUTORIAL + "/dynamics.json", format="json-ld")
    g.parse(TUTORIAL + "/fpk-algorithm.json", format="json-ld")

    with open("model.dot", mode="w") as stream:
        rdf2dot(g, stream)