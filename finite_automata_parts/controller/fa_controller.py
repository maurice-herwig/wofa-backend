from wofa import FiniteAutomata
import constants
import automaton_parser
from ..controller import fa_parser


def create_automaton(data):
    """ Create a new automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The creation failed.

    Returns:
        dict: The json context of the new automaton
    """
    # Get the type that are to crated
    type_to_crate = fa_parser.parse_type_of_creation(data=data)

    # Set the alphabet
    fa_parser.parse_and_set_alphabet(data=data)

    # Create a nfa that only accept the word of the letter of the input letter.
    if type_to_crate == constants.FA_TYPE_ONE_SYMBOL:
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=FiniteAutomata.one_symbol_nfa(
                a=fa_parser.parse_letter(data=data)))}

    # Create a nfa that accept all words of length one.
    elif type_to_crate == constants.FA_TYPE_UNIV_SYMBOL:
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=FiniteAutomata.univ_symbol_nfa())}

    # Create the full nfa for the given alphabet.
    elif type_to_crate == constants.FA_TYPE_FULL:
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=FiniteAutomata.full_nfa())}

    # Create the empty nfa.
    elif type_to_crate == constants.FA_TYPE_EMPTY:
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=FiniteAutomata.empty_nfa())}

    # This type to create don't exist.
    else:
        raise Exception(f'The tool can only create automatons of type {constants.FA_TYPE_EMPTY}, '
                        f'{constants.FA_TYPE_FULL}, {constants.FA_TYPE_ONE_SYMBOL} and '
                        f'{constants.FA_TYPE_UNIV_SYMBOL}.')


def check_automaton(data):
    """ Check if the given automaton an empty automaton or accept a given word or accept the empty word. The
        thing what we check appends on the given method.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the result of the operation at the result value
    """
    try:
        # Get the automaton.
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Parse what we want to check.
        check_what = fa_parser.parse_check_method(data=data)

        # Check if the automaton empty.
        if check_what == constants.FA_CHECK_IS_EMPTY:
            return {constants.BODY_RESULT: automaton.is_empty()}

        # Check if the automaton accept the empty word.
        elif check_what == constants.FA_CHECK_EMTPY_WORD:
            return {constants.BODY_RESULT: automaton.accepts_empty_word()}

        # Check if the automaton accept a given word.
        elif check_what == constants.FA_CHECK_WORD:
            return {constants.BODY_RESULT: automaton.accepts_word(word=fa_parser.parse_word(data=data))}

        else:
            raise Exception(f'This endpoint support only this check methods {constants.FA_CHECK_IS_EMPTY}, '
                            f'{constants.FA_CHECK_WORD}, {constants.FA_CHECK_EMTPY_WORD}.')

    except Exception as e:
        raise Exception(str(e))


def compute_longest_run(data):
    """ Compute the length of the longest run of the given automaton without that any state visited two times.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the result of the operation at the result value
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Compute the longest run
        return {constants.BODY_RESULT: automaton.get_length_longest_run()}

    except Exception as e:
        raise Exception(str(e))


def reachable_states(data):
    """ Compute all reachable states of the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the result of the operation at the result value
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Compute all reachable states
        return {constants.BODY_RESULT: automaton.reachable()}

    except Exception as e:
        raise Exception(str(e))


def productive_states(data):
    """ Compute all productive states of the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the result of the operation at the result value
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Compute all productive states
        return {constants.BODY_RESULT: automaton.productive()}

    except Exception as e:
        raise Exception(str(e))


def compute_sim_pairs(data):
    """ Compute the simulation pairs of states of the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the result of the operation at the result value.
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Compute simulation pais of states
        return {constants.BODY_RESULT: automaton.simulation_pairs()}

    except Exception as e:
        raise Exception(str(e))


def minimize_automaton(data):
    """ Minimize the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Minimize the automaton
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton.minimize())}

    except Exception as e:
        raise Exception(str(e))


def star_automaton(data):
    """ Star the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Star the automaton
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(automaton=automaton.star())}

    except Exception as e:
        raise Exception(str(e))


def determine_automaton(data):
    """ Determine the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Determine the automaton
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton.determine())}

    except Exception as e:
        raise Exception(str(e))


def complement_automaton(data):
    """ Compute the complement of the given automaton.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automaton
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Complement the automaton
        return {
            constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(automaton=automaton.complement())}

    except Exception as e:
        raise Exception(str(e))


def union_two_automates(data):
    """ Union the two given automates.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
       dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Union the two automates
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton1.union(automaton2))}

    except Exception as e:
        raise Exception(str(e))


def concatenate_two_automates(data):
    """ Concatenate the two given automates.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Concatenate the two automates
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton1.concatenate(automaton2))}

    except Exception as e:
        raise Exception(str(e))


def intersect_two_automates(data):
    """ Compute the intersection of the language of the two given automates.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Concatenate the two automates
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton1.intersect(automaton2))}

    except Exception as e:
        raise Exception(str(e))


def compute_sym_difference(data):
    """ Compute the symmetrical difference of the languages of the given automates.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Concatenate the two automates
        return {constants.BODY_RESULT_AUTOMATON: automaton_parser.finite_automata_to_json(
            automaton=automaton1.symmetric_difference(automaton2))}

    except Exception as e:
        raise Exception(str(e))


def check_equivalence(data):
    """ Check if the languages of the two given automates are equivalent.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Check if the two automates equivalent
        res, false_word = automaton1.equivalence_test(other=automaton2)

        # Create the result context
        context = {constants.BODY_RESULT: res}

        # If the automatons not equivalent add a word as representative
        if not res:
            context[constants.BODY_FALSE_WORD] = false_word.strip()

        return context

    except Exception as e:
        raise Exception(str(e))


def check_inclusion(data):
    """ Check if the language of the given automation_1 a subset of automaton_2.

    Args:
        data (dict): The data from the request data.

    Raises:
        Exception: The computation failed.

    Returns:
        dict: with the resulting automaton in the result_automaton value.
    """
    try:
        # Get the automates
        automaton1, automaton2 = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Check if automaton a subset of automaton 2
        res, false_word = automaton1.inclusion(other=automaton2)

        # Create the result context
        context = {constants.BODY_RESULT: res}

        # If the automatons not a subset add a false word as representative
        if not res:
            context[constants.BODY_FALSE_WORD] = false_word.strip()

        return context

    except Exception as e:
        raise Exception(str(e))
