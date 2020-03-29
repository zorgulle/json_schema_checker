import logging
logger = logging.getLogger(__name__)


class List:
    def __init__(self, possible_types):
        self._types = possible_types

    def is_valid(self, values) -> bool:
        """
        Took an iterable and check if all element are one of the possible types
        :param values:
        :return:
        """

        is_valid = False
        for value in values:
            if any(t.is_valid(value) for t in self._types):
                is_valid = True
            else:
                logger.info("%s is not one of types %s" % (str(value), str(self._types)))
                is_valid = False
        return is_valid

class IntList:
    def __init__(self):
        from json_schema_checker.validators import Int
        self._types = [Int()]

    def is_valid(self, values) -> bool:
        """
        Took an iterable and check if all element are one of the possible types
        :param values:
        :return:
        """

        is_valid = False
        for value in values:
            if any(t.is_valid(value) for t in self._types):
                is_valid = True
            else:
                logger.info("%s is not one of types %s" % (str(value), str(self._types)))
                is_valid = False
        return is_valid
