class NotFoundError(Exception):
    def __init__(*args, **kwargs):
        super().__init__(args, kwargs)
