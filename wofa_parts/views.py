from rest_framework.response import Response
from rest_framework.views import APIView
from .controller import wofa_controller
from permissions import ClientAuthorization


class weight(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Post a finite automaton of the request and response with the weight of this automaton.

        Args:
            request (request):  The post request with the body values: automaton and the additionally
                                body values: eta, lambda, variant.

        Returns:
            Response: response with the weight as body value.
        """
        try:
            # compute the weight
            return Response(data=wofa_controller.weight(request.data),
                            status=200)

        except Exception as e:
            return Response(str(e), status=400)


class weight_diff(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Post two finite automaton in the body of the request and get the weight of these automatons.

        Args:
            request (request):  The post request with the body values: solution, test_object and the additionally
                                body values: eta, lambda, variant.

        Returns:
            Response:   with the body values: weight, the weight of words that contained only in the solution and the
                        weight of words that contained only in the test object.
        """
        try:
            # determine the weight
            return Response(data=wofa_controller.weight_diff(request.data),
                            status=200)

        except Exception as e:
            return Response(str(e), status=400)


class grading_weight(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Post a solution and a test object in the body of the request and get as response a points proposal for this
            combination.

        Args:
            request (request):  The post request with the body values: solution, test_object, max_points,
            linear displacement and the additionally body values: eta, lambda, variant.

        Returns:
            Response: response with the points proposal as body value.
        """
        try:
            # determine the points' proposal.
            return Response(data=wofa_controller.grading_weight(request.data),
                            status=200)

        except Exception as e:
            return Response(str(e), status=400)


class grading_subsets(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Post a solution and a test object in the body of the request and get as response a points proposal for this
            combination with the subset method.

            Args:
                request (request):  The post request with the body values: solution, test_object, max_points.

            Returns:
                Response: response with the points proposal as body value.
            """
        try:
            # determine the points' proposal.
            return Response(data=wofa_controller.grading_subsets(request.data),
                            status=200)

        except Exception as e:
            return Response(str(e), status=400)


class grading_test_words(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Post a solution and a test words in the body of the request and get as response a points proposal for this
                    combination with the subset method.

            Args:
                request (request):  The post request with the body values: test_object, max_points, containing_words and
                                    not included words.

            Returns:
                Response: response with the points proposal as body value.
            """
        try:
            # determine the points' proposal.
            return Response(data=wofa_controller.grading_test_words(request.data),
                            status=200)

        except Exception as e:
            return Response(str(e), status=400)
