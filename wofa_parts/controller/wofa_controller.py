from wofa import WeightFiniteAutomata, Gradings
from .wofa_parser import get_wofa_parameters, get_max_points, get_linear_displacement, get_words_list
import constants
from finite_automata_parts.controller import fa_parser


def weight(data):
    """ Determine the weight of a given finite automaton in an JSON format.

    Args:
        data (JSON): the finite automaton object in a JSON format and the additionally parameters.

    Raises:
        Exception: The errors of the process.

    Returns:
        dict: the weight of the automaton.
    """
    try:
        # Get the automaton and set the alphabet
        automaton = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Determine the parameters.
        eta, lam, variant = get_wofa_parameters(automaton, data)

        # return the weight
        return {constants.BODY_WEIGHT: WeightFiniteAutomata.weight(dfa=automaton.determine(),
                                                                   eta=eta,
                                                                   lam=lam,
                                                                   variant=variant)}

    except Exception as e:
        raise Exception(str(e))


def weight_diff(data):
    """ Determine the weight of the symmetrical difference of two finite automatons given in an JSON format.

    Args:
        data (JSON): the finite automaton objects in JSON format and the additionally parameters.

    Raises:
        Exception: The errors of the process.

    Returns:
        dict: with the three keys  weight, weight_only_solution, weight_only_test_object
                            1: The weight of the language containing the words contained only in the solution
                                and not in test object.
                            2: The weight of the language containing the words contained only in test object
                                and not in the solution.
                            3: The weight of the symmetrical difference.
    """
    try:
        # Get the automatons and set the alphabet
        solution, test_obj = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Determine the parameters.
        eta, lam, variant = get_wofa_parameters(solution, data)

        # compute the weight
        weight_difference = WeightFiniteAutomata.weight_diff(fa_a=solution,
                                                             fa_b=test_obj,
                                                             eta=eta,
                                                             lam=lam,
                                                             variant=variant)

        return {constants.BODY_WEIGHT: weight_difference[2],
                constants.BODY_WEIGHT_ONLY_SOLUTION: weight_difference[0],
                constants.BODY_WEIGHT_ONLY_TEST_OBJECT: weight_difference[1]}

    except Exception as e:
        raise Exception(str(e))


def grading_weight(data):
    """ Determine a point proposal for a solution and a test object, with the weighting method.

    Args:
        data (JSON): the finite automaton objects in JSON format and the additionally parameters.

    Raises:
        Exception: The errors of the process.

    Returns:
        dict: with a point proposal.
    """
    try:
        # Get the automatons and set the alphabet
        solution, test_obj = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Determine the parameters.
        eta, lam, variant = get_wofa_parameters(solution, data)

        # Get max points
        max_points = get_max_points(data)

        # Get the linear displacement
        lin_dis = get_linear_displacement(data)

        # computes a points proposal
        return {constants.BODY_POINTS: Gradings.grading_weight(solution=solution,
                                                               test_obj=test_obj,
                                                               eta=eta,
                                                               lam=lam,
                                                               max_po=max_points,
                                                               lin_dis=lin_dis,
                                                               variant=variant)}

    except Exception as e:
        raise Exception(str(e))


def grading_subsets(data):
    """ Determine a point proposal for a solution and a test object, with the subset method.

    Args:
        data (JSON): the finite automaton objects in JSON format.

    Raises:
        Exception: The errors of the process.

    Returns:
        dict: a point proposal.
    """
    try:
        # Get the automatons and set the alphabet
        solution, test_obj = fa_parser.get_two_automates_and_set_alphabet(data=data)

        # Get max points
        max_points = get_max_points(data)

        # returns a points proposal
        return {constants.BODY_POINTS: Gradings.grading_subsets(solution=solution,
                                                                test_obj=test_obj,
                                                                max_po=max_points)}
    except Exception as e:
        raise Exception(str(e))


def grading_test_words(data):
    """ Determine a point proposal for a solution and a test object, with the test word method.

    Args:
        data (JSON): the finite automaton object, containing_words, not_included_words and max_points in JSON format.

    Raises:
        Exception: The errors of the process.

    Returns:
        dict: a point proposal.
    """
    try:
        # Get the automaton and set the alphabet
        test_obj = fa_parser.get_automaton_and_set_alphabet(data=data)

        # Get max points
        max_points = get_max_points(data)

        # Get containing_words and not included words
        containing_words = get_words_list(data[constants.BODY_CONTAINING_WORDS])
        not_included_words = get_words_list(data[constants.BODY_NOT_INCLUDED_WORDS])

        # returns a points proposal
        return {constants.BODY_POINTS: Gradings.grading_test_words(test_obj=test_obj,
                                                                   max_po=max_points,
                                                                   containing_words=containing_words,
                                                                   not_included_words=not_included_words)}

    except Exception as e:
        raise Exception(str(e))
