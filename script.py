"""test on string"""

import unicodedata


def count_char(text):
    """Créez une fonction qui prend une chaîne de caractères en
    paramètre et retourne sa longueur après avoir supprimé tous les espaces."""
    return len(text.replace(" ", ""))


def greeting(first_name):
    """Développez une fonction qui accepte un prénom en paramètre
    et renvoie une salutation personnalisée en mettant la première lettre en majuscule."""
    return f"Bonjour {first_name.title()}"


def exclamation_point(text):
    """Écrivez une fonction qui détermine si une chaîne
    de caractères se termine par un point d'exclamation."""
    return text.endswith("!")


def reverse_words(text):
    """Créez une fonction qui prend une chaîne de caractères
    en paramètre et retourne une nouvelle chaîne avec les mots dans l'ordre inverse."""
    return " ".join(text.split()[::-1])


def count_letter(text, letter):
    """Écrivez une fonction qui compte le nombre
    d'occurrences d'une lettre dans une chaîne"""
    return text.count(letter)


def to_camel_case(text):
    """Écrivez une fonction qui convertit une chaîne en camelCase."""
    words = text.replace("_", " ").split()
    return words[0].lower() + "".join(word.title() for word in words[1:])


def count_vowels(text):
    """Écrivez une fonction qui compte le nombre de voyelles dans une chaîne."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def min_maj_alternate(text):
    """Écrivez une fonction qui alterne majuscules et minuscules dans une chaîne."""
    result = []
    for i, char in enumerate(text):
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


def remove_duplicates(text):
    """Écrivez une fonction qui supprime les caractères en double consécutifs."""
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)


def extract_initials(name):
    """Écrivez une fonction qui extrait les initiales d'un nom complet."""
    words = name.split()
    initials = [word[0].upper() for word in words if word]
    return "".join(initials)


def mask_string(text, n):
    """Écrivez une fonction qui masque les caractères d'une chaîne sauf
    les N derniers."""
    if len(text) <= n:
        return text
    return "*" * (len(text) - n) + text[-n:]


def is_palindrome(text):
    """Écrivez une fonction qui vérifie si une chaîne est un palindrome."""
    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(
        char for char in normalized if unicodedata.category(char) != "Mn"
    )
    cleaned = "".join(char.lower() for char in without_accents if char.isalnum())
    return cleaned == cleaned[::-1]


def longest_sequence(text):
    """Écrivez une fonction qui trouve la plus longue séquence
    de caractères identiques."""
    if not text:  # Si la chaîne est vide
        return ""
    char_max = text[0]
    long_max = 1
    present_char = text[0]
    present_long = 1
    for char in text[1:]:
        if present_char == char:
            present_long += 1
        else:
            if present_long > long_max:
                long_max = present_long
                char_max = present_char
            present_long = 1
            present_char = char
    if present_long > long_max:
        long_max = present_long
        char_max = present_char
    return char_max * long_max


def format_ellipsis(text, n):
    """Écrivez une fonction qui formate un texte en
    ajoutant des points de suspension"""
    return text[: n - 3] + "..."


def capitalize_words(text):
    """Écrivez une fonction qui capitalise la première lettre
    de chaque mot"""
    return text.title()
