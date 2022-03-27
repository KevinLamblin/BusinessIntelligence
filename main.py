from plotly.offline import plot

import Genre
import GenrePlateform
import Plateform
import createDatabase
import myConnection
import plotly.graph_objs as go

"""
Script d'analyse des data

"""

# Connecte la base de données
connection = myConnection.connection()

# Création d'un diagramme qui permet de récupérer le nombre de jeux, le nombre de vente et le score critique moyen de
# chaque genre de jeux sur le 5 dernières années

# Si la base est connectée
if connection.is_connected():
    select = 1

    if select == 0:
        Genre.drawGenreDiagram(connection)
    elif select == 1:
        Plateform.drawPlateformDiagram(connection)
    elif select == 2:
        GenrePlateform.drawGenrePlateformDiagram(connection)