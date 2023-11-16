# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Union
from pydantic import StrictFloat, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.license_manager_state_enum import LicenseManagerStateEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LicenseDiagnostics(DataObject):
    """
    Deprecated as of vSphere API 4.0, this is not used by the system.  This data object type provides summary status and diagnostic information for *LicenseManager*.  Counters in this property can be reset to zero. The property specified as a discontinuity is used to determine when this last occurred.  ***Since:*** VI API 2.5 
    """ # noqa: E501
    source_last_changed: datetime = Field(description="A timestamp of when sourceAvailable last changed state, expressed in UTC.  ***Since:*** VI API 2.5 ", alias="sourceLastChanged")
    source_lost: StrictStr = Field(description="Counter to track number of times connection to source was lost.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5 ", alias="sourceLost")
    source_latency: Union[StrictFloat, StrictInt] = Field(description="Exponentially decaying average of the transaction time for license acquisition and routine communications with LicenseSource.  Units: milliseconds.  ***Since:*** VI API 2.5 ", alias="sourceLatency")
    license_requests: StrictStr = Field(description="Counter to track total number of licenses requested.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5 ", alias="licenseRequests")
    license_request_failures: StrictStr = Field(description="Counter to track Total number of licenses requests that were not fulfilled (denied, timeout, or other).  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5 ", alias="licenseRequestFailures")
    license_feature_unknowns: StrictStr = Field(description="Counter to track Total number of license features parsed from License source that are not recognized.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5 ", alias="licenseFeatureUnknowns")
    op_state: LicenseManagerStateEnum = Field(alias="opState")
    last_status_update: datetime = Field(description="A timestamp of when opState was last updated.  ***Since:*** VI API 2.5 ", alias="lastStatusUpdate")
    op_failure_message: StrictStr = Field(description="A human readable reason when optState reports Fault condition.  ***Since:*** VI API 2.5 ", alias="opFailureMessage")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LicenseDiagnostics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LicenseDiagnostics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

