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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.cannot_access_vm_component import CannotAccessVmComponent
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CannotAccessVmDevice(CannotAccessVmComponent):
    """
    One of the virtual machine's devices uses a backing that is not accessible on the host.  Following is a discussion of this fault's use in migration validation. This is an error if the device is currently connected and a warning otherwise. Devices that can be disconnected can only be connected if the virtual machine is powered on.  The usage of this fault is slightly different if the backing of a device is inherently host-local, and therefore not shared or globally named among hosts. (Examples of such backings: physical CD-ROM drive, physical serial port.) If a device with such a backing is currently connected, that will be a migration error. If the device is disconnected, there will be a warning if no backing with the same name exists on the destination host. If the device is disconnected and a backing with the same name exists on the destination host, this is neither a warning nor an error case, even though the destination host's backing is not the same instance as the source host's. It is assumed that use of the host-local backing is what is desired for the device. 
    """ # noqa: E501
    device: StrictStr = Field(description="The label of the device. ")
    backing: StrictStr = Field(description="The backing of the device. ")
    connected: StrictBool = Field(description="The connected/disconnected state of the device. ")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','CannotAccessNetwork': 'CannotAccessNetwork','CannotAccessVmDisk': 'CannotAccessVmDisk','DestinationSwitchFull': 'DestinationSwitchFull','LegacyNetworkInterfaceInUse': 'LegacyNetworkInterfaceInUse','RDMPointsToInaccessibleDisk': 'RDMPointsToInaccessibleDisk','VMOnConflictDVPort': 'VMOnConflictDVPort','VMOnVirtualIntranet': 'VMOnVirtualIntranet'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of CannotAccessVmDevice from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of CannotAccessVmDevice from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("CannotAccessVmDevice failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.cannot_access_network import CannotAccessNetwork
from vmware_vi.models.cannot_access_vm_disk import CannotAccessVmDisk
from vmware_vi.models.destination_switch_full import DestinationSwitchFull
from vmware_vi.models.legacy_network_interface_in_use import LegacyNetworkInterfaceInUse
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
from vmware_vi.models.rdm_points_to_inaccessible_disk import RDMPointsToInaccessibleDisk
from vmware_vi.models.vmon_conflict_dv_port import VMOnConflictDVPort
from vmware_vi.models.vmon_virtual_intranet import VMOnVirtualIntranet
# TODO: Rewrite to not use raise_errors
CannotAccessVmDevice.model_rebuild(raise_errors=False)

