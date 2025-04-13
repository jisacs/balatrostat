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

