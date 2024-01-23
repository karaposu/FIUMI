from graphviz import Digraph

# Initialize Digraph object
dot = Digraph(comment='The Fiumi System')

# Adding nodes (Here, components of the system)
dot.node('PG', 'Persona Generator')
dot.node('PFG', 'Persona Face Generator')
dot.node('SCC', 'Server Credential Creator')
dot.node('FAD', 'Fiumi Agent Database')
dot.node('ADM', 'Activity Distribution Manager')
dot.node('AC', 'Account Creator')
dot.node('IA', 'Idle Activity')
dot.node('PC', 'Post Creator')
dot.node('SC', 'Scroller')
dot.node('ST', 'Stroller')
dot.node('LK', 'Liker')
dot.node('CM', 'Commenter')

# Adding edges (representing the interactions/relationships)
dot.edge('PG', 'PFG', label='generates face data')
dot.edge('PG', 'FAD', label='sends persona data')
dot.edge('PFG', 'FAD', label='sends face images')
dot.edge('SCC', 'ADM', label='provides credentials and IPs')
dot.edge('FAD', 'ADM', label='provides persona data')
dot.edge('ADM', 'AC', label='commands')
dot.edge('ADM', 'IA', label='commands')
dot.edge('ADM', 'PC', label='commands')
dot.edge('ADM', 'SC', label='commands')
dot.edge('ADM', 'ST', label='commands')
dot.edge('ADM', 'LK', label='commands')
dot.edge('ADM', 'CM', label='commands')

# Render the graph to a file (PDF)
dot.render('/mnt/data/fiumi_uml_diagram', view=False, format='pdf')

# Return the path to the UML diagram PDF file
'/mnt/data/fiumi_uml_diagram.pdf'
