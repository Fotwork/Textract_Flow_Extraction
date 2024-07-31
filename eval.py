import Levenshtein

def count_matches(all_lines, liste_produits):
    exact_matches = 0
    normalized_0_1 = 0
    normalized_0_2 = 0

    for line in all_lines:
        min_normalized_distance = 120344
        
        for produit in liste_produits:
            distance = Levenshtein.distance(line, produit)
            max_length = max(len(line), len(produit))
            normalized_distance = distance / max_length
            
            if normalized_distance < min_normalized_distance:
                min_normalized_distance = normalized_distance
        
        if min_normalized_distance == 0:
            exact_matches += 1
        elif min_normalized_distance <= 0.1:
            normalized_0_1 += 1
        elif min_normalized_distance <= 0.2:
            normalized_0_2 += 1

    return exact_matches, normalized_0_1, normalized_0_2
