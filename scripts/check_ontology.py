import os
from owlready2 import get_ontology


def check_ontology(ontology_path):
    try:
        ontology = get_ontology(ontology_path).load()
        # Perform your checks here
        print(f"Ontology {ontology_path} loaded successfully.")
        return True
    except Exception as e:
        print(f"Error loading ontology {ontology_path}: {e}")
        return False


if __name__ == "__main__":
    ontology_files = ["../gdo.owl", "../gdoa.owl"]
    for file in ontology_files:
        check_ontology(file)
