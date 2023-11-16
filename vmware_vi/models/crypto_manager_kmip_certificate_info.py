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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CryptoManagerKmipCertificateInfo(DataObject):
    """
    Basic information of a certificate.  ***Since:*** vSphere API 6.5 
    """ # noqa: E501
    subject: StrictStr = Field(description="Subject identifies whom the certificate is issued to.  ***Since:*** vSphere API 6.5 ")
    issuer: StrictStr = Field(description="Issuer identifies the party that issued this certificate.  ***Since:*** vSphere API 6.5 ")
    serial_number: StrictStr = Field(description="The unique serial number of the certificate given by issuer.  ***Since:*** vSphere API 6.5 ", alias="serialNumber")
    not_before: datetime = Field(description="The beginning time of the period of validity.  ***Since:*** vSphere API 6.5 ", alias="notBefore")
    not_after: datetime = Field(description="The ending time of the period of validity.  ***Since:*** vSphere API 6.5 ", alias="notAfter")
    fingerprint: StrictStr = Field(description="The SSL SHA1 fingerprint of the certificate.  ***Since:*** vSphere API 6.5 ")
    check_time: datetime = Field(description="The timestamp when the state of the certificate is checked.  ***Since:*** vSphere API 6.5 ", alias="checkTime")
    seconds_since_valid: Optional[StrictInt] = Field(default=None, description="Total seconds since this certificate has entered valid state.  It is the time difference between \"now\" and \"notBefore\". If it is negative value, that means the certificate will become valid in a future time.  ***Since:*** vSphere API 6.5 ", alias="secondsSinceValid")
    seconds_before_expire: Optional[StrictInt] = Field(default=None, description="Total seconds before this certificate expires.  It is the time difference between \"notAfter\" and \"now\". If it is negative value, that means the certificate has already expired.  ***Since:*** vSphere API 6.5 ", alias="secondsBeforeExpire")
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
        """Create an instance of CryptoManagerKmipCertificateInfo from a JSON string"""
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
        """Create an instance of CryptoManagerKmipCertificateInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

