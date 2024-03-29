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
from pydantic import BaseModel
from pydantic import Field
from vmware_vi.models.distributed_virtual_switch_manager_dvs_product_spec import DistributedVirtualSwitchManagerDvsProductSpec
from vmware_vi.models.distributed_virtual_switch_manager_host_container import DistributedVirtualSwitchManagerHostContainer
from vmware_vi.models.distributed_virtual_switch_manager_host_dvs_filter_spec import DistributedVirtualSwitchManagerHostDvsFilterSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryDvsCheckCompatibilityRequestType(BaseModel):
    """
    The parameters of *DistributedVirtualSwitchManager.QueryDvsCheckCompatibility*. 
    """ # noqa: E501
    host_container: DistributedVirtualSwitchManagerHostContainer = Field(alias="hostContainer")
    dvs_product_spec: Optional[DistributedVirtualSwitchManagerDvsProductSpec] = Field(default=None, alias="dvsProductSpec")
    host_filter_spec: Optional[List[DistributedVirtualSwitchManagerHostDvsFilterSpec]] = Field(default=None, description="The hosts against which to check compatibility. This is a filterSpec and users can use this to specify all hosts in a container (datacenter, folder, or computeResource), an array of hosts, or hosts that might or might not be a DVS member.  ***Since:*** vSphere API 4.1 ", alias="hostFilterSpec")
    __properties: ClassVar[List[str]] = ["hostContainer", "dvsProductSpec", "hostFilterSpec"]

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
        """Create an instance of QueryDvsCheckCompatibilityRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of host_container
        if self.host_container:
            _dict['hostContainer'] = self.host_container.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dvs_product_spec
        if self.dvs_product_spec:
            _dict['dvsProductSpec'] = self.dvs_product_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in host_filter_spec (list)
        _items = []
        if self.host_filter_spec:
            for _item in self.host_filter_spec:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostFilterSpec'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QueryDvsCheckCompatibilityRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostContainer": DistributedVirtualSwitchManagerHostContainer.from_dict(obj.get("hostContainer")) if obj.get("hostContainer") is not None else None,
            "dvsProductSpec": DistributedVirtualSwitchManagerDvsProductSpec.from_dict(obj.get("dvsProductSpec")) if obj.get("dvsProductSpec") is not None else None,
            "hostFilterSpec": [DistributedVirtualSwitchManagerHostDvsFilterSpec.from_dict(_item) for _item in obj.get("hostFilterSpec")] if obj.get("hostFilterSpec") is not None else None
        })
        return _obj


