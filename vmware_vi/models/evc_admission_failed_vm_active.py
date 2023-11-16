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


from typing import Any, ClassVar, Dict, List

from vmware_vi.models.evc_admission_failed import EVCAdmissionFailed
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EVCAdmissionFailedVmActive(EVCAdmissionFailed):
    """
    An attempt to move or add a host into an Enhanced VMotion Compatibility cluster has failed for the following reason: - The host exposes additional compatibility-relevant CPU features beyond   those present in the baseline mandated by the cluster's EVC mode. - The host has powered-on or suspended virtual machines.    Therefore the host may not be admitted into the cluster, since its virtual machines may be using CPU features suppressed in the cluster.  Note that in rare cases, this may occur even if the host's *maxEVCModeKey* corresponds to the EVC mode of the cluster. This means that even though that EVC mode is the best match for the host's hardware, the host still has some features beyond those present in the baseline for that EVC mode.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
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
        """Create an instance of EVCAdmissionFailedVmActive from a JSON string"""
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
        """Create an instance of EVCAdmissionFailedVmActive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

