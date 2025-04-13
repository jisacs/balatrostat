from  scipy.special import comb 


from math import comb

def proba_exactement_N_valeurs(N, M, total_cartes=52, nb_valeurs=4):
    """
    Calcule la probabilité d'obtenir exactement N cartes d'une valeur particulière (ex: As)
    en tirant M cartes sans remise d'un jeu de total_cartes cartes.

    Args:
        N (int): Nombre de cartes spécifiques souhaitées (ex: N As).
        M (int): Nombre total de cartes tirées.
        total_cartes (int): Nombre total de cartes dans le jeu (par défaut 52).
        nb_valeurs (int): Nombre de cartes de la valeur ciblée dans le jeu (par défaut 4).

    Returns:
        float: Probabilité (entre 0 et 1).
    """
    if N > nb_valeurs or N > M or M > total_cartes:
        return 0.0  # impossible si N trop grand, ou M trop grand

    favorable = comb(nb_valeurs, N) * comb(total_cartes - nb_valeurs, M - N)
    total = comb(total_cartes, M)

    probability = favorable / total
    return probability


from math import comb

def proba_au_moins_N_valeurs(N, M, total_cartes, nb_valeurs):
    """
    Calcule la probabilité d'obtenir au moins N cartes d'une valeur particulière (ex: As)
    en tirant M cartes sans remise d'un jeu de total_cartes cartes, où nb_valeurs est le
    nombre de cartes de cette valeur particulière dans le jeu (par exemple 4 pour les As).

    Args:
        N (int): Nombre minimum de cartes spécifiques souhaitées (ex: au moins N As).
        M (int): Nombre total de cartes tirées.
        total_cartes (int): Nombre total de cartes dans le jeu (par exemple 40 ou 60).
        nb_valeurs (int): Nombre de cartes de la valeur ciblée dans le jeu (par exemple 3 ou 5).

    Returns:
        float: Probabilité (entre 0 et 1).
    """
    if N > nb_valeurs or N > M or M > total_cartes:
        return 0.0  # impossible si N trop grand, ou M trop grand

    probability = 0.0
    max_possible = min(nb_valeurs, M)

    for k in range(N, max_possible + 1):
        favorable = comb(nb_valeurs, k) * comb(total_cartes - nb_valeurs, M - k)
        total = comb(total_cartes, M)
        probability += favorable / total

    return probability

   