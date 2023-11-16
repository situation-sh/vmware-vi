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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.crypto_spec import CryptoSpec
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.service_locator import ServiceLocator
from vmware_vi.models.virtual_device_config_spec import VirtualDeviceConfigSpec
from vmware_vi.models.virtual_machine_profile_spec import VirtualMachineProfileSpec
from vmware_vi.models.virtual_machine_relocate_spec_disk_locator import VirtualMachineRelocateSpecDiskLocator
from vmware_vi.models.virtual_machine_relocate_transformation_enum import VirtualMachineRelocateTransformationEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineRelocateSpec(DataObject):
    """
    Specification for moving or copying a virtual machine to a different datastore or host. 
    """ # noqa: E501
    service: Optional[ServiceLocator] = None
    folder: Optional[ManagedObjectReference] = None
    datastore: Optional[ManagedObjectReference] = None
    disk_move_type: Optional[StrictStr] = Field(default=None, description="Manner in which to move the virtual disk to the *target datastore*.  The set of possible values is described in *VirtualMachineRelocateDiskMoveOptions_enum*.  This property applies to all the disks which the virtual machine has, but can be overridden on a per-disk basis using *VirtualMachineRelocateSpecDiskLocator.diskMoveType* prior to vSphere API 6.0 or using *VirtualDiskConfigSpec.diskMoveType* in vSphere API 6.0 and later.  This property can only be set if *HostCapability.deltaDiskBackingsSupported* is true.  If left unset then *moveAllDiskBackingsAndDisallowSharing* is assumed.  ***Since:*** vSphere API 4.0 ", alias="diskMoveType")
    pool: Optional[ManagedObjectReference] = None
    host: Optional[ManagedObjectReference] = None
    disk: Optional[List[VirtualMachineRelocateSpecDiskLocator]] = Field(default=None, description="An optional list that allows specifying the datastore location for each virtual disk. ")
    transform: Optional[VirtualMachineRelocateTransformationEnum] = None
    device_change: Optional[List[VirtualDeviceConfigSpec]] = Field(default=None, description="An optional list of virtual device specs that allow specifying the new device locations for the relocate operation.  The supported device changes are: - For *VirtualEthernetCard*, it has to be used   in *VirtualDeviceConfigSpec.device* to specify the   target network backing. - For *VirtualDisk*, it can be used to specify   vFlash cache configuration, or the storage profile for destination   disks. The storage profiles are used to either upgrade the virtual   disk's storage to a persistent memory, or keep the virtual disk   in persistent memory when moving the virtual machine's overall   storage. - All other specification are ignored.    ***Since:*** vSphere API 5.5 ", alias="deviceChange")
    profile: Optional[List[VirtualMachineProfileSpec]] = Field(default=None, description="Storage profile requirement for Virtual Machine's home directory.  Profiles are solution specific. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5 ")
    crypto_spec: Optional[CryptoSpec] = Field(default=None, alias="cryptoSpec")
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
        """Create an instance of VirtualMachineRelocateSpec from a JSON string"""
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
        """Create an instance of VirtualMachineRelocateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


