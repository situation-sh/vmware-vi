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
from vmware_vi.models.cluster_compute_resource_host_configuration_input import ClusterComputeResourceHostConfigurationInput
from vmware_vi.models.sddc_base import SDDCBase
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExtendHCIRequestType(BaseModel):
    """
    The parameters of *ClusterComputeResource.ExtendHCI_Task*. 
    """ # noqa: E501
    host_inputs: Optional[List[ClusterComputeResourceHostConfigurationInput]] = Field(default=None, description="Inputs to configure specified set of hosts in the cluster. See *ClusterComputeResourceHostConfigurationInput* for details. Hosts in this list should be part of the cluster and should be in maintenance mode for them to be configured per specification. Hosts which were not configured due to not being in maintenance mode will be returned in *ClusterComputeResourceClusterConfigResult.failedHosts*. Specify *ClusterComputeResourceHostConfigurationInput.hostVmkNics* only if *dvsSetting* is set.  ***Since:*** vSphere API 6.7.1 ", alias="hostInputs")
    v_san_config_spec: Optional[SDDCBase] = Field(default=None, alias="vSanConfigSpec")
    __properties: ClassVar[List[str]] = ["hostInputs", "vSanConfigSpec"]

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
        """Create an instance of ExtendHCIRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in host_inputs (list)
        _items = []
        if self.host_inputs:
            for _item in self.host_inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostInputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of v_san_config_spec
        if self.v_san_config_spec:
            _dict['vSanConfigSpec'] = self.v_san_config_spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExtendHCIRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostInputs": [ClusterComputeResourceHostConfigurationInput.from_dict(_item) for _item in obj.get("hostInputs")] if obj.get("hostInputs") is not None else None,
            "vSanConfigSpec": SDDCBase.from_dict(obj.get("vSanConfigSpec")) if obj.get("vSanConfigSpec") is not None else None
        })
        return _obj


