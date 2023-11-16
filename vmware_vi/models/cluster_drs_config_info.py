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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.drs_behavior_enum import DrsBehaviorEnum
from vmware_vi.models.option_value import OptionValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterDrsConfigInfo(DataObject):
    """
    The *ClusterDrsConfigInfo* data object contains configuration information for the VMware DRS service.  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied. 
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=None, description="Deprecated as of vSphere API 7.0. To disable DRS load balancing, please use the lowest DRS aggressiveness level, setting *ClusterDrsConfigInfo.vmotionRate* to 5, and/or setting *ClusterDrsConfigInfo.defaultVmBehavior* to manual. The former only generates manadatory move recommendations, not load balancing recommendations. The latter only generates recommendations, without executing them. To remove all the child resource pools, please find the root resource pool *ComputeResource.resourcePool*, and destroy all its children *ResourcePool.DestroyChildren*. Vice versa.  Flag indicating whether or not DRS service is enabled. ")
    enable_vm_behavior_overrides: Optional[StrictBool] = Field(default=None, description="Flag that dictates whether DRS Behavior overrides for individual virtual machines (*ClusterDrsVmConfigInfo*) are enabled.  The default value is <code>true</code>.  When this flag is <code>true</code>, the *ClusterConfigSpecEx*.*ClusterConfigSpecEx.drsVmConfigSpec* values override the *ClusterDrsConfigInfo.defaultVmBehavior*.  When this flag is <code>false</code>, the *ClusterDrsConfigInfo.defaultVmBehavior* value applies to all virtual machines, with the following exception: in a cluster that has EVC disabled, you cannot override the virtual machine setting (*ClusterConfigSpecEx.drsVmConfigSpec*) for Fault Tolerance virtual machines.  ***Since:*** vSphere API 4.0 ", alias="enableVmBehaviorOverrides")
    default_vm_behavior: Optional[DrsBehaviorEnum] = Field(default=None, alias="defaultVmBehavior")
    vmotion_rate: Optional[StrictInt] = Field(default=None, description="Threshold for generated *ClusterRecommendation*s.  DRS generates only those recommendations that are above the specified vmotionRate. Ratings vary from 1 to 5. This setting applies to manual, partiallyAutomated, and fullyAutomated DRS clusters. See *DrsBehavior_enum*. ", alias="vmotionRate")
    scale_descendants_shares: Optional[StrictStr] = Field(default=None, description="Specifies the scaling behavior of the shares of all resource pools in the cluster.  See *ResourceConfigSpecScaleSharesBehavior_enum* for possible values. If any scaling behavior other than *disabled* is specified, the system will scale the CPU and memory shares allocated to each resource pool with the total shares of all powered on virtual machines under each respective pool. The system will also use the *SharesInfo* set on each resource pool as a multiplier for the scale. Setting the *ClusterDrsConfigInfo.scaleDescendantsShares* on the cluster is equivalent to setting the *ResourceConfigSpec.scaleDescendantsShares* on the root resource pool.  ***Since:*** vSphere API 7.0 ", alias="scaleDescendantsShares")
    option: Optional[List[OptionValue]] = Field(default=None, description="Advanced settings. ")
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
        """Create an instance of ClusterDrsConfigInfo from a JSON string"""
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
        """Create an instance of ClusterDrsConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


