def fair_sharer(values, num_iterations, share=0.1):
    values_new = values[:]  # Kopie der ursprünglichen Werte, um sie nicht zu verändern
    
    for _ in range(num_iterations):
        max_index = values_new.index(max(values_new))  # Index des höchsten Wertes
        max_value = values_new[max_index]  # Höchster Wert
        
        # Verteilung des Anteils des höchsten Wertes an die Nachbarn
        left_neighbor = (max_index - 1) % len(values_new)  # Index des linken Nachbarn
        right_neighbor = (max_index + 1) % len(values_new)  # Index des rechten Nachbarn
        
        # Berechnung der Anteile für die Nachbarn
        share_to_give = max_value * share
        values_new[left_neighbor] += share_to_give
        values_new[right_neighbor] += share_to_give
        
        # Reduzierung des höchsten Wertes um den Anteil, der verteilt wurde
        values_new[max_index] -= 2 * share_to_give
    
    return values_new

fair_sharer([0, 1000, 800, 0], 1)  # --> [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2)  # --> [100, 890, 720, 90]
