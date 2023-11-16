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
from pydantic import SecretStr, StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNasVolumeSpec(DataObject):
    """
    Specification for creating NAS volume.  When mounting a NAS volume on multiple hosts, the same remoteHost and remotePath values should be used on every host, otherwise it will be treated as different datastores. For example, if one host references the remotePath of a NAS volume as \"/mnt/mount1\" and another references it as \"/mnt/mount1/\", it will not be recognized as the same datastore. 
    """ # noqa: E501
    remote_host: StrictStr = Field(description="The host that runs the NFS v3 or CIFS server.  For NFS v4.1 and beyond use remoteHostNames defined later. The field remotehost may be deprecated in future for NFS, so clients should plan to use the property remoteHostNames to send in the host name(s) for both NFS v3 and v4.1 ", alias="remoteHost")
    remote_path: StrictStr = Field(description="The remote path of the NFS mount point. ", alias="remotePath")
    local_path: StrictStr = Field(description="The localPath refers to the name of the NAS datastore to be created using this specification.  In the case of ESX Server, the datastore name is a component in the file system path at which the NAS volume can be found. For example, if localPath is set to \"nas\\_volume\" the created NAS datastore will be named \"nas\\_volume\" and it can be accessed via the file system path \"/vmfs/volumes/nas\\_volume\".  In the case of VMware Server, the localPath will also be used as the datastore name, but the datastore name may not necessarily be reflected in the file system path where the NAS volume may be accessed. ", alias="localPath")
    access_mode: StrictStr = Field(description="Access mode for the mount point.  Mounting in read-write mode would be successful irregardless on how the mount point is exported or access permissions. For example, mounting a volume that is exported as read-only as readWrite will succeed. Hence, that a readWrite mount succeeds should not be taken as an indication that all files on a mount is writable.  If a file system is mounted readOnly, the system cannot create or modify any files on the file system. This is mostly useful for storing ISO images and templates, since a virtual machine cannot be powered on from a readOnly volume.  The access mode of a mounted NFS volume can be obtained at *HostMountInfo.accessMode*.  See also *HostMountMode_enum*. ", alias="accessMode")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the the NAS volume.  Supported types are *CIFS*, *NFS*, *NFS41* If not specified, defaults to *NFS*  ***Since:*** VI API 2.5 ")
    user_name: Optional[StrictStr] = Field(default=None, description="If type is CIFS, the user name to use when connecting to the CIFS server.  If type is NFS, this field will be ignored.  ***Since:*** VI API 2.5 ", alias="userName")
    password: Optional[SecretStr] = Field(default=None, description="If type is CIFS, the password to use when connecting to the CIFS server.  If type is NFS, this field will be ignored.  ***Since:*** VI API 2.5 ")
    remote_host_names: Optional[List[StrictStr]] = Field(default=None, description="Hostnames or IP addresses of remote NFS server.  In case of NFS v4.1 this may have multiple entries. For NFS v3 the input should be same in both remoteHost and remoteHostNames. In case of NFS v4.1, if vmknic binding is enabled, then input can be in format {hostip1:vmknic1, hostip2:vmknic2}.  ***Since:*** vSphere API 6.0 ", alias="remoteHostNames")
    security_type: Optional[StrictStr] = Field(default=None, description="Provided during mount indicating what security type, if any, to use See *HostNasVolumeSecurityType_enum*  ***Since:*** vSphere API 6.0 ", alias="securityType")
    vmknic_to_bind: Optional[StrictStr] = Field(default=None, description="Name of the vmknic to be used by this mount.  This field will be updated by a client with vmknic that will be used for NAS volume mount operation for vmknic binding for NFSv3 ", alias="vmknicToBind")
    vmknic_bound: Optional[StrictBool] = Field(default=None, description="Indicates whether a client wants to bind this mount to vmknic.  This field will be set to true by a client if vmknic should bind during NAS volume mount operation for NFSv3 else it will be set to false ", alias="vmknicBound")
    connections: Optional[StrictInt] = Field(default=None, description="Indicates the number of TCP connections for the particular NFSv3 Server during NAS volume mount operation.  If unset or set to 0, it defaults to one connection ")
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
        """Create an instance of HostNasVolumeSpec from a JSON string"""
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
        """Create an instance of HostNasVolumeSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

