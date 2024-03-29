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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.virtual_hardware_compatibility_issue import VirtualHardwareCompatibilityIssue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CpuIncompatible(VirtualHardwareCompatibilityIssue):
    """
    Deprecated as of vSphere API 6.5 use *FeatureRequirementsNotMet*.  The host is not compatible with the CPU feature requirements of the virtual machine, for a particular CPUID register.  A subclass of this fault may be used to express the incompatibilities in a more easily understandable format. 
    """ # noqa: E501
    level: StrictInt = Field(description="The CpuIdInfo level where a problem was detected.  Other levels may also have problems. ")
    register_name: StrictStr = Field(description="The CpuIdInfo register where a problem was detected.  Other registers may also have problems. Possible register names are eax, ebx, ecx, or edx. ", alias="registerName")
    register_bits: Optional[StrictStr] = Field(default=None, description="The contents of the register on the target host, in CpuIdInfo register format.  The '-' character indicates an unknown value.  ***Since:*** VI API 2.5 ", alias="registerBits")
    desired_bits: Optional[StrictStr] = Field(default=None, description="The desired values for the register's bits.  The 'x' character indicates don't-care.  ***Since:*** VI API 2.5 ", alias="desiredBits")
    host: Optional[ManagedObjectReference] = None
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','CpuCompatibilityUnknown': 'CpuCompatibilityUnknown','CpuIncompatible1ECX': 'CpuIncompatible1ECX','CpuIncompatible81EDX': 'CpuIncompatible81EDX','FaultToleranceCpuIncompatible': 'FaultToleranceCpuIncompatible'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self]:
        """Create an instance of CpuIncompatible from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self]:
        """Create an instance of CpuIncompatible from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("CpuIncompatible failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.cpu_compatibility_unknown import CpuCompatibilityUnknown
from vmware_vi.models.cpu_incompatible1_ecx import CpuIncompatible1ECX
from vmware_vi.models.cpu_incompatible81_edx import CpuIncompatible81EDX
from vmware_vi.models.fault_tolerance_cpu_incompatible import FaultToleranceCpuIncompatible
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
# TODO: Rewrite to not use raise_errors
CpuIncompatible.model_rebuild(raise_errors=False)

