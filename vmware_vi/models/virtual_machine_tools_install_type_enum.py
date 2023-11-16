# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class VirtualMachineToolsInstallTypeEnum(str, Enum):
    """
    The installation type of tools in the VM.  Possible values: - `guestToolsTypeUnknown`: Installation type is not known.      Most likely tools have been   installed by OSPs or open-vm-tools, but a version that does   not report its install type or an install type that we do   not recognize. - `guestToolsTypeMSI`: MSI is the installation type used for VMware Tools on Windows. - `guestToolsTypeTar`: Tools have been installed by the tar installer. - `guestToolsTypeOSP`: OSPs are RPM or Debian packages tailored for the OS in the VM.      See http://packages.vmware.com - `guestToolsTypeOpenVMTools`: open-vm-tools are the open-source version of VMware Tools, may have   been packaged by the OS vendor.    ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    GUESTTOOLSTYPEUNKNOWN = 'guestToolsTypeUnknown'
    GUESTTOOLSTYPEMSI = 'guestToolsTypeMSI'
    GUESTTOOLSTYPETAR = 'guestToolsTypeTar'
    GUESTTOOLSTYPEOSP = 'guestToolsTypeOSP'
    GUESTTOOLSTYPEOPENVMTOOLS = 'guestToolsTypeOpenVMTools'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineToolsInstallTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


