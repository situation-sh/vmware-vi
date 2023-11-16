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
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.storage_drs_pod_selection_spec import StorageDrsPodSelectionSpec
from vmware_vi.models.virtual_machine_clone_spec import VirtualMachineCloneSpec
from vmware_vi.models.virtual_machine_config_spec import VirtualMachineConfigSpec
from vmware_vi.models.virtual_machine_move_priority_enum import VirtualMachineMovePriorityEnum
from vmware_vi.models.virtual_machine_relocate_spec import VirtualMachineRelocateSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StoragePlacementSpec(DataObject):
    """
    StoragePlacementSpec encapsulates all of the inputs passed to the *StorageResourceManager.RecommendDatastores* method.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    type: StrictStr = Field(description="The storage placement type.  The set of possible values is described in *StoragePlacementSpecPlacementType_enum*  ***Since:*** vSphere API 5.0 ")
    priority: Optional[VirtualMachineMovePriorityEnum] = None
    vm: Optional[ManagedObjectReference] = None
    pod_selection_spec: StorageDrsPodSelectionSpec = Field(alias="podSelectionSpec")
    clone_spec: Optional[VirtualMachineCloneSpec] = Field(default=None, alias="cloneSpec")
    clone_name: Optional[StrictStr] = Field(default=None, description="Name for cloned virtual machine.  ***Since:*** vSphere API 5.0 ", alias="cloneName")
    config_spec: Optional[VirtualMachineConfigSpec] = Field(default=None, alias="configSpec")
    relocate_spec: Optional[VirtualMachineRelocateSpec] = Field(default=None, alias="relocateSpec")
    resource_pool: Optional[ManagedObjectReference] = Field(default=None, alias="resourcePool")
    host: Optional[ManagedObjectReference] = None
    folder: Optional[ManagedObjectReference] = None
    disallow_prerequisite_moves: Optional[StrictBool] = Field(default=None, description="Specification for whether to disable pre-requisite storage vmotions for storage placements.  If unset, default behavior is to allow such prerequisite moves.  ***Since:*** vSphere API 5.1 ", alias="disallowPrerequisiteMoves")
    resource_lease_duration_sec: Optional[StrictInt] = Field(default=None, description="Resource lease duration in seconds.  If the duration is within bounds, Storage DRS will hold onto resources needed for applying recommendations generated as part of that call. Only initial placement recommendations generated by storage DRS can reserve resources this way.  ***Since:*** vSphere API 5.1 ", alias="resourceLeaseDurationSec")
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
        """Create an instance of StoragePlacementSpec from a JSON string"""
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
        """Create an instance of StoragePlacementSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


