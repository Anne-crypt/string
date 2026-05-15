"""test on object"""

from urllib.parse import urlencode, quote


def get_values(scores):
    """Écrivez une fonction qui récupère toutes les valeurs d'un objet"""
    return list(scores.values())


def transform_values(prices_in_euros, to_dollars):
    """Écrivez une fonction qui transforme les valeurs d'un objet"""
    return {key: to_dollars(valeur) for key, valeur in prices_in_euros.items()}


def merge_objects(obj1, obj2):
    """Écrivez une fonction qui fusionne deux objets en sommant
    les valeurs numériques communes."""
    merged = obj1.copy()
    for key, value in obj2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


def filter_object(obj, stock):
    """Écrivez une fonction qui filtre un objet selon une
    condition sur les valeurs."""
    return {key: value for key, value in obj.items() if stock(value)}


def flat_to_nested(flat_config):
    """Écrivez une fonction qui convertit un objet plat en objet imbriqué en utilisant
    les points comme séparateurs"""
    nested_config = {}
    for key, value in flat_config.items():
        parts = key.split(".")
        current = nested_config
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return nested_config


def find_keys_by_value(obj, target_value):
    """Écrivez une fonction qui trouve les clés d'un objet
    ayant une valeur spécifique."""
    return [key for key, value in obj.items() if value == target_value]


def create_object_from_arrays(array1, array2):
    """Écrivez une fonction qui crée un objet à partir de deux tableaux"""
    return dict(zip(array1, array2))


def count_values(obj):
    """Écrivez une fonction qui compte les occurrences de valeurs dans un objet."""
    counts = {}
    for value in obj.values():
        counts[value] = counts.get(value, 0) + 1
    return counts


def extract_properties(obj, list_of_keys):
    """Écrivez une fonction qui extrait certaines propriétés d'un objet."""
    return {key: obj[key] for key in list_of_keys if key in obj}


def sort_object_by_value(obj):
    """Écrivez une fonction qui trie un objet par ses valeurs."""
    return dict(sorted(obj.items(), key=lambda item: item[1]))


def find_max_value(obj):
    """Écrivez une fonction qui trouve la valeur maximale dans un objet de nombres."""
    if not obj:
        return None
    return max(obj.values())


def create_object_from_pairs(pairs):
    """Écrivez une fonction qui créé un objet à partir d'un tableau de paires clé-valeur."""
    return dict(pairs)


def find_value_in_object(imb_obj, target_value, current_path=None):
    """Écrivez une fonction qui recherche une valeur dans un objet imbriqué."""
    if current_path is None:
        current_path = []
    for key, value in imb_obj.items():
        if value == target_value:
            return current_path + [key]
        elif isinstance(value, dict):
            result = find_value_in_object(value, target_value, current_path + [key])
            if result:
                return result
    return None


def group_by_property(list_of_objects, property_name):
    """Écrivez une fonction qui groupe les objets par une propriété spécifique."""
    grouped = {}
    for obj in list_of_objects:
        key = obj.get(property_name)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)
    return grouped


def validate_object(user_input, user_schema):
    """Écrivez une fonction qui vérifie si un objet correspond à un schéma spécifique."""
    type_mapping = {"string": str, "number": (int)}
    for key, expected_type in user_schema.items():
        if key not in user_input:
            return False
        right_type = type_mapping[expected_type]
        if not isinstance(user_input[key], right_type):
            return False
    return True


def compare_differences(obj1, obj2):
    """Écrivez une fonction qui compare les modifications entre deux objets."""
    differences = {}
    all_keys = set(obj1.keys()) | set(obj2.keys())
    for key in all_keys:
        val1 = obj1.get(key)
        val2 = obj2.get(key)
        if val1 != val2:
            if key not in obj1:
                differences[key] = {"type": "added", "old": None, "new": val2}
            elif key not in obj2:
                differences[key] = {"type": "suppressed", "old": val1, "new": None}
            else:
                differences[key] = {"type": "modified", "old": val1, "new": val2}
    return differences


def object_to_url_params(search_params):
    """Écrivez une fonction qui convertit un objet en chaîne de paramètres d'URL."""
    formatted_params = {
        k: str(v).lower() if isinstance(v, bool) else v
        for k, v in search_params.items()
    }
    return urlencode(formatted_params, quote_via=quote)


def get_object_stats(obj):
    """Écrivez une fonction qui génère un résumé statistique d'un objet contenant des nombres."""
    values = list(obj.values())
    if not values:
        return {
            "basic": {"min": None, "max": None, "average": None, "total": 0},
            "advanced": {"median": None, "variance": None, "standardDeviation": None},
        }

    values_sorted = sorted(values)
    n = len(values_sorted)
    total = sum(values_sorted)
    average = total / n

    if n % 2 == 0:
        median = (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2
    else:
        median = values_sorted[n // 2]

    variance = sum((value - average) ** 2 for value in values_sorted) / n
    standard_deviation = round(variance**0.5, 2)

    if isinstance(average, float) and average.is_integer():
        average = int(average)
    if isinstance(median, float) and median.is_integer():
        median = int(median)
    if isinstance(variance, float) and variance.is_integer():
        variance = int(variance)

    return {
        "basic": {
            "min": min(values_sorted),
            "max": max(values_sorted),
            "average": average,
            "total": total,
        },
        "advanced": {
            "median": median,
            "variance": variance,
            "standardDeviation": standard_deviation,
        },
    }
