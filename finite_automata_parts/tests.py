from django.test import TestCase
from .views import *
import constants


class Mocked_Request:

    def __init__(self, data):
        self.data = data

    def data(self):
        return self.data


class Finite_Automata_Part_Tests(TestCase):

    def setUp(self) -> None:
        self.request_empty = Mocked_Request(data={})

        self.request_automaton = Mocked_Request(
            data={constants.BODY_AUTOMATON: {constants.BODY_FA_START_STATES: {0},
                                             constants.BODY_FA_TRANSITIONS: [{
                                                 constants.BODY_FA_START: 0,
                                                 constants.BODY_FA_LETTER: 'a',
                                                 constants.BODY_FA_END: 1}, {
                                                 constants.BODY_FA_START: 1,
                                                 constants.BODY_FA_LETTER: 'b',
                                                 constants.BODY_FA_END: 0}],
                                             constants.BODY_FA_ACC_STATES: {0}}
                  })

        self.request_automaton_1 = Mocked_Request(
            data={constants.BODY_AUTOMATON: {constants.BODY_FA_START_STATES: {0},
                                             constants.BODY_FA_TRANSITIONS: [{
                                                 constants.BODY_FA_START: 0,
                                                 constants.BODY_FA_LETTER: 'a',
                                                 constants.BODY_FA_END: 0}, {
                                                 constants.BODY_FA_START: 1,
                                                 constants.BODY_FA_LETTER: 'b',
                                                 constants.BODY_FA_END: 1}],
                                             constants.BODY_FA_ACC_STATES: {0}}
                  })

        self.request_automaton_2 = Mocked_Request(
            data={constants.BODY_AUTOMATON: {constants.BODY_FA_START_STATES: {0},
                                             constants.BODY_FA_TRANSITIONS: [{
                                                 constants.BODY_FA_START: 0,
                                                 constants.BODY_FA_LETTER: 'a',
                                                 constants.BODY_FA_END: 1}],
                                             constants.BODY_FA_ACC_STATES: {1}}
                  })
        self.request_automaton_3 = Mocked_Request(
            data={constants.BODY_AUTOMATON: {constants.BODY_FA_START_STATES: {0},
                                             constants.BODY_FA_TRANSITIONS: [{
                                                 constants.BODY_FA_START: 0,
                                                 constants.BODY_FA_LETTER: 'a',
                                                 constants.BODY_FA_END: 0}],
                                             constants.BODY_FA_ACC_STATES: {0}}
                  })
        self.request_two_automates = Mocked_Request(
            data={constants.BODY_AUTOMATON_1: {constants.BODY_FA_START_STATES: {0},
                                               constants.BODY_FA_TRANSITIONS: [{
                                                   constants.BODY_FA_START: 0,
                                                   constants.BODY_FA_LETTER: 'a',
                                                   constants.BODY_FA_END: 0}],
                                               constants.BODY_FA_ACC_STATES: {0}},
                  constants.BODY_AUTOMATON_2: {constants.BODY_FA_START_STATES: {0},
                                               constants.BODY_FA_TRANSITIONS: [{
                                                   constants.BODY_FA_START: 0,
                                                   constants.BODY_FA_LETTER: 'a',
                                                   constants.BODY_FA_END: 1}],
                                               constants.BODY_FA_ACC_STATES: {1}}
                  })

        self.request_equivalent_automates = Mocked_Request(
            data={constants.BODY_AUTOMATON_1: {constants.BODY_FA_START_STATES: {0},
                                               constants.BODY_FA_TRANSITIONS: [{
                                                   constants.BODY_FA_START: 0,
                                                   constants.BODY_FA_LETTER: 'a',
                                                   constants.BODY_FA_END: 0}],
                                               constants.BODY_FA_ACC_STATES: {0}},
                  constants.BODY_AUTOMATON_2: {constants.BODY_FA_START_STATES: {0},
                                               constants.BODY_FA_TRANSITIONS: [{
                                                   constants.BODY_FA_START: 0,
                                                   constants.BODY_FA_LETTER: 'a',
                                                   constants.BODY_FA_END: 0}],
                                               constants.BODY_FA_ACC_STATES: {0}}
                  })

        self.request_create = Mocked_Request(data={constants.BODY_TYPE: constants.FA_TYPE_FULL,
                                                   constants.BODY_FA_ALPHABET: ["a", "b"]})

    def test_create(self):
        # Setup
        endpoint = create()

        """Try to creat an automaton without any data
        """
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertFalse(response.exception)

        """ Crate the full language"""
        # Test
        response = endpoint.post(request=self.request_create)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON], {'start_states': {0}, 'transitions': [
            {'start': 0, 'letter': 'a', 'end': 0}, {'start': 0, 'letter': 'b', 'end': 0}], 'acc_states': {0}})

        """ Crate the empty language"""
        # Setup
        self.request_create.data[constants.BODY_TYPE] = constants.FA_TYPE_EMPTY

        # Test
        response = endpoint.post(request=self.request_create)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'start_states': {0}, 'transitions': [], 'acc_states': set()})

        """ Crate univ symbol language"""
        # Setup
        self.request_create.data[constants.BODY_TYPE] = constants.FA_TYPE_UNIV_SYMBOL
        self.request_create.data[constants.BODY_FA_LETTER] = 'a'

        # Test
        response = endpoint.post(request=self.request_create)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'acc_states': {1},
                          'start_states': {0},
                          'transitions': [{'end': 1, 'letter': 'a', 'start': 0},
                                          {'end': 1, 'letter': 'b', 'start': 0}]}
                         )

        """ Crate one symbol language"""
        # Setup
        self.request_create.data[constants.BODY_TYPE] = constants.FA_TYPE_ONE_SYMBOL
        self.request_create.data[constants.BODY_FA_LETTER] = 'a'

        # Test
        response = endpoint.post(request=self.request_create)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'acc_states': {1},
                          'start_states': {0},
                          'transitions': [{'end': 1, 'letter': 'a', 'start': 0}]}
                         )

        """ Try to create a non existing type
        """
        # Setup
        self.request_create.data[constants.BODY_TYPE] = ''

        # Test
        response = endpoint.post(request=self.request_create)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_longest_run(self):
        """ Test the longest run
        """
        # Setup
        endpoint = longest_run()

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], 2)

        """ Try to compute the longest run without automaton
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_reachable_sets(self):
        """ Compute all reachable states
        """
        # Setup
        endpoint = reachable()

        # Test
        response = endpoint.post(request=self.request_automaton_1)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], {0})

        """ Try to compute the reachable set without automaton
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_productive_sets(self):
        """ Compute all productive states
        """
        # Setup
        endpoint = productive()

        # Test
        response = endpoint.post(request=self.request_automaton_1)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], {0})

        """ Try to compute the productive set without automaton
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_simulation_pairs(self):
        """ Compute all simulation pair states
        """
        # Setup
        endpoint = simulation_pairs()

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], set())

        """ Try to compute the simulation pairs set without automaton
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_minimize(self):
        # Setup
        endpoint = minimize()

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON], {'start_states': {0}, 'transitions': [
            {'start': 0, 'letter': 'a', 'end': 1}, {'start': 1, 'letter': 'b', 'end': 0}], 'acc_states': {0}})

        """ Try to minimize the automaton without automaton.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_star_automaton(self):
        # Setup
        endpoint = star()

        # Test
        response = endpoint.post(request=self.request_automaton_2)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'start_states': {0}, 'transitions': [{'start': 0, 'letter': 'a', 'end': 0}],
                          'acc_states': {0}})

        """ Try to star the automaton without automaton.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_determine(self):
        # Setup
        endpoint = determine()

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON], {'start_states': {0}, 'transitions': [
            {'start': 0, 'letter': 'a', 'end': 1}, {'start': 1, 'letter': 'b', 'end': 0}], 'acc_states': {0}})

        """ Try to determine the automaton without automaton.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_complement(self):
        # Setup
        endpoint = complement()

        # Test
        response = endpoint.post(request=self.request_automaton_3)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'start_states': set(), 'transitions': [], 'acc_states': set()})

        """ Try to compute the complement the automaton without automaton.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_union(self):
        # Setup
        endpoint = union()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON], {'start_states': {0}, 'transitions': [
            {'start': 0, 'letter': 'a', 'end': 0}, {'start': 0, 'letter': 'a', 'end': 1}], 'acc_states': {0, 1}}
                         )

        """ Try to compute the union of two automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_concatenate(self):
        # Setup
        endpoint = concatenate()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON], {'start_states': {0}, 'transitions': [
            {'start': 0, 'letter': 'a', 'end': 0}, {'start': 0, 'letter': 'a', 'end': 1}], 'acc_states': {1}})

        """ Try to compute the concatenation of the automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_intersect(self):
        # Setup
        endpoint = intersect()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT_AUTOMATON],
                         {'start_states': {0}, 'transitions': [{'start': 0, 'letter': 'a', 'end': 1}],
                          'acc_states': {1}})

        """ Try to compute the intersection of the automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_symmetric_difference(self):
        # Setup
        endpoint = symmetric_difference()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(200, response.status_code)

        """ Try to compute the symmetrically difference of the automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_equivalent(self):
        # Setup
        endpoint = equivalent()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], False)
        self.assertEqual(response.data[constants.BODY_FALSE_WORD], 'aa')

        # Test, with two equivalent automates
        response = endpoint.post(request=self.request_equivalent_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], True)

        """ Try to compute the equivalence of the automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_inclusion(self):
        # Setup
        endpoint = inclusion()

        # Test
        response = endpoint.post(request=self.request_two_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], False)
        self.assertEqual(response.data[constants.BODY_FALSE_WORD], 'aa')

        # Test, with two equivalent automates
        response = endpoint.post(request=self.request_equivalent_automates)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], True)

        """ Try to compute the equivalence of the automates without automates.
        """
        # Test
        response = endpoint.post(request=self.request_empty)

        # Assert
        self.assertEqual(400, response.status_code)

    def test_check_the_automaton(self):
        """ Check if the automaton is empty
        """
        # Setup
        endpoint = check()
        self.request_automaton.data[constants.FA_CHECK_METHOD] = constants.FA_CHECK_IS_EMPTY

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], False)

        """ Check if the automaton accept the empty
        """
        # Setup
        self.request_automaton.data[constants.FA_CHECK_METHOD] = constants.FA_CHECK_EMTPY_WORD

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], True)

        """ Check if the automaton accept the word 'a'
        """
        # Setup
        self.request_automaton.data[constants.FA_CHECK_METHOD] = constants.FA_CHECK_WORD
        self.request_automaton.data[constants.BODY_FA_WORD] = 'a'

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(response.data[constants.BODY_RESULT], False)

        """ Try to check a method that not exists.
        """
        # Setup
        self.request_automaton.data[constants.FA_CHECK_METHOD] = ''

        # Test
        response = endpoint.post(request=self.request_automaton)

        # Assert
        self.assertEqual(400, response.status_code)
