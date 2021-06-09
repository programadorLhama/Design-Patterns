from infra import MysqlRepository
from controllers import UseCase

class UseCaseFactory:

    @staticmethod
    def create() -> UseCase:
        return UseCase(MysqlRepository())
