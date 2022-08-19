class EatThemAllExceptions(Exception):
    pass


class QuitGameException(EatThemAllExceptions):
    pass


class RetryLevelException(EatThemAllExceptions):
    pass


class NextLevelException(EatThemAllExceptions):
    pass
