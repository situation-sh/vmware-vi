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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DatastoreInfo(DataObject):
    """
    Detailed information about a datastore.  This is a base type for derived types that have more specific details about a datastore.  See also *HostVmfsVolume*, *HostNasVolume*, *HostLocalFileSystemVolume*. 
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the datastore. ")
    url: StrictStr = Field(description="The unique locator for the datastore. ")
    free_space: StrictInt = Field(description="Free space of this datastore, in bytes.  The server periodically updates this value. It can be explicitly refreshed with the Refresh operation. ", alias="freeSpace")
    max_file_size: StrictInt = Field(description="The maximum size of a file that can reside on this file system volume. ", alias="maxFileSize")
    max_virtual_disk_capacity: Optional[StrictInt] = Field(default=None, description="The maximum capacity of a virtual disk which can be created on this volume.  ***Since:*** vSphere API 5.5 ", alias="maxVirtualDiskCapacity")
    max_memory_file_size: StrictInt = Field(description="The maximum size of a snapshot or a swap file that can reside on this file system volume.  ***Since:*** vSphere API 6.0 ", alias="maxMemoryFileSize")
    timestamp: Optional[datetime] = Field(default=None, description="Time when the free-space and capacity values in *DatastoreInfo* and *DatastoreSummary* were updated.  ***Since:*** vSphere API 4.0 ")
    container_id: Optional[StrictStr] = Field(default=None, description="The unique container ID of the datastore, if applicable.  ***Since:*** vSphere API 5.5 ", alias="containerId")
    alias_of: Optional[StrictStr] = Field(default=None, description="vSAN datastore container that this datastore is alias of.  If this field is unset then this datastore is not alias of any other vSAN datastore. See *DatastoreInfo.containerId*.  ***Since:*** vSphere API 6.7.1 ", alias="aliasOf")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','LocalDatastoreInfo': 'LocalDatastoreInfo','NasDatastoreInfo': 'NasDatastoreInfo','PMemDatastoreInfo': 'PMemDatastoreInfo','VmfsDatastoreInfo': 'VmfsDatastoreInfo','VsanDatastoreInfo': 'VsanDatastoreInfo','VvolDatastoreInfo': 'VvolDatastoreInfo'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self]:
        """Create an instance of DatastoreInfo from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self]:
        """Create an instance of DatastoreInfo from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("DatastoreInfo failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.local_datastore_info import LocalDatastoreInfo
from vmware_vi.models.nas_datastore_info import NasDatastoreInfo
from vmware_vi.models.p_mem_datastore_info import PMemDatastoreInfo
from vmware_vi.models.primitive_binary import PrimitiveBinary
from vmware_vi.models.primitive_boolean import PrimitiveBoolean
from vmware_vi.models.primitive_byte import PrimitiveByte
from vmware_vi.models.primitive_date_time import PrimitiveDateTime
from vmware_vi.models.primitive_double import PrimitiveDouble
from vmware_vi.models.primitive_float import PrimitiveFloat
from vmware_vi.models.primitive_int import PrimitiveInt
from vmware_vi.models.primitive_long import PrimitiveLong
from vmware_vi.models.primitive_method_name import PrimitiveMethodName
from vmware_vi.models.primitive_prop_path import PrimitivePropPath
from vmware_vi.models.primitive_short import PrimitiveShort
from vmware_vi.models.primitive_string import PrimitiveString
from vmware_vi.models.primitive_type_name import PrimitiveTypeName
from vmware_vi.models.primitive_uri import PrimitiveURI
from vmware_vi.models.vmfs_datastore_info import VmfsDatastoreInfo
from vmware_vi.models.vsan_datastore_info import VsanDatastoreInfo
from vmware_vi.models.vvol_datastore_info import VvolDatastoreInfo
# TODO: Rewrite to not use raise_errors
DatastoreInfo.model_rebuild(raise_errors=False)

