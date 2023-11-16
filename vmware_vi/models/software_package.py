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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.relation import Relation
from vmware_vi.models.software_package_capability import SoftwarePackageCapability
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SoftwarePackage(DataObject):
    """
    Software Packages provide discrete version and packaging.  This data is reported by CLI:: esxcli software vib get -n ...  ***Since:*** vSphere API 6.5 
    """ # noqa: E501
    name: StrictStr = Field(description="Identifier that uniquely identifies the software package.  ***Since:*** vSphere API 6.5 ")
    version: StrictStr = Field(description="Version string uniquely identifies this package.  ***Since:*** vSphere API 6.5 ")
    type: StrictStr = Field(description="Type of vib installed.  See *SoftwarePackageVibType_enum*.  ***Since:*** vSphere API 6.5 ")
    vendor: StrictStr = Field(description="The corporate entity that created this package.  ***Since:*** vSphere API 6.5 ")
    acceptance_level: StrictStr = Field(description="See also *HostImageAcceptanceLevel_enum*.  ***Since:*** vSphere API 6.5 ", alias="acceptanceLevel")
    summary: StrictStr = Field(description="A brief description of the package contents.  ***Since:*** vSphere API 6.5 ")
    description: StrictStr = Field(description="A full account of the package contents.  ***Since:*** vSphere API 6.5 ")
    reference_url: Optional[List[StrictStr]] = Field(default=None, description="The list of SupportReference objects with in-depth support information.  ***Since:*** vSphere API 6.5 ", alias="referenceURL")
    creation_date: Optional[datetime] = Field(default=None, description="The time when the package was installed.  On Autodeploy stateless installs there is no set value.  ***Since:*** vSphere API 6.5 ", alias="creationDate")
    depends: Optional[List[Relation]] = Field(default=None, description="A list of VIBs that must be installed at the same time as this VIB.  ***Since:*** vSphere API 6.5 ")
    conflicts: Optional[List[Relation]] = Field(default=None, description="A list of VIBs that cannot be installed at the same time as this VIB for a given version.  ***Since:*** vSphere API 6.5 ")
    replaces: Optional[List[Relation]] = Field(default=None, description="A list of SoftwareConstraint objects that identify VIBs that replace this VIB or make it obsolete.  VIBs automatically replace VIBs with the same name but lower versions.  ***Since:*** vSphere API 6.5 ")
    provides: Optional[List[StrictStr]] = Field(default=None, description="A list of virtual packages or interfaces this VIB provides.  ***Since:*** vSphere API 6.5 ")
    maintenance_mode_required: Optional[StrictBool] = Field(default=None, description="True if hosts must be in maintenance mode for installation of this VIB.  ***Since:*** vSphere API 6.5 ", alias="maintenanceModeRequired")
    hardware_platforms_required: Optional[List[StrictStr]] = Field(default=None, description="A list of hardware platforms this package is supported on.  ***Since:*** vSphere API 6.5 ", alias="hardwarePlatformsRequired")
    capability: SoftwarePackageCapability
    tag: Optional[List[StrictStr]] = Field(default=None, description="A list of string tags for this package defined by the vendor or publisher.  Tags can be used to identify characteristics of a package.  ***Since:*** vSphere API 6.5 ")
    payload: Optional[List[StrictStr]] = Field(default=None, description="A list of string tags to indicate one or more of what is contained: may be one of bootloader, upgrade, bootisobios, bootisoefi, vgz, tgz, boot or other values.  ***Since:*** vSphere API 6.5 ")
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
        """Create an instance of SoftwarePackage from a JSON string"""
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
        """Create an instance of SoftwarePackage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


