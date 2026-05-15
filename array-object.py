"""test on array-object"""


def filter_by_property(array_of_objects, property_name, property_value):
    """Écrivez une fonction qui filtre un tableau d'objets selon
    une propriété et sa valeur."""
    return [obj for obj in array_of_objects if obj.get(property_name) == property_value]


def group_by(array_of_objects, property_name):
    """Écrivez une fonction qui groupe les éléments d'un tableau
    selon une propriété."""
    grouped = {}
    for obj in array_of_objects:
        key = obj.get(property_name)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)
    return grouped


def find_intersection(lib1, lib2, property_name):
    """Écrivez une fonction qui trouve l'intersection entre deux
    tableaux d'objets selon une propriété donnée"""
    set1 = {obj.get(property_name) for obj in lib1}
    set2 = {obj.get(property_name) for obj in lib2}
    intersection = set1 & set2
    return [obj for obj in lib1 if obj.get(property_name) in intersection]


def transform_array(array_of_objects, mapping_function):
    """Écrivez une fonction qui transforme un tableau d'objets en
    utilisant une fonction de mapping personnalisée"""
    return [mapping_function(obj) for obj in array_of_objects]


def aggregate_data(array_of_objects, group_key, value_key):
    """Écrivez une fonction qui agrège les données d'un tableau d'objets."""
    aggregated = {}
    for obj in array_of_objects:
        key = obj.get(group_key)
        value = obj.get(value_key, 0)
        aggregated[key] = aggregated.get(key, 0) + value
    return aggregated
