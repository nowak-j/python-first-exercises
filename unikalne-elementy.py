# Napisz funkcję unique_elements(elements), która będzie zwracać listę z unikalnymi elementami.

def unique_elements(elements):
    unique_list = []

    for element in elements:
        if element not in unique_list:
            unique_list.append(element)
            
    return unique_list