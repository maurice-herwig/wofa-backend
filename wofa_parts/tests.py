from django.test import TestCase
import constants
from .controller import wofa_controller


class WofaControllerTest(TestCase):
    
    def setUp(self) -> None:
        self.automaton_1_as_json = {constants.BODY_FA_START_STATES: ["1", "2"],
                                    constants.BODY_FA_TRANSITIONS: [{
                                        constants.BODY_FA_START: "1",
                                        constants.BODY_FA_LETTER: "a",
                                        constants.BODY_FA_END: "2"
                                    }, {
                                        constants.BODY_FA_START: "2",
                                        constants.BODY_FA_LETTER: "b",
                                        constants.BODY_FA_END: "1"}],
                                    constants.BODY_FA_ACC_STATES: ["2"]}

        self.automaton_2_as_json = {constants.BODY_FA_START_STATES: ["1", "2"],
                                    constants.BODY_FA_TRANSITIONS: [{
                                        constants.BODY_FA_START: "1",
                                        constants.BODY_FA_LETTER: "a",
                                        constants.BODY_FA_END: "2"}],
                                    constants.BODY_FA_ACC_STATES: []}

        self.automaton_3_as_txt = {constants.BODY_TYPE: constants.BODY_TYPE_TXT,
                                   constants.BODY_VALUE: "input_alphabet = a, b \n\n start_states = 0 \n\n transitions "
                                                         "= 0,a -> 1 \n 0,b -> 0 \n 1,a -> 1 \n 1,b -> 2 \n 2,a -> 1 "
                                                         "\n 2,b -> 3 \n 3,b -> 0 \n\n\n acc_states = 0,1,2,3 \n"}

    def test_weight(self):
        # Setup
        data = {constants.BODY_AUTOMATON: self.automaton_1_as_json}

        # Test with default values
        self.assertEqual(0.16932351979419896, wofa_controller.weight(data=data)[constants.BODY_WEIGHT])

        # Setup additionally parameters
        data[constants.BODY_ETA] = 5
        data[constants.BODY_LAMBDA] = 0.75
        data[constants.BODY_VARIANT] = constants.BODY_VARIANT_WORD_LENGTHS

        # Test with the new parameters values
        self.assertEqual(0.27083816528320304, wofa_controller.weight(data=data)[constants.BODY_WEIGHT])

        # Setup with the automaton 3
        data[constants.BODY_AUTOMATON] = self.automaton_3_as_txt

        # Test with the automation 3
        self.assertEqual(0.916783613413958, wofa_controller.weight(data=data)[constants.BODY_WEIGHT])

        # assert

        # Test try to compute the weight of an automation without description
        data[constants.BODY_AUTOMATON] = {}

        # Test
        try:
            wofa_controller.weight(data=data)
        except Exception as e:
            self.assertEqual(str(e), "'start_states'")

    def test_weight_diff(self):
        # Setup
        data = {constants.BODY_AUTOMATON_1: self.automaton_1_as_json,
                constants.BODY_AUTOMATON_2: self.automaton_2_as_json}

        # Test
        response = wofa_controller.weight_diff(data=data)

        # Assert
        self.assertEqual(response[constants.BODY_WEIGHT], 0.16932351979419896)
        self.assertEqual(response[constants.BODY_WEIGHT_ONLY_SOLUTION], 0.16932351979419896)
        self.assertEqual(response[constants.BODY_WEIGHT_ONLY_TEST_OBJECT], 0)

        # Test try to compute the weight of an automation without description
        data[constants.BODY_SOLUTION] = {}

        # Test
        try:
            wofa_controller.weight_diff(data=data)
        except Exception as e:
            self.assertEqual(str(e), "'start_states'")

    def test_grading_weight(self):
        # Setup
        data = {constants.BODY_AUTOMATON_1: self.automaton_1_as_json,
                constants.BODY_AUTOMATON_2: self.automaton_2_as_json,
                constants.BODY_MAX_POINTS: 10,
                constants.BODY_LIN_DIS: 5}

        # Test
        response = wofa_controller.grading_weight(data=data)

        # Assert
        self.assertEqual(response[constants.BODY_POINTS], 0)

        # Don't set the linear displacement value
        del data[constants.BODY_LIN_DIS]

        # Test
        try:
            wofa_controller.grading_weight(data=data)
        except Exception as e:
            self.assertEqual(str(e), 'The linear displacement value is needed')

    def test_grading_subsets(self):
        # Setup
        data = {constants.BODY_AUTOMATON_1: self.automaton_1_as_json,
                constants.BODY_AUTOMATON_2: self.automaton_2_as_json,
                constants.BODY_MAX_POINTS: 2}

        # Test
        response = wofa_controller.grading_subsets(data=data)

        # Assert
        self.assertEqual(response[constants.BODY_POINTS], 1)

        # Don't set the max point value
        del data[constants.BODY_MAX_POINTS]

        # Test
        try:
            wofa_controller.grading_subsets(data=data)
        except Exception as e:
            self.assertEqual(str(e), 'The max points value is needed')

    def test_grading_test_words(self):
        # Setup
        data = {constants.BODY_AUTOMATON: self.automaton_1_as_json,
                constants.BODY_MAX_POINTS: 6,
                constants.BODY_CONTAINING_WORDS: ['', 'a', 'b'],
                constants.BODY_NOT_INCLUDED_WORDS: ['aa', 'bb', 'ab']}

        # Test
        response = wofa_controller.grading_test_words(data=data)

        # Assert
        self.assertEqual(response[constants.BODY_POINTS], 5)

        # Don't set the not included words
        del data[constants.BODY_NOT_INCLUDED_WORDS]

        # Test
        try:
            wofa_controller.grading_test_words(data=data)
        except Exception as e:
            self.assertEqual(str(e), "'not_included_words'")

