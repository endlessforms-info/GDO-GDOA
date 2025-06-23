# GDO/A

Repository for the Graphic Descriptor Ontology (GDO) and the Graphic Descriptor Ontology Anatomy extension (GDOA)

## About

The Graphic Descriptor Ontology (GDO) is intended for use in describing graphics that represent the form of objects. It uses the language of visual communication, illustration, and technical drawing. The GDO is rooted in the Basic Formal Ontology (BFO) and uses several classes from the Information Entity Ontology of the Common Core Ontologies as a mid-level ontology.

Our driving use case is description of anatomical graphics, both human anatomy and the anatomy of other organisms. To accommodate anatomy-specific classes we developed the Graphic Descriptor Ontology Anatomy extension (GDOA), which extends the GDO to the domain of anatomical graphics.

The combined GDO and GDOA (which we refer to as GDO/A) include classes for describing qualities of graphics (including anatomical views, projection type, and style of representation of parts) and the roles of graphical marks (such as occluding contour line, line of striation, and location point).

A merged version of the GDO/A is also available via NCBO Portal: https://bioportal.bioontology.org/ontologies/GDOA

## Use

The GDO file (gdo.owl) can be used stand-alone. The GDOA file (gdoa.owl), however, imports the file god.owl. This is easiest done via local imports, but local imports require IRI to local file mappings to properly resolve. If opening the GDOA in Protege, the included file catalog-v001.xml provides this mapping. It maps to a relative location, so all of the files gdo.owl, gdoa.owl, and catalog-v001.xml must be in the same directory. 

However, if you aren't using Protege, or don't wish to resolve imports locally, the imports *should* resolve from the web. 
