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
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.ip_pool_association import IpPoolAssociation
from vmware_vi.models.ip_pool_ip_pool_config_info import IpPoolIpPoolConfigInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IpPool(DataObject):
    """
    Specifications of the network configuration to be used on a network.  This is used to generate IP addresses and for self-customization of vApps.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique ID, generated by the server.  This is used to identify the pool in subsequent lookups or updates. The generated value is also returned by the *IpPoolManager.CreateIpPool* method.  ***Since:*** vSphere API 4.0 ")
    name: Optional[StrictStr] = Field(default=None, description="Pool name.  The pool name must be unique within the datacenter.  Any / (slash), \\\\ (backslash), character used in this name element is escaped. Similarly, any % (percent) character used in this name element is escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.  ***Since:*** vSphere API 4.0 ")
    ipv4_config: Optional[IpPoolIpPoolConfigInfo] = Field(default=None, alias="ipv4Config")
    ipv6_config: Optional[IpPoolIpPoolConfigInfo] = Field(default=None, alias="ipv6Config")
    dns_domain: Optional[StrictStr] = Field(default=None, description="DNS Domain.  For example, vmware.com. This can be an empty string if no domain is configured.  ***Since:*** vSphere API 4.0 ", alias="dnsDomain")
    dns_search_path: Optional[StrictStr] = Field(default=None, description="DNS Search Path.  For example, eng.vmware.com;vmware.com  ***Since:*** vSphere API 4.0 ", alias="dnsSearchPath")
    host_prefix: Optional[StrictStr] = Field(default=None, description="Prefix for hostnames.  ***Since:*** vSphere API 4.0 ", alias="hostPrefix")
    http_proxy: Optional[StrictStr] = Field(default=None, description="The HTTP proxy to use on this network, e.g., &lt;host&gt;:&lt;port&gt;  ***Since:*** vSphere API 4.0 ", alias="httpProxy")
    network_association: Optional[List[IpPoolAssociation]] = Field(default=None, description="The networks that are associated with this IP pool  ***Since:*** vSphere API 4.0 ", alias="networkAssociation")
    available_ipv4_addresses: Optional[StrictInt] = Field(default=None, description="The number of IPv4 addresses available for allocation.  ***Since:*** vSphere API 5.1 ", alias="availableIpv4Addresses")
    available_ipv6_addresses: Optional[StrictInt] = Field(default=None, description="The number of IPv6 addresses available for allocation.  ***Since:*** vSphere API 5.1 ", alias="availableIpv6Addresses")
    allocated_ipv4_addresses: Optional[StrictInt] = Field(default=None, description="The number of allocated IPv4 addresses.  ***Since:*** vSphere API 5.1 ", alias="allocatedIpv4Addresses")
    allocated_ipv6_addresses: Optional[StrictInt] = Field(default=None, description="The number of allocated IPv6 addresses.  ***Since:*** vSphere API 5.1 ", alias="allocatedIpv6Addresses")
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
        """Create an instance of IpPool from a JSON string"""
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
        """Create an instance of IpPool from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

