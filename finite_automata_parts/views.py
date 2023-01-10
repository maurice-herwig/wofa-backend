from rest_framework.views import APIView
from .controller import fa_controller
from rest_framework.response import Response
from permissions import ClientAuthorization


class create(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Send a post request to this endpoint to create a new automaton.

        Args:
            request (Request): Request with the needed body value: type and the additionally values alphabet and
                             letter

        Returns:
            Response: Response with the json context of the created automaton.
        """
        try:
            return Response(data=fa_controller.create_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class check(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint we can make checks at the automaton. Here we can check word, is_empty and empty_word.

        Args:
            request (Request): Request to this endpoint with the body values: automaton, method and by the check_word
                            method the word.

        Returns:
            Response: Response with the result of the check.
        """
        try:
            return Response(data=fa_controller.check_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class longest_run(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint can we compute the longest_run on the automaton without visit one state twice.

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the answer of the request
        """
        try:
            return Response(data=fa_controller.compute_longest_run(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class reachable(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint can we compute all reachable states of the automaton

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the answer of the request
        """
        try:
            return Response(data=fa_controller.reachable_states(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class productive(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint can we compute all productive states of the automaton

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the answer of the request
        """
        try:
            return Response(data=fa_controller.productive_states(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class simulation_pairs(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint wan we compute states that are simulation equivalent.

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the answer of the request
        """
        try:
            return Response(data=fa_controller.compute_sim_pairs(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class minimize(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Minimize the given automaton.

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the minimized automaton.
        """
        try:
            return Response(data=fa_controller.minimize_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class star(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Star the given automaton

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the stared automaton.
        """
        try:
            return Response(data=fa_controller.star_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class determine(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Determine the given automaton.

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the stared automaton.
        """
        try:
            return Response(data=fa_controller.determine_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class complement(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ Compute the complement of the given automaton

        Args:
            request (Request): The request to this endpoint, with the body value automaton.

        Returns:
            Response: Response with the complement automaton.
        """
        try:
            return Response(data=fa_controller.complement_automaton(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class union(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint can we compute the union of two given automaton

        Args:
            request (Request): The request to this endpoint, with the body values' automaton_1 and automaton_2

        Returns:
            Response: Response with the union automaton of the two given automates.
        """
        try:
            return Response(data=fa_controller.union_two_automates(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class concatenate(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint we can compute the concatenation of two given automates.

        Args:
            request (Request): The request to this endpoint, with the body values' automaton_1 and automaton_2

        Returns:
            Response: Response with the concatenation automaton of the two given automates.
        """
        try:
            return Response(data=fa_controller.concatenate_two_automates(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class intersect(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint we can compute the intersection of two given automates.

        Args:
            request (Request): The request to this endpoint, with the body values' automaton_1 and automaton_2

        Returns:
            Response: Response with the intersection automaton of the two given automates.
        """
        try:
            return Response(data=fa_controller.intersect_two_automates(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class symmetric_difference(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """ At this endpoint we can compute the symmetric difference of the two given automates.

        Args:
            request (Request): The request to this endpoint, with the body values' automaton_1 and automaton_2

        Returns:
            Response: Response with the symmetric difference automaton of the two given automates.
        """
        try:
            return Response(data=fa_controller.compute_sym_difference(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class equivalent(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            return Response(data=fa_controller.check_equivalence(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)


class inclusion(APIView):
    permission_classes = [ClientAuthorization]

    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            return Response(data=fa_controller.check_inclusion(data=request.data),
                            status=200)
        except Exception as e:
            return Response(str(e), status=400)
