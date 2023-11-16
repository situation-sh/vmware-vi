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
from pydantic import StrictBool, StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVSNetworkResourceManagementCapability(DataObject):
    """
    Dataobject representing the feature capabilities of network resource management supported by the vSphere Distributed Switch.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    network_resource_management_supported: StrictBool = Field(description="Indicates whether network I/O control is supported on the vSphere Distributed Switch.  Network I/O control is supported in vSphere Distributed Switch Version 4.1 or later.  ***Since:*** vSphere API 5.0 ", alias="networkResourceManagementSupported")
    network_resource_pool_high_share_value: StrictInt = Field(description="High share level (*SharesLevel_enum*.*high*) for *DVSNetworkResourcePoolAllocationInfo*.*DVSNetworkResourcePoolAllocationInfo.shares*.  The <code>networkResourcePoolHighshareValue</code> property implicitly defines the legal range of share values to be between 1 and this value. This property also defines values for other level types, such as *normal* being one half of this value and *low* being one fourth of this value. This feature is supported in vSphere Distributed Switch Version 4.1 or later.  ***Since:*** vSphere API 5.0 ", alias="networkResourcePoolHighShareValue")
    qos_supported: StrictBool = Field(description="Indicates whether Qos Tag(802.1p priority tag)is supported on the vSphere Distributed Switch.  Qos Tag is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0 ", alias="qosSupported")
    user_defined_network_resource_pools_supported: StrictBool = Field(description="Indicates whether the switch supports creating user defined resource pools.  This feature is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0 ", alias="userDefinedNetworkResourcePoolsSupported")
    network_resource_control_version3_supported: Optional[StrictBool] = Field(default=None, description="Flag to indicate whether Network Resource Control version 3 is supported.  The API supported by Network Resouce Control version 3 include: 1. VM virtual NIC network resource specification    *VirtualEthernetCardResourceAllocation* 2. VM virtual NIC network resource pool specification    *DVSVmVnicNetworkResourcePool* 3. Host infrastructure traffic network resource specification    *DvsHostInfrastructureTrafficResource*     Network Resource Control version 3 is supported for Switch Version 6.0 or later.  ***Since:*** vSphere API 6.0 ", alias="networkResourceControlVersion3Supported")
    user_defined_infra_traffic_pool_supported: Optional[StrictBool] = Field(default=None, description="Indicates whether user defined infrastructure traffic pool supported in vSphere Distributed Switch.  ***Since:*** vSphere API 6.7 ", alias="userDefinedInfraTrafficPoolSupported")
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
        """Create an instance of DVSNetworkResourceManagementCapability from a JSON string"""
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
        """Create an instance of DVSNetworkResourceManagementCapability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

