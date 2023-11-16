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
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterUsageSummary(DataObject):
    """
    This class contains cluster usage summary that is populated by DRS and used by Cloud Placement Engine in VCD.  ***Since:*** vSphere API 6.0 
    """ # noqa: E501
    total_cpu_capacity_mhz: StrictInt = Field(description="Total CPU capacity of the cluster.  ***Since:*** vSphere API 6.0 ", alias="totalCpuCapacityMhz")
    total_mem_capacity_mb: StrictInt = Field(description="Total memory capacity of the cluster.  ***Since:*** vSphere API 6.0 ", alias="totalMemCapacityMB")
    cpu_reservation_mhz: StrictInt = Field(description="Sum of CPU reservation of all the Resource Pools and powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="cpuReservationMhz")
    mem_reservation_mb: StrictInt = Field(description="Sum of memory reservation of all the Resource Pools and powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="memReservationMB")
    powered_off_cpu_reservation_mhz: Optional[StrictInt] = Field(default=None, description="Sum of CPU reservation of all the powered-off VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="poweredOffCpuReservationMhz")
    powered_off_mem_reservation_mb: Optional[StrictInt] = Field(default=None, description="Sum of memory reservation of all the powered-off VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="poweredOffMemReservationMB")
    cpu_demand_mhz: StrictInt = Field(description="Sum of CPU demand of all the powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="cpuDemandMhz")
    mem_demand_mb: StrictInt = Field(description="Sum of memory demand of all the powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0 ", alias="memDemandMB")
    stats_gen_number: StrictInt = Field(description="Generation number of the usage stats.  Updated during every DRS load balancing call.  ***Since:*** vSphere API 6.0 ", alias="statsGenNumber")
    cpu_entitled_mhz: StrictInt = Field(description="This is the current CPU entitlement across the cluster  ***Since:*** vSphere API 6.0 ", alias="cpuEntitledMhz")
    mem_entitled_mb: StrictInt = Field(description="This is the current memory entitlement across the cluster  ***Since:*** vSphere API 6.0 ", alias="memEntitledMB")
    powered_off_vm_count: StrictInt = Field(description="The number of powered off VMs in the cluster  ***Since:*** vSphere API 6.0 ", alias="poweredOffVmCount")
    total_vm_count: StrictInt = Field(description="The number of VMs in the cluster  ***Since:*** vSphere API 6.0 ", alias="totalVmCount")
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
        """Create an instance of ClusterUsageSummary from a JSON string"""
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
        """Create an instance of ClusterUsageSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


