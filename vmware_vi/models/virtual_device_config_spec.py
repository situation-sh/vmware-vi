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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.virtual_device import VirtualDevice
from vmware_vi.models.virtual_device_config_spec_backing_spec import VirtualDeviceConfigSpecBackingSpec
from vmware_vi.models.virtual_device_config_spec_file_operation_enum import VirtualDeviceConfigSpecFileOperationEnum
from vmware_vi.models.virtual_device_config_spec_operation_enum import VirtualDeviceConfigSpecOperationEnum
from vmware_vi.models.virtual_machine_base_independent_filter_spec import VirtualMachineBaseIndependentFilterSpec
from vmware_vi.models.virtual_machine_profile_spec import VirtualMachineProfileSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualDeviceConfigSpec(DataObject):
    """
    The VirtualDeviceSpec data object type encapsulates change specifications for an individual virtual device.  The virtual device being added or modified must be fully specified. 
    """ # noqa: E501
    operation: Optional[VirtualDeviceConfigSpecOperationEnum] = None
    file_operation: Optional[VirtualDeviceConfigSpecFileOperationEnum] = Field(default=None, alias="fileOperation")
    device: VirtualDevice
    profile: Optional[List[VirtualMachineProfileSpec]] = Field(default=None, description="Virtual Device Profile requirement.  Profiles are solution specifics. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM service. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5 ")
    backing: Optional[VirtualDeviceConfigSpecBackingSpec] = None
    filter_spec: Optional[List[VirtualMachineBaseIndependentFilterSpec]] = Field(default=None, description="List of independent filters *VirtualMachineIndependentFilterSpec* to configure on the virtual device.  ***Since:*** vSphere API 7.0.2.1 ", alias="filterSpec")
    change_mode: Optional[StrictStr] = Field(default=None, description="The change mode of the device.  The values of the mode will be one of *VirtualDeviceConfigSpecChangeMode_enum* enumerations. On unset, default to 'fail'. ", alias="changeMode")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','VirtualDiskConfigSpec': 'VirtualDiskConfigSpec'
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
    def from_json(cls, json_str: str) -> Union[Self]:
        """Create an instance of VirtualDeviceConfigSpec from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self]:
        """Create an instance of VirtualDeviceConfigSpec from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("VirtualDeviceConfigSpec failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
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
from vmware_vi.models.virtual_disk_config_spec import VirtualDiskConfigSpec
# TODO: Rewrite to not use raise_errors
VirtualDeviceConfigSpec.model_rebuild(raise_errors=False)
