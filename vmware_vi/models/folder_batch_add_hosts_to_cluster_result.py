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

from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.folder_failed_host_result import FolderFailedHostResult
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FolderBatchAddHostsToClusterResult(DataObject):
    """
    FolderBatchAddHostsToClusterResult
    """ # noqa: E501
    hosts_added_to_cluster: Optional[List[ManagedObjectReference]] = Field(default=None, description="List of hosts that were successfully added to the cluster in the desired state.  ***Since:*** vSphere API 6.7.1  Refers instances of *HostSystem*. ", alias="hostsAddedToCluster")
    hosts_failed_inventory_add: Optional[List[FolderFailedHostResult]] = Field(default=None, description="Contains a fault for each host that failed addition to the inventory.  A failed host will not be part of hostsAddedToCluster list.  ***Since:*** vSphere API 6.7.1 ", alias="hostsFailedInventoryAdd")
    hosts_failed_move_to_cluster: Optional[List[FolderFailedHostResult]] = Field(default=None, description="List of hosts that are part of inventory but failed to move to the cluster in the desired state.  A failed host will not be part of hostsAddedToCluster list however, a failed host will be part of inventory as it might have been added as a standalone host but failed to move to cluster in the desired state.  ***Since:*** vSphere API 6.7.1 ", alias="hostsFailedMoveToCluster")
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
        """Create an instance of FolderBatchAddHostsToClusterResult from a JSON string"""
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
        """Create an instance of FolderBatchAddHostsToClusterResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


