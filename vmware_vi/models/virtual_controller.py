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
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.virtual_device import VirtualDevice
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualController(VirtualDevice):
    """
    VirtualController is the base data object type for a device controller in a virtual machine.  VirtualController extends *VirtualDevice* to inherit general information about a controller (such as name and description), and to allow controllers to appear in a generic list of virtual devices. 
    """ # noqa: E501
    bus_number: StrictInt = Field(description="Bus number associated with this controller. ", alias="busNumber")
    device: Optional[List[StrictInt]] = Field(default=None, description="List of devices currently controlled by this controller.  Each entry contains the *VirtualDevice.key* property of the corresponding device object. ")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','ParaVirtualSCSIController': 'ParaVirtualSCSIController','VirtualAHCIController': 'VirtualAHCIController','VirtualBusLogicController': 'VirtualBusLogicController','VirtualIDEController': 'VirtualIDEController','VirtualLsiLogicController': 'VirtualLsiLogicController','VirtualLsiLogicSASController': 'VirtualLsiLogicSASController','VirtualNVDIMMController': 'VirtualNVDIMMController','VirtualNVMEController': 'VirtualNVMEController','VirtualPCIController': 'VirtualPCIController','VirtualPS2Controller': 'VirtualPS2Controller','VirtualSATAController': 'VirtualSATAController','VirtualSCSIController': 'VirtualSCSIController','VirtualSIOController': 'VirtualSIOController','VirtualUSBController': 'VirtualUSBController','VirtualUSBXHCIController': 'VirtualUSBXHCIController'
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
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of VirtualController from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of VirtualController from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("VirtualController failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.para_virtual_scsi_controller import ParaVirtualSCSIController
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
from vmware_vi.models.virtual_ahci_controller import VirtualAHCIController
from vmware_vi.models.virtual_bus_logic_controller import VirtualBusLogicController
from vmware_vi.models.virtual_ide_controller import VirtualIDEController
from vmware_vi.models.virtual_lsi_logic_controller import VirtualLsiLogicController
from vmware_vi.models.virtual_lsi_logic_sas_controller import VirtualLsiLogicSASController
from vmware_vi.models.virtual_nvdimm_controller import VirtualNVDIMMController
from vmware_vi.models.virtual_nvme_controller import VirtualNVMEController
from vmware_vi.models.virtual_pci_controller import VirtualPCIController
from vmware_vi.models.virtual_ps2_controller import VirtualPS2Controller
from vmware_vi.models.virtual_sata_controller import VirtualSATAController
from vmware_vi.models.virtual_scsi_controller import VirtualSCSIController
from vmware_vi.models.virtual_sio_controller import VirtualSIOController
from vmware_vi.models.virtual_usb_controller import VirtualUSBController
from vmware_vi.models.virtual_usbxhci_controller import VirtualUSBXHCIController
# TODO: Rewrite to not use raise_errors
VirtualController.model_rebuild(raise_errors=False)

