import os
from owlready2 import get_ontology, Restriction
import rdflib
from rdflib import Graph, BNode
from rdflib.namespace import OWL, RDF, RDFS, XSD, Namespace


def check_ontology(ontology_path):
    try:
        ontology = get_ontology(ontology_path).load()
        # Perform your checks here
        print(f"Ontology {ontology_path} loaded successfully.")
        return True
    except Exception as e:
        print(f"Error loading ontology {ontology_path}: {e}")
        return False


def check_undefined_classes(ontology_path):
    g = Graph()
    g.parse(ontology_path)

    # Namespaces
    owl = Namespace("http://www.w3.org/2002/07/owl#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

    built_in_namespaces = {str(OWL), str(RDF), str(RDFS), str(XSD)}

    # Get all defined classes and properties
    defined_entities = (
        set(g.subjects(RDF.type, OWL.Class))
        | set(g.subjects(RDF.type, OWL.ObjectProperty))
        | set(g.subjects(RDF.type, OWL.DatatypeProperty))
    )

    # Get all referenced classes and properties
    referenced_entities = (
        set(g.objects(None, RDF.type))
        | set(g.objects(None, rdf.parseType))
        | set(g.objects(None, owl.onProperty))
    )

    # Check for ranges and domains in ObjectProperty and DatatypeProperty
    for prop in set(g.subjects(RDF.type, OWL.ObjectProperty)) | set(
        g.subjects(RDF.type, OWL.DatatypeProperty)
    ):
        if (prop, RDFS.range, None) in g:
            referenced_entities.add(g.value(prop, RDFS.range))
        if (prop, RDFS.domain, None) in g:
            referenced_entities.add(g.value(prop, RDFS.domain))

    # Check for restrictions
    for restriction in g.subjects(RDF.type, OWL.Restriction):
        if (restriction, owl.someValuesFrom, None) in g:
            referenced_entities.add(g.value(restriction, owl.someValuesFrom))

    # Filter out defined entities
    undefined_entities = referenced_entities - defined_entities

    # Exclude built-in entities and blank nodes
    undefined_entities = {
        entity
        for entity in undefined_entities
        if not any(str(entity).startswith(ns) for ns in built_in_namespaces)
        and not isinstance(entity, BNode)
    }

    for undefined_entity in undefined_entities:
        print(f"Referenced but undefined class or property: {undefined_entity}")


if __name__ == "__main__":
    ontology_files = ["gdo.owl", "gdoa.owl", "pruned_gdo.owl"]
    for file in ontology_files:
        check_ontology(file)
        check_undefined_classes(file)
        # check_undefined_entities(file)
