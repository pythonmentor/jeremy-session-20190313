# Recommandations pour le dev d'un parser de questions pour Grandpy

phrase = "Salut grandpy! Est-ce que tu POURRAIS me dire où se site la tour Eiffel?"

Etapes:

- tout mettre en miniscules
- enlever tous les accents, apostrophes (remplacer par un espace)
- isoler les éléments intéressants de la phrase à l'aide d'expressions rationnelles
- éliminer tous les caractères spéciaux (ponctuation)
- découper la phrase mot par mot -> liste de mots
- filtrer les mots dans la liste (filtrer les stop words)

Liens utiles:

- [Cours sur les expressions rationnelles](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233857-manipulez-les-expressions-regulieres)
- [Howto de la doc officielle sur les expressions rationnelles](https://docs.python.org/fr/3/howto/regex.html)