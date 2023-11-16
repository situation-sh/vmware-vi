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
from vmware_vi.models.int_option import IntOption
from vmware_vi.models.virtual_controller_option import VirtualControllerOption
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualPCIControllerOption(VirtualControllerOption):
    """
    This data object type contains the options for a virtual PCI Controller. 
    """ # noqa: E501
    num_scsi_controllers: IntOption = Field(alias="numSCSIControllers")
    num_ethernet_cards: IntOption = Field(alias="numEthernetCards")
    num_video_cards: IntOption = Field(alias="numVideoCards")
    num_sound_cards: IntOption = Field(alias="numSoundCards")
    num_vmi_roms: IntOption = Field(alias="numVmiRoms")
    num_vmci_devices: IntOption = Field(alias="numVmciDevices")
    num_pci_passthrough_devices: IntOption = Field(alias="numPCIPassthroughDevices")
    num_sas_scsi_controllers: IntOption = Field(alias="numSasSCSIControllers")
    num_vmxnet3_ethernet_cards: IntOption = Field(alias="numVmxnet3EthernetCards")
    num_para_virtual_scsi_controllers: IntOption = Field(alias="numParaVirtualSCSIControllers")
    num_sata_controllers: IntOption = Field(alias="numSATAControllers")
    num_nvme_controllers: Optional[IntOption] = Field(default=None, alias="numNVMEControllers")
    num_vmxnet3_vrdma_ethernet_cards: Optional[IntOption] = Field(default=None, alias="numVmxnet3VrdmaEthernetCards")
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
        """Create an instance of VirtualPCIControllerOption from a JSON string"""
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
        """Create an instance of VirtualPCIControllerOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

