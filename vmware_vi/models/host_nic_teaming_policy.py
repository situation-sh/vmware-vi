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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_nic_failure_criteria import HostNicFailureCriteria
from vmware_vi.models.host_nic_order_policy import HostNicOrderPolicy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNicTeamingPolicy(DataObject):
    """
    Policy for a network adapter team. 
    """ # noqa: E501
    policy: Optional[StrictStr] = Field(default=None, description="Network adapter teaming policy includes failover and load balancing, It can be one of the following: - **loadbalance\\_ip**: route based on ip hash. - **loadbalance\\_srcmac**: route based on source MAC hash. - **loadbalance\\_srcid**: route based on the source of the port ID. - **failover\\_explicit**: use explicit failover order.    See also *HostNetCapabilities.nicTeamingPolicy*. ")
    reverse_policy: Optional[StrictBool] = Field(default=None, description="Deprecated as of VI API 5.1, the system default (true) will be used.  The flag to indicate whether or not the teaming policy is applied to inbound frames as well.  For example, if the policy is explicit failover, a broadcast request goes through uplink1 and comes back through uplink2. Then if the reverse policy is set, the frame is dropped when it is received from uplink2. This reverse policy is useful to prevent the virtual machine from getting reflections. ", alias="reversePolicy")
    notify_switches: Optional[StrictBool] = Field(default=None, description="Flag to specify whether or not to notify the physical switch if a link fails.  If this property is true, ESX Server will respond to the failure by sending a RARP packet from a different physical adapter, causing the switch to update its cache. ", alias="notifySwitches")
    rolling_order: Optional[StrictBool] = Field(default=None, description="The flag to indicate whether or not to use a rolling policy when restoring links.  For example, assume the explicit link order is (vmnic9, vmnic0), therefore vmnic9 goes down, vmnic0 comes up. However, when vmnic9 comes backup, if rollingOrder is set to be true, vmnic0 continues to be used, otherwise, vmnic9 is restored as specified in the explicitly order. ", alias="rollingOrder")
    failure_criteria: Optional[HostNicFailureCriteria] = Field(default=None, alias="failureCriteria")
    nic_order: Optional[HostNicOrderPolicy] = Field(default=None, alias="nicOrder")
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
        """Create an instance of HostNicTeamingPolicy from a JSON string"""
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
        """Create an instance of HostNicTeamingPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

