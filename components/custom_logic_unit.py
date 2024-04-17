import csv
from typing import List

from eidolon_ai_sdk.cpu.logic_unit import LogicUnit, llm_function
from eidolon_ai_sdk.system.reference_model import Specable
from pydantic import BaseModel


class CustomLogicUnitConfig(BaseModel):
    csv_location: str = "chargers.csv"
    parse_args: dict = {"delimiter": ' ', "quotechar": '|'}


class ChargerSearcher(Specable[CustomLogicUnitConfig], LogicUnit):
    def __init__(self, **kwargs):
        LogicUnit.__init__(self, **kwargs)
        Specable.__init__(self, **kwargs)

    @llm_function()  # Python docs are used as function description by default
    async def get_chargers_near_location(self, lat: str, long: str, max_drive_time_seconds: int = 300) -> List[dict]:
        """
        Get the chargers within a certain drive time of a given latitude and longitude
        """
        csv.reader(self.spec.csv_location, **self.spec.parse_args)  # todo parse however we want it later


        results = []
        # todo do search
        return results

    @llm_function()  # Python docs are used as function description by default
    async def method_2(self, lat: str, long: str, max_drive_time_seconds: int = 300) -> List[dict]:
        """
        Get the chargers within a certain drive time of a given latitude and longitude
        """
        csv.reader(self.spec.csv_location, **self.spec.parse_args)  # todo parse however we want it later


        results = []
        # todo do search
        return None

