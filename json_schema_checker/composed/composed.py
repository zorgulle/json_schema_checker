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

        for value in values:
            if any(t.is_valid(value) for t in self._types):
                continue
            else:
                logger.info("%s is not one of types %s" % (str(value), str(self._types)))
                return False
        return True
