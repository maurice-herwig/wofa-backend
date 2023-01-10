import constants
from wofa import FiniteAutomata
import automaton_parser


def parse_type_of_creation(data):
    """ Parse the type of nfa that we want to create.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The data field is needed.

    Returns:
        str: The type that the user want to create.
    """
    if constants.BODY_TYPE in data.keys():
        return data[constants.BODY_TYPE]
    else:
        raise Exception('The type field is needed.')


def parse_and_set_alphabet(data):
    """ Parse the alphabet from the data and set the FiniteAutomaton class variable to this value.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The alphabet isn't a list or the field is needed.

    Returns:
        list: The alphabet as list.
    """
    if constants.BODY_FA_ALPHABET in data.keys():

        # parse the alphabet
        alphabet = data[constants.BODY_FA_ALPHABET]

        # Check if the alphabet from type list
        if not isinstance(alphabet, list):
            raise Exception('The alphabet must be an list.')

        # Set the alphabet
        FiniteAutomata.set_alphabet(sigma=alphabet)

        return alphabet

    else:
        raise Exception('The field alphabet is needed.')


def parse_letter(data):
    """ Parse the letter form the data.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The field is needed.

    Returns:
        str: The letter.
    """
    if constants.BODY_FA_LETTER in data.keys():
        return data[constants.BODY_FA_LETTER]
    else:
        raise Exception('The letter field is needed.')


def get_two_automates_and_set_alphabet(data):
    """ Parse the two automates and set the alphabet, by the given value or if the alphabet don't give set the alphabet
     by ll used letter of the transitions of the automates.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: One of the automates cannot parse.

    Returns:
        FiniteAutomata, FiniteAutomata: The parsed automates
    """
    try:
        # Get the automates
        automaton1, alphabet1 = automaton_parser.parse_automaton(data[constants.BODY_AUTOMATON_1])
        automaton2, alphabet2 = automaton_parser.parse_automaton(data[constants.BODY_AUTOMATON_2])

        # Check if the alphabet is given separately.
        if constants.BODY_FA_ALPHABET in data.keys():
            parse_and_set_alphabet(data=data)
        else:
            # Else set the alphabet by the default values.
            FiniteAutomata.set_alphabet(alphabet1.union(alphabet2))

        return automaton1, automaton2

    except Exception as e:
        raise Exception(str(e))


def get_automaton_and_set_alphabet(data):
    """ Parse the automaton and set the alphabet, by the given value or if the alphabet don't give set the alphabet by
    all used letter of the transitions of the automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The automaton cannot parse

    Returns:
        FiniteAutomata: The parsed automaton
    """
    try:
        # Get the automates
        automaton, alphabet = automaton_parser.parse_automaton(data[constants.BODY_AUTOMATON])

        # Check if the alphabet is given separately.
        if constants.BODY_FA_ALPHABET in data.keys():
            parse_and_set_alphabet(data=data)
        else:
            # Else set the alphabet by the default values.
            FiniteAutomata.set_alphabet(alphabet)

        return automaton

    except Exception as e:
        raise Exception(str(e))


def parse_check_method(data):
    """ Parse the method that we want to make a check on a given nfa.

    Args:
       data (dict): The data from the request data.

    Raises:
        Exception: The method field is needed.

    Returns:
        str: The parsed method.
    """
    if constants.FA_CHECK_METHOD in data.keys():
        return data[constants.FA_CHECK_METHOD]
    else:
        raise Exception('The method field is needed.')


def parse_word(data):
    """ Parse the word of the word value.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The word field is needed.

    Returns:
        str: the parsed word.
    """
    if constants.BODY_FA_WORD in data.keys():
        return data[constants.BODY_FA_WORD]
    else:
        raise Exception('The word field is needed.')
