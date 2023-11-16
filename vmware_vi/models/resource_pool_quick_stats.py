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

class ResourcePoolQuickStats(DataObject):
    """
    A set of statistics that are typically updated with near real-time regularity.  These statistics are aggregates of the corresponding statistics of all virtual machines in the given resource pool, and unless otherwise noted, only make sense when at least one virtual machine in the given resource pool is powered on. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    overall_cpu_usage: Optional[StrictInt] = Field(default=None, description="Basic CPU performance statistics, in MHz.  ***Since:*** vSphere API 4.0 ", alias="overallCpuUsage")
    overall_cpu_demand: Optional[StrictInt] = Field(default=None, description="Basic CPU performance statistics, in MHz.  ***Since:*** vSphere API 4.0 ", alias="overallCpuDemand")
    guest_memory_usage: Optional[StrictInt] = Field(default=None, description="Guest memory utilization statistics, in MB.  This is also known as active guest memory. The number can be between 0 and the configured memory size of a virtual machine.  ***Since:*** vSphere API 4.0 ", alias="guestMemoryUsage")
    host_memory_usage: Optional[StrictInt] = Field(default=None, description="Host memory utilization statistics, in MB.  This is also known as consummed host memory. This is between 0 and the configured resource limit. Valid while a virtual machine is running. This includes the overhead memory of a virtual machine.  ***Since:*** vSphere API 4.0 ", alias="hostMemoryUsage")
    distributed_cpu_entitlement: Optional[StrictInt] = Field(default=None, description="This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  ***Since:*** vSphere API 4.0 ", alias="distributedCpuEntitlement")
    distributed_memory_entitlement: Optional[StrictInt] = Field(default=None, description="This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  ***Since:*** vSphere API 4.0 ", alias="distributedMemoryEntitlement")
    static_cpu_entitlement: Optional[StrictInt] = Field(default=None, description="The static CPU resource entitlement for a virtual machine.  This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.  ***Since:*** vSphere API 4.0 ", alias="staticCpuEntitlement")
    static_memory_entitlement: Optional[StrictInt] = Field(default=None, description="The static memory resource entitlement for a virtual machine.  This value is calculated based on this virtual machine's resource reservations, shares and limit, and doesn't take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.  ***Since:*** vSphere API 4.0 ", alias="staticMemoryEntitlement")
    private_memory: Optional[StrictInt] = Field(default=None, description="The portion of memory, in MB, that is granted to a virtual machine from non-shared host memory.  ***Since:*** vSphere API 4.0 ", alias="privateMemory")
    shared_memory: Optional[StrictInt] = Field(default=None, description="The portion of memory, in MB, that is granted to a virtual machine from host memory that is shared between VMs.  ***Since:*** vSphere API 4.0 ", alias="sharedMemory")
    swapped_memory: Optional[StrictInt] = Field(default=None, description="The portion of memory, in MB, that is granted to a virtual machine from the host's swap space.  This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0 ", alias="swappedMemory")
    ballooned_memory: Optional[StrictInt] = Field(default=None, description="The size of the balloon driver in a virtual machine, in MB.  The host will inflate the balloon driver to reclaim physical memory from a virtual machine. This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0 ", alias="balloonedMemory")
    overhead_memory: Optional[StrictInt] = Field(default=None, description="The amount of memory resource (in MB) that will be used by a virtual machine above its guest memory requirements.  This value is set if and only if a virtual machine is registered on a host that supports memory resource allocation features. For powered off VMs, this is the minimum overhead required to power on the VM on the registered host. For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.  See also *HostSystem.QueryMemoryOverheadEx*.  ***Since:*** vSphere API 4.0 ", alias="overheadMemory")
    consumed_overhead_memory: Optional[StrictInt] = Field(default=None, description="The amount of overhead memory, in MB, currently being consumed to run a VM.  This value is limited by the overhead memory reservation for a VM, stored in *ResourcePoolQuickStats.overheadMemory*.  ***Since:*** vSphere API 4.0 ", alias="consumedOverheadMemory")
    compressed_memory: Optional[StrictInt] = Field(default=None, description="The amount of compressed memory currently consumed by VM, in KB.  ***Since:*** vSphere API 4.1 ", alias="compressedMemory")
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
        """Create an instance of ResourcePoolQuickStats from a JSON string"""
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
        """Create an instance of ResourcePoolQuickStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

