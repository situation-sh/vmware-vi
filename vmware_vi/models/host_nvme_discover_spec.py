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
from pydantic import StrictBool
from pydantic import Field
from vmware_vi.models.host_nvme_spec import HostNvmeSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNvmeDiscoverSpec(HostNvmeSpec):
    """
    Specifies the parameters necessary to connect to a Discovery Service and retrieve a Discovery Log Page.  Here the transportParameters are used to establish a transport level connection to a Discovery Controller. Further details can be found here: - \"NVM Express over Fabrics 1.0\", Section 5, \"Discovery service\"    ***Since:*** vSphere API 7.0 
    """ # noqa: E501
    auto_connect: Optional[StrictBool] = Field(default=None, description="Indicates whether the specified adapter should automatically be connected to all the discovered controllers.  It is possible to automatically connect to all discovered controllers. This will only be attempted if this flag is set to true. Whether the connection attempt for an entry succeeded can then be determined via the corresponding *HostNvmeDiscoveryLogEntry.connected* field.  ***Since:*** vSphere API 7.0 ", alias="autoConnect")
    root_discovery_controller: Optional[StrictBool] = Field(default=None, description="If set to true, this flag indicates we are connecting to a root/central discovery controller (RDC/CDC).  This will create a persistent connection between the host and the root discovery controller, thus enabling some advanced features.  ***Since:*** vSphere API 7.0.3.0 ", alias="rootDiscoveryController")
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
        """Create an instance of HostNvmeDiscoverSpec from a JSON string"""
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
        """Create an instance of HostNvmeDiscoverSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


