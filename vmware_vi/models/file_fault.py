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


from typing import Any, ClassVar, Dict, List, Union
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.vim_fault import VimFault
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FileFault(VimFault):
    """
    The common base type for all file-related exceptions. 
    """ # noqa: E501
    file: StrictStr = Field(description="The file in question. ")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','CannotAccessFile': 'CannotAccessFile','CannotCreateFile': 'CannotCreateFile','CannotDeleteFile': 'CannotDeleteFile','DirectoryNotEmpty': 'DirectoryNotEmpty','FileAlreadyExists': 'FileAlreadyExists','FileLocked': 'FileLocked','FileNameTooLong': 'FileNameTooLong','FileNotFound': 'FileNotFound','FileNotWritable': 'FileNotWritable','FileTooLarge': 'FileTooLarge','IncorrectFileType': 'IncorrectFileType','NetworkCopyFault': 'NetworkCopyFault','NoDiskSpace': 'NoDiskSpace','NotADirectory': 'NotADirectory','NotAFile': 'NotAFile','TooManyConcurrentNativeClones': 'TooManyConcurrentNativeClones','TooManyNativeCloneLevels': 'TooManyNativeCloneLevels','TooManyNativeClonesOnFile': 'TooManyNativeClonesOnFile'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of FileFault from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of FileFault from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("FileFault failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.cannot_access_file import CannotAccessFile
from vmware_vi.models.cannot_create_file import CannotCreateFile
from vmware_vi.models.cannot_delete_file import CannotDeleteFile
from vmware_vi.models.directory_not_empty import DirectoryNotEmpty
from vmware_vi.models.file_already_exists import FileAlreadyExists
from vmware_vi.models.file_locked import FileLocked
from vmware_vi.models.file_name_too_long import FileNameTooLong
from vmware_vi.models.file_not_found import FileNotFound
from vmware_vi.models.file_not_writable import FileNotWritable
from vmware_vi.models.file_too_large import FileTooLarge
from vmware_vi.models.incorrect_file_type import IncorrectFileType
from vmware_vi.models.network_copy_fault import NetworkCopyFault
from vmware_vi.models.no_disk_space import NoDiskSpace
from vmware_vi.models.not_a_directory import NotADirectory
from vmware_vi.models.not_a_file import NotAFile
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
from vmware_vi.models.too_many_concurrent_native_clones import TooManyConcurrentNativeClones
from vmware_vi.models.too_many_native_clone_levels import TooManyNativeCloneLevels
from vmware_vi.models.too_many_native_clones_on_file import TooManyNativeClonesOnFile
# TODO: Rewrite to not use raise_errors
FileFault.model_rebuild(raise_errors=False)

