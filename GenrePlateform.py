from plotly.offline import plot
import plotly.graph_objs as go

"""
Script de création d'un des diagrammes, 

:param connection Connection de la base de données
"""
def drawGenrePlateformDiagram(connection):
    cursor = connection.cursor(buffered=True)
    cursor.execute("select database();")

    # Requête qui nous donne le nombre de jeux et le total de vente de chaque genre de jeux depuis 2016
    mySQL_query = """select genre, count(rank), sum(globalSale) from videogames natural join genres where year >= 2016 group by genre having  sum(globalSale) is not null;"""
    cursor.execute(mySQL_query)
    res = cursor.fetchall()
    connection.commit()

    # Initialisations des données pour le diagramme
    genres = []
    nbGames = []
    totalSales = []
    averageSales = []

    for i in range(0, len(res)):
        genres.append(res[i][0])
        nbGames.append(res[i][1])
        totalSales.append(res[i][2])
        averageSales.append(totalSales[i] / nbGames[i])

    # Diagramme pour le nombre de jeux par genre
    number = {
        "values": nbGames,
        "labels": genres,
        "domain": {"column": 0},
        "name": "Games",
        "hoverinfo": "name+label+percent+value",
        "type": "pie",
    }
    # Diagramme pour le nombre de vente par genre
    sales = {
        "values": totalSales,
        "labels": genres,
        "domain": {"column": 1},
        "name": "Sales",
        "hoverinfo": "name+label+percent+value",
        "type": "pie",
    }
    # Diagramme pour le nombre de vente moyen par genre
    average = {
        "values": averageSales,
        "labels": genres,
        "domain": {"column": 2},
        "name": "Average Sales",
        "hoverinfo": "name+label+percent+value",
        "type": "pie",
    }

    # Assemblage des données
    data = [number, sales, average]

    # Affichage des titres
    layout = go.Layout(
        {
            "title": "Games by genres since 2016",
            "grid": {"rows": 1, "columns": 3},
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Number of game",
                    "x": 0.09,
                    "y": 0.5
                },
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Total sales in million",
                    "x": 0.5,
                    "y": 0.5
                },
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Average sales in million",
                    "x": 0.93,
                    "y": 0.5
                }
            ]
        }
    )
    # Création de la figure
    fig = go.Figure(data=data, layout=layout)
    plot(fig)