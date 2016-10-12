"""Error"""


class ValidationError(Exception):
    """Validation Error"""
    def __init__(self, message=''):
        """Init"""
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class FormatError(ValidationError):
    """Format error"""
    pass


class ValueError(ValidationError):
    pass
