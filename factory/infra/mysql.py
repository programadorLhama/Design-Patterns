from typing import Dict
from interface import DatabaseInterface

class MysqlRepository (DatabaseInterface):

    def select_one(self) -> Dict:
        return {
            "success": True,
            "data": 'Ola Mundo'
        }
