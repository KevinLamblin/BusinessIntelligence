import csv
import myConnection

"""
Script de création de la base de données

"""
def createDatabase():
    # Récupération des données du CSV
    with open('D:\VideoGamesData\Vgsales-12-4-2019.csv', 'r', encoding='utf-8') as file:
        data = csv.reader(file)
        next(data)
        # Pour chaque ligne
        for row in data:
            # Définition des variables qui contiennent nos données
            rank = row[0]
            name = row[1]
            basename = row[2]
            genre = row[3]
            esrbRating = row[4]
            plateform = row[5]
            publisher = row[6]
            developer = row[7]
            criticScore = row[9]
            userScore = row[10]
            globalSale = row[11]
            year = row[17]
            vgChartzScore = row[21]

            # Gestion des valeurs NULL
            if (name == ''):
                name = None

            if (basename == ''):
                basename = None


            if (criticScore == ''):
                criticScore = None

            if (userScore == ''):
                userScore = None

            if (globalSale == ''):
                globalSale = row[12]
                lowerSales = globalSale.lower()
                containsLetter = lowerSales.islower()
                if (containsLetter):
                    globalSale = ''
            if (globalSale == ''):
                globalSale = None

            if (year == ''):
                year = None

            if (vgChartzScore == ''):
                vgChartzScore = None

            # Connection à la base mySQL
            connection = myConnection.connection()

            # Si la base est connectée
            if connection.is_connected():
                cursor = connection.cursor(buffered = True)
                cursor.execute("select database();")

                # Vérifie si le genre est déjà dans la base
                mySQL_verify_data = """select idGenre from GENRES where genre = %(genre)s;"""
                cursor.execute(mySQL_verify_data, {'genre': genre})
                res = cursor.fetchall()
                connection.commit()

                # Si le genre n'est pas connus,
                if (len(res) == 0):
                    # On insère le genre
                    mySQL_insert_data = """insert into GENRES values (%s, %s); """
                    val = (0, genre)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                # Vérifie si l'éditeur est déjà dans la base
                mySQL_verify_data = """select idPublisher from PUBLISHERS where publisher = %(publisher)s;"""
                cursor.execute(mySQL_verify_data, {'publisher': publisher})
                res = cursor.fetchall()
                connection.commit()

                # Si l'éditeur n'est pas connus,
                if (len(res) == 0):
                    # On insère l'éditeur
                    mySQL_insert_data = """insert into PUBLISHERS values (%s, %s); """
                    val = (0, publisher)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                # Vérifie si le développeur est déjà dans la base
                mySQL_verify_data = """select idDeveloper from DEVELOPERS where developer = %(developer)s;"""
                cursor.execute(mySQL_verify_data, {'developer': developer})
                res = cursor.fetchall()
                connection.commit()

                # Si le développeur n'est pas connus,
                if (len(res) == 0):
                    # On insère le développeur
                    mySQL_insert_data = """insert into DEVELOPERS values (%s, %s); """
                    val = (0, developer)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                # Vérifie si la plateforme est déjà dans la base
                mySQL_verify_data = """select idPlateform from PLATEFORMS where plateform = %(plateform)s;"""
                cursor.execute(mySQL_verify_data, {'plateform': plateform})
                res = cursor.fetchall()
                connection.commit()

                # Si la plateforme n'est pas connus,
                if (len(res) == 0):
                    # On insère la plateforme
                    mySQL_insert_data = """insert into PLATEFORMS values (%s, %s); """
                    val = (0, plateform)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                # Vérifie si l'esrb est déjà dans la base
                mySQL_verify_data = """select idEsrbRating from ESRBRATINGS where esrbRating = %(esrbRating)s;"""
                cursor.execute(mySQL_verify_data, {'esrbRating': esrbRating})
                res = cursor.fetchall()
                connection.commit()

                # Si l'esrb n'est pas connus,
                if (len(res) == 0):
                    # On insère l'esrb
                    mySQL_insert_data = """insert into ESRBRATINGS values (%s, %s); """
                    val = (0, esrbRating)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                # Récupération des id Genre, Plateform, Developer et Publisher

                mySQL_verify_data = """select idGenre from GENRES where genre = %(genre)s;"""
                cursor.execute(mySQL_verify_data, {'genre': genre})
                res = cursor.fetchall()
                connection.commit()
                # Conversion du resultat tuple en int pour les id
                idGenre = int(''.join(map(str, res[0])))




                mySQL_verify_data = """select idPublisher from PUBLISHERS where publisher = %(publisher)s;"""
                cursor.execute(mySQL_verify_data, {'publisher': publisher})
                res = cursor.fetchall()
                connection.commit()
                idPublisher = int(''.join(map(str, res[0])))


                mySQL_verify_data = """select idPlateform from PLATEFORMS where plateform = %(plateform)s;"""
                cursor.execute(mySQL_verify_data, {'plateform': plateform})
                res = cursor.fetchall()
                connection.commit()
                idPlateform = int(''.join(map(str, res[0])))

                mySQL_verify_data = """select idDeveloper from DEVELOPERS where developer = %(developer)s;"""
                cursor.execute(mySQL_verify_data, {'developer': developer})
                res = cursor.fetchall()
                connection.commit()
                idDeveloper = int(''.join(map(str, res[0])))

                mySQL_verify_data = """select idEsrbRating from ESRBRATINGS where esrbRating = %(esrbRating)s;"""
                cursor.execute(mySQL_verify_data, {'esrbRating': esrbRating})
                res = cursor.fetchall()
                connection.commit()
                # Conversion du resultat tuple en int pour les id
                idEsrbRating = int(''.join(map(str, res[0])))

                # Vérifie si la data est déjà dans la base
                mySQL_verify_data = """select rank from VIDEOGAMES where rank = %(rank)s;"""
                cursor.execute(mySQL_verify_data, {'rank': rank})
                res = cursor.fetchall()
                connection.commit()

                # Si la data n'est pas dans la base
                if(len(res) == 0):
                    # On insère a données
                    mySQL_insert_data = """insert into VIDEOGAMES values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
                    val = (
                        rank, name, basename, idGenre, idEsrbRating, idPlateform, idPublisher, idDeveloper, criticScore, userScore,
                        globalSale,
                        year, vgChartzScore)
                    cursor.execute(mySQL_insert_data, val)
                    connection.commit()

                cursor.close()
        connection.close()