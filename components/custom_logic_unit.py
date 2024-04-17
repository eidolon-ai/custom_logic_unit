from eidolon_ai_sdk.cpu.logic_unit import LogicUnit, llm_function
from eidolon_ai_sdk.system.reference_model import Specable
from pydantic import BaseModel


class CustomLogicUnitConfig(BaseModel):
    config_key: str = "config default value"


class CustomLogicUnit(Specable[CustomLogicUnitConfig], LogicUnit):
    def __init__(self, **kwargs):
        LogicUnit.__init__(self, **kwargs)
        Specable.__init__(self, **kwargs)

    @llm_function()  # Python docs are used as function description by default
    async def get_location(self, lat: str, long: str) -> str:
        """
        Get the location of a given latitude and longitude
        """
        return f"tool was called with the following arguments: config value: {self.spec.config_key}, lat: {lat}, long: {long}"
