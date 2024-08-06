import Levenshtein

def count_matches(ocr_lines, product_list, total_products_count):
    # Initialize counters for different match categories
    exact_match_count = 0
    distance_0_1_count = 0
    distance_0_2_count = 0

    # Iterate over each line from the OCR results
    for ocr_line in ocr_lines:
        min_distance = float('inf')

        # Compare each OCR line with every product name
        for product_name in product_list:
            distance = Levenshtein.distance(ocr_line, product_name)  # Compute Levenshtein distance
            max_length = max(len(ocr_line), len(product_name))  # Get the maximum length for normalization
            distance = distance / max_length  # Normalize the distance

            # Update the minimum distance if a smaller one is found
            if distance < min_distance:
                min_distance = distance

        # Categorize the match based on the minimum normalized distance
        if min_distance == 0:
            exact_match_count += 1
        elif min_distance <= 0.1:
            distance_0_1_count += 1
        elif min_distance <= 0.2:
            distance_0_2_count += 1

    # Calculate the count of products with a distance > 0.2
    distance_sup_0_2_count = total_products_count - (exact_match_count + distance_0_1_count + distance_0_2_count)

    return exact_match_count, distance_0_1_count, distance_0_2_count, distance_sup_0_2_count

