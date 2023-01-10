from wofa import FiniteAutomata
import constants
import wofa.Parser as parser_from_wofa
import re


def parse_automaton(json_obj):
    """ Method can parse an automaton that is decoded in different ways.
        Currently, possible decoding types (body parameter type):
            - json is the default type:
                 needs body parameters: start_states, transitions and acc_states
            - txt:
                needs body parameter value: string that decoded the automaton
                IMPORTANT: the value string need the format that every information is in a new line.
                Example: "input_alphabet = a, b start_states = 0 \n transitions = 0,a -> 1 \n 0,b -> 0 \n 1,a -> 1
                       \n 1,b -> 2 \n 2,a -> 1 \n 2,b -> 3 \n 3,b -> 0 \n acc_states = 0,1,2,3 \n"

            TODO: add more types e.g: RegEx

    Args:
        json_obj (JSON): The Finite Automaton in a JSON Format

    Raises:
        Exception: Of the error in the parsing process.

    Returns:
        FiniteAutomata, set: the created finite_automata_parts object and the used alphabet of this automaton.
    """

    # Get the decoding type of the automaton default is JSON
    if constants.BODY_TYPE in json_obj.keys():
        automaton_type = json_obj[constants.BODY_TYPE]
    else:
        automaton_type = constants.BODY_TYPE_JSON

    # Call the parsing method for this type
    # json
    if automaton_type == constants.BODY_TYPE_JSON:
        try:
            return json_to_finite_automata(json_obj=json_obj)
        except Exception as e:
            raise Exception(str(e))

    # txt
    elif automaton_type == constants.BODY_TYPE_TXT:
        try:
            # Create a finite_automata_parts Object
            finite_automata = parser_from_wofa.parse(json_obj[constants.BODY_VALUE].split('\n'))

            # Determine the used alphabet
            alphabet = set()
            for t in finite_automata.get_transitions():
                alphabet.add(t[1])

            # Return the automaton and the alphabet
            return finite_automata, alphabet

        except Exception as e:
            raise Exception(str(e))

    else:
        raise Exception("Type value match no type")


def json_to_finite_automata(json_obj):
    """ Parse a Finite Automaton in a JSON format into a finite_automata_parts Object from wofa.

        Args:
            json_obj (JSON): The Finite Automaton in a JSON Format

        Raises:
            Exception: Of the error in the parsing process.

        Returns:
            FiniteAutomata, set: the created finite_automata_parts object and the alphabet of this automaton.
        """

    def __parse_states(st, state_co, state_di):
        """ Auxiliary method to parse the states
        """
        # Parse the state
        if isinstance(st, str):
            st = st.strip()
        elif isinstance(st, int):
            st = str(st)
        else:
            raise Exception('The type of states can only from integer or string.')

        if re.match(constants.CONST_STATE_NAME, st):
            if st not in state_di:
                state_di[st.strip()] = state_co
                state_co += 1
                return state_di[st.strip()], state_co, state_di
            return state_di[st], state_co, state_di
        else:
            raise Exception(f'Error: Unexpected symbol in state identifier. ({st})')

    """ Start of the main method. 
    """

    try:
        start_states = json_obj[constants.BODY_FA_START_STATES]
        given_transitions = json_obj[constants.BODY_FA_TRANSITIONS]
        final_states = json_obj[constants.BODY_FA_ACC_STATES]
    except Exception as e:
        raise Exception(str(e))

    state_dict = dict()
    state_counter = 0

    initials = set()
    transitions = []
    finals = set()

    alphabet = set()

    # initial states
    for state in start_states:
        try:
            state, state_counter, state_dict = __parse_states(st=state, state_di=state_dict, state_co=state_counter)
            initials.add(state)
        except Exception as e:
            raise Exception(str(e))

    # final states
    for state in final_states:
        try:
            state, state_counter, state_dict = __parse_states(st=state, state_di=state_dict, state_co=state_counter)
            finals.add(state)
        except Exception as e:
            raise Exception(str(e))

    # transitions
    for trans in given_transitions:
        # start state of the transition
        start, state_counter, state_dict = __parse_states(st=trans[constants.BODY_FA_START],
                                                          state_di=state_dict,
                                                          state_co=state_counter)

        end, state_counter, state_dict = __parse_states(st=trans[constants.BODY_FA_END],
                                                        state_di=state_dict,
                                                        state_co=state_counter)

        # letter
        letter = trans[constants.BODY_FA_LETTER].strip()

        # add the letter to the alphabet
        alphabet.add(letter)

        # add the transition
        transitions.append((start, letter, end))

    return FiniteAutomata(initials, transitions, finals), alphabet


def finite_automata_to_json(automaton: FiniteAutomata):
    """ Translate an automaton from a FiniteAutomat object to the json format for automatons.

    Args:
        automaton (FiniteAutomata): The automaton that we want to translate.

    Returns:
        dict: The automaton in json format.
    """
    # translate the transitions to the json format.
    transitions = []
    for start, letter, end in automaton.get_transitions():
        transitions.append({constants.BODY_FA_START: start,
                            constants.BODY_FA_LETTER: letter,
                            constants.BODY_FA_END: end})

    # translate the complete automaton to the json format.
    return {constants.BODY_FA_START_STATES: automaton.get_initials(),
            constants.BODY_FA_TRANSITIONS: transitions,
            constants.BODY_FA_ACC_STATES: automaton.get_finals()}
