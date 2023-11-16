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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.v_app_ip_assignment_info import VAppIPAssignmentInfo
from vmware_vi.models.v_app_ovf_section_spec import VAppOvfSectionSpec
from vmware_vi.models.v_app_product_spec import VAppProductSpec
from vmware_vi.models.v_app_property_spec import VAppPropertySpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VmConfigSpec(DataObject):
    """
    vApp related configuration of a VM.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    product: Optional[List[VAppProductSpec]] = Field(default=None, description="Information about the product.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ")
    var_property: Optional[List[VAppPropertySpec]] = Field(default=None, description="List of properties.  Adding and editing properties requires various privileges depending on which fields are affected. See *VAppPropertyInfo* for details.  Deleting properties requires the privilege VApp.ApplicationConfig.  ***Since:*** vSphere API 4.0 ", alias="property")
    ip_assignment: Optional[VAppIPAssignmentInfo] = Field(default=None, alias="ipAssignment")
    eula: Optional[List[StrictStr]] = Field(default=None, description="End User Liceses Agreements.  If this list is set, it replaces all exiting licenses. An empty list will not make any changes to installed licenses. A list with a single element {\"\"} will remove all licenses and leave an empty list.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ")
    ovf_section: Optional[List[VAppOvfSectionSpec]] = Field(default=None, description="List of uninterpreted OVF meta-data sections.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="ovfSection")
    ovf_environment_transport: Optional[List[StrictStr]] = Field(default=None, description="List the transports to use for properties.  Supported values are: iso and com.vmware.guestInfo.  If this list is set, it replaces all exiting entries. An empty list will not make any changes. A list with a single element {\"\"} will clear the list of transports.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="ovfEnvironmentTransport")
    install_boot_required: Optional[StrictBool] = Field(default=None, description="If this is on a VirtualMachine object, it specifies whether the VM needs an initial boot before the deployment is complete.  If this is on a vApp object, it indicates than one or more VMs needs an initial reboot. This flag is automatically reset once the reboot has happened.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="installBootRequired")
    install_boot_stop_delay: Optional[StrictInt] = Field(default=None, description="Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true).  A value of 0 means wait forever.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="installBootStopDelay")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','VAppConfigSpec': 'VAppConfigSpec'
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
        """Create an instance of VmConfigSpec from a JSON string"""
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
        """Create an instance of VmConfigSpec from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("VmConfigSpec failed to lookup discriminator value from " +
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
from vmware_vi.models.v_app_config_spec import VAppConfigSpec
# TODO: Rewrite to not use raise_errors
VmConfigSpec.model_rebuild(raise_errors=False)
