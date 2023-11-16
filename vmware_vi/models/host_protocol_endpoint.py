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
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostProtocolEndpoint(DataObject):
    """
    ProtocolEndpoint is configured LUN or NFS directory This is used for io path to actual virtual disks (VVols)  ***Since:*** vSphere API 6.0 
    """ # noqa: E501
    pe_type: StrictStr = Field(description="Deprecated from all vmodl version above @released(\"6.0\") Use type instead.  Type of ProtocolEndpoint See *HostProtocolEndpointPEType_enum*  ***Since:*** vSphere API 6.0 ", alias="peType")
    type: Optional[StrictStr] = Field(default=None, description="Type of ProtocolEndpoint See *HostProtocolEndpointProtocolEndpointType_enum*  ***Since:*** vSphere API 6.5 ")
    uuid: StrictStr = Field(description="Identifier for PE assigned by VASA Provider  ***Since:*** vSphere API 6.0 ")
    host_key: Optional[List[ManagedObjectReference]] = Field(default=None, description="Set of ESX hosts which can see the same PE  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*. ", alias="hostKey")
    storage_array: Optional[StrictStr] = Field(default=None, description="Associated Storage Array  ***Since:*** vSphere API 6.0 ", alias="storageArray")
    nfs_server: Optional[StrictStr] = Field(default=None, description="NFSv3 and NFSv4x PE will contain information about NFS Server For NFSv4x this field may contain comma separated list of IP addresses which are associated with the NFS Server  ***Since:*** vSphere API 6.0 ", alias="nfsServer")
    nfs_dir: Optional[StrictStr] = Field(default=None, description="NFSv3 and NFSv4x PE will contain information about NFS directory  ***Since:*** vSphere API 6.0 ", alias="nfsDir")
    nfs_server_scope: Optional[StrictStr] = Field(default=None, description="NFSv4x PE will contain information about NFSv4x Server Scope  ***Since:*** vSphere API 6.5 ", alias="nfsServerScope")
    nfs_server_major: Optional[StrictStr] = Field(default=None, description="NFSv4x PE will contain information about NFSv4x Server Major  ***Since:*** vSphere API 6.5 ", alias="nfsServerMajor")
    nfs_server_auth_type: Optional[StrictStr] = Field(default=None, description="NFSv4x PE will contain information about NFSv4x Server Auth-type  ***Since:*** vSphere API 6.5 ", alias="nfsServerAuthType")
    nfs_server_user: Optional[StrictStr] = Field(default=None, description="NFSv4x PE will contain information about NFSv4x Server User  ***Since:*** vSphere API 6.5 ", alias="nfsServerUser")
    device_id: Optional[StrictStr] = Field(default=None, description="SCSI PE will contain information about SCSI device ID  ***Since:*** vSphere API 6.0 ", alias="deviceId")
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
        """Create an instance of HostProtocolEndpoint from a JSON string"""
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
        """Create an instance of HostProtocolEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

