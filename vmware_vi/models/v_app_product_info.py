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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VAppProductInfo(DataObject):
    """
    Information that describes what product a vApp contains, for example, the software that is installed in the contained virtual machines.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: StrictInt = Field(description="A unique key for the product section  ***Since:*** vSphere API 4.0 ")
    class_id: Optional[StrictStr] = Field(default=None, description="Class name for this attribute.  Valid values for classId: Any string except any white-space characters.  ***Since:*** vSphere API 4.0 ", alias="classId")
    instance_id: Optional[StrictStr] = Field(default=None, description="Class name for this attribute.  Valid values for instanceId: Any string except any white-space characters.  ***Since:*** vSphere API 4.0 ", alias="instanceId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the product.  ***Since:*** vSphere API 4.0 ")
    vendor: Optional[StrictStr] = Field(default=None, description="Vendor of the product.  ***Since:*** vSphere API 4.0 ")
    version: Optional[StrictStr] = Field(default=None, description="Short version of the product, for example, 1.0.  ***Since:*** vSphere API 4.0 ")
    full_version: Optional[StrictStr] = Field(default=None, description="Full-version of the product, for example, 1.0-build 12323.  ***Since:*** vSphere API 4.0 ", alias="fullVersion")
    vendor_url: Optional[StrictStr] = Field(default=None, description="URL to vendor homepage.  ***Since:*** vSphere API 4.0 ", alias="vendorUrl")
    product_url: Optional[StrictStr] = Field(default=None, description="URL to product homepage.  ***Since:*** vSphere API 4.0 ", alias="productUrl")
    app_url: Optional[StrictStr] = Field(default=None, description="URL to entry-point for application.  This is often specified using a macro, for example, http://${app.ip}/, where app.ip is a defined property on the virtual machine or vApp container.  ***Since:*** vSphere API 4.0 ", alias="appUrl")
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
        """Create an instance of VAppProductInfo from a JSON string"""
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
        """Create an instance of VAppProductInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

