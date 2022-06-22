import rdflib

import os
import jinja2
from rdflib.namespace import OWL, RDF, RDFS, XSD


class FileManager:
    def __init__(self, directory):
        self.directory = directory
        self.file = None

    def open_file(self, file_name):
        path = os.path.join(self.directory, file_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.file = open(path, "w")
        return ""

    def write_and_close(self, data):
        if self.file is None:
            return

        self.file.write(data)
        self.file.close()
        self.file = None


def iri_to_identifier(iri):
    return str(iri) \
            .replace("https://comp-rob2b.github.io/modelling-tutorial/robot#", "") \
            .replace(":", "_").replace("-", "_").replace("<", "").replace(">", "") \
            .replace("/", "_").replace(".", "_").replace("#", "_")


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


    COMP_ROB2B = "https://comp-rob2b.github.io"
    GEOM_ENT = rdflib.Namespace(COMP_ROB2B + "/metamodels/geometry/structural-entities#")
    GEOM_REL = rdflib.Namespace(COMP_ROB2B + "/metamodels/geometry/spatial-relations#")
    GEOM_CRD = rdflib.Namespace(COMP_ROB2B + "/metamodels/geometry/coordinates#")
    GEOM_OP  = rdflib.Namespace(COMP_ROB2B + "/metamodels/geometry/spatial-operators#")
    KC_ENT   = rdflib.Namespace(COMP_ROB2B + "/metamodels/kinematic-chain/structural-entities#")
    KC_STAT  = rdflib.Namespace(COMP_ROB2B + "/metamodels/kinematic-chain/state#")
    KC_OP    = rdflib.Namespace(COMP_ROB2B + "/metamodels/kinematic-chain/operators#")
    ALGO     = rdflib.Namespace(COMP_ROB2B + "/metamodels/algorithm#")
    QUDT     = rdflib.Namespace("http://qudt.org/schema/qudt/")

    fm = FileManager("gen/")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("jinja/"),
                             lstrip_blocks=True, trim_blocks=True)
    env.filters["file"] = fm.open_file

    for template_name in env.list_templates():
        template = env.get_template(template_name)
        rendered = template.render({
            "g": g,
            "RDF": RDF,
            "GEOM_ENT": GEOM_ENT,
            "GEOM_REL": GEOM_REL,
            "GEOM_CRD": GEOM_CRD,
            "GEOM_OP": GEOM_OP,
            "KC_ENT": KC_ENT,
            "KC_STAT": KC_STAT,
            "KC_OP": KC_OP,
            "ALGO": ALGO,
            "QUDT": QUDT,
            "rdflib": rdflib,
            "inv_path": rdflib.paths.inv_path,
            "list": list,
            "iri_to_identifier": iri_to_identifier
        })
        fm.write_and_close(rendered)