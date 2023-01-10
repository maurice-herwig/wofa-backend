from wofa import FiniteAutomata
import constants


def get_wofa_parameters(automaton, json_obj):
    """ Parse the parameter values eta, lambda and variant from the given json object and determine a default value is
    the parameter is not given in the json object.

    Args:
        automaton (FiniteAutomata): A finite automaton to determine the default values.
        json_obj (JSON): An json object with the parameters.

    Raises:
        Exception: If the variant is not words or wordLengths or eta and lambda have not the right type.

    Returns:
        int, float, string : eta, lambda, variant
    """
    # eta default the pumping constant of the given automaton.
    if constants.BODY_ETA in json_obj.keys():
        eta = json_obj[constants.BODY_ETA]

        # check the type
        if not (type(eta) == int or type(eta) == float):
            raise Exception(f'The parameter eta have the type: {type(eta)} '
                            f'but the allowed types are only: int and float')
    else:
        eta = automaton.get_length_longest_run() + 1

    # lambda default so that half of the weight up to eta and half of the weight on word lengths greater than eta.
    if constants.BODY_LAMBDA in json_obj.keys():
        lam = json_obj[constants.BODY_LAMBDA]

        # check the type
        if not (type(lam) == int or type(lam) == float):
            raise Exception(f'The parameter lambda have the type: {type(lam)} '
                            f'but the allowed types are only:float')

        # check if the value real smaller than 1
        if not (lam < 1):
            raise Exception("the parameter lambda must be less than 1.")

    else:
        lam = 0.5 ** (1 / eta)

    # variant default words.
    if constants.BODY_VARIANT in json_obj.keys():
        variant = json_obj[constants.BODY_VARIANT]

        # check if variant words or wordLengths
        if not (variant == constants.BODY_VARIANT_WORDS or variant == constants.BODY_VARIANT_WORD_LENGTHS):
            raise Exception(f'The variants to determine the weight are only words and wordLengths and not '
                            f'{variant}')
    else:
        variant = constants.BODY_VARIANT_WORDS

    # return the parameters
    return int(eta), lam, variant


def get_max_points(json_obj):
    """ Parse the max points from a given json object.

    Args:
        json_obj (JSON): An json object with the parameters.

    Raises:
        Exception: The parameter doesn't exist or have not the correct type.

    Returns:
        float: max points
    """

    # check if the value exists.
    if constants.BODY_MAX_POINTS in json_obj:
        max_points = json_obj[constants.BODY_MAX_POINTS]

        # parse a digit as string to a float
        if type(max_points) == str and max_points.isdigit():
            max_points = float(max_points)

        # check the type
        if not (type(max_points) == float or type(max_points) == int):
            raise Exception(f'The parameter max points have the type: {type(max_points)} '
                            f'but the allowed types are only:float')

        # return the value
        return float(max_points)

    else:
        raise Exception("The max points value is needed")


def get_linear_displacement(json_obj):
    """ Parse the max points from a given json object.

    Args:
        json_obj (JSON): An json object with the parameters.

    Raises:
        Exception: The parameter doesn't exist or have not the correct type.

    Returns:
        float: linear displacement.
    """

    # check if the value exists.
    if constants.BODY_LIN_DIS in json_obj:
        lin_dis = json_obj[constants.BODY_LIN_DIS]

        # parse a digit as string to a float
        if type(lin_dis) == str and lin_dis.isdigit():
            lin_dis = float(lin_dis)

        # check the type
        if not (type(lin_dis) == float or type(lin_dis) == int):
            raise Exception(f'The parameter linear displacement have the type: {type(lin_dis)} '
                            f'but the allowed types are only:float')

        # return the value
        return float(lin_dis)

    else:
        raise Exception("The linear displacement value is needed")


def get_words_list(word_list):
    """ check if all words from the str

    Args:
        word_list (list of strings): list of test words.

    Raises:
        Exception: at least one word is not from the type string.

    Returns:
        list of strings: the list of words.
    """
    res = []
    for word in word_list:
        if type(word) == str:
            res.append(word)
        else:
            raise Exception(f'the word {word} is not from the type string.')
    return res
