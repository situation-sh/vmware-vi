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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.host_nvme_transport_parameters import HostNvmeTransportParameters
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNvmeOverTcpParameters(HostNvmeTransportParameters):
    """
    This data object represents the transport specific parameters necessary to establish an NVME over TCP connection.  ***Since:*** vSphere API 7.0.3.0 
    """ # noqa: E501
    address: StrictStr = Field(description="The address of the connection target.  It is expected to be an IPv4 or IPv6 address.  ***Since:*** vSphere API 7.0.3.0 ")
    port_number: Optional[StrictInt] = Field(default=None, description="The port number of the TCP target port.  If this field is unset, the default value of 8009 is assumed as per the IANA assignment: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml  ***Since:*** vSphere API 7.0.3.0 ", alias="portNumber")
    digest_verification: Optional[StrictStr] = Field(default=None, description="Digest verification parameter.  When used in a discovery or connect spec, this parameter specifies the requested digest verification setting. The list of supported values is described in *HostDigestVerificationSetting_enum*. If unset, a default value of disabled is assumed. For details, see: - NVM Express Technical Proposal 8000 - NVMe/TCP Transport,   Section 7.4.10.2, \"Initialize Connection Request PDU (ICReq)\" - DGST field.    When part of *HostNvmeDiscoveryLogEntry*, this value is unset.  ***Since:*** vSphere API 7.0.3.0 ", alias="digestVerification")
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
        """Create an instance of HostNvmeOverTcpParameters from a JSON string"""
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
        """Create an instance of HostNvmeOverTcpParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


