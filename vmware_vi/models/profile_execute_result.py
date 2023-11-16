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
from vmware_vi.models.host_config_spec import HostConfigSpec
from vmware_vi.models.profile_deferred_policy_option_parameter import ProfileDeferredPolicyOptionParameter
from vmware_vi.models.profile_execute_error import ProfileExecuteError
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProfileExecuteResult(DataObject):
    """
    The *ProfileExecuteResult* data object contains the results from a *HostProfile*.*HostProfile.ExecuteHostProfile* operation.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    status: StrictStr = Field(description="Status of the profile execution operation.  The value is a string that contains one of the *ProfileExecuteResultStatus_enum* enumerations.  ***Since:*** vSphere API 4.0 ")
    config_spec: Optional[HostConfigSpec] = Field(default=None, alias="configSpec")
    inapplicable_path: Optional[List[StrictStr]] = Field(default=None, description="List of property paths.  Each path identifies a policy that does not apply to this host. For example, if the precheck policies for a port group are not satisfied, the port group will not be created when you apply the profile to the host. Based on this information, the client might not display that part of the profile tree.  ***Since:*** vSphere API 4.0 ", alias="inapplicablePath")
    require_input: Optional[List[ProfileDeferredPolicyOptionParameter]] = Field(default=None, description="List that describes the required input for host configuration and identifies any policy options that still require parameter data.  Each entry in the list specifies the path to a policy and a parameter list. If the call to *HostProfile.ExecuteHostProfile* includes deferred parameters, the <code>requireInput</code> entries (<code>requireInput\\[\\].</code>*ProfileDeferredPolicyOptionParameter.parameter*\\[\\]) will be populated with the parameter data that was passed to the execute method. For policies that still require input data, the parameter list in the corresponding entry will be null.  A vSphere client that displays a GUI can use this information to show the host-specific configuration policy options. The client can highlight required input fields and ask the user for data in increments instead of collecting all of the input at once. For example, in the first pass, the client collects a minimum of user input and sends that to the Server. The Server evaluates the profile and might decide to invalidate a particular part of the subtree or enable a new subtree in the profile. This would result in a new set of invalid paths (*ProfileExecuteResult.inapplicablePath*\\[\\]) and required input property paths (*ProfileDeferredPolicyOptionParameter*.*ProfileDeferredPolicyOptionParameter.inputPath*). The client can make a series of calls to the method until it achieves a success status.  When *HostProfile.ExecuteHostProfile* returns a success status, the <code>requireInput</code> list contains the complete list of parameters, consisting of the following data: - Deferred parameter values resolved through successive calls to   *HostProfile.ExecuteHostProfile*. - Default parameter values from the host configuration. - User-specified values that override the defaults.    You can specify the returned <code>requireInput</code> list in the <code>userInput</code> parameter to the *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task* method. The Server will use the list to update the *AnswerFile* associated with the host.  ***Since:*** vSphere API 4.0 ", alias="requireInput")
    error: Optional[List[ProfileExecuteError]] = Field(default=None, description="List of errors that were encountered during execute.  This field will be set if status is set to error.  ***Since:*** vSphere API 4.0 ")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','ApplyHostProfileConfigurationSpec': 'ApplyHostProfileConfigurationSpec'
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
        """Create an instance of ProfileExecuteResult from a JSON string"""
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
        """Create an instance of ProfileExecuteResult from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("ProfileExecuteResult failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.apply_host_profile_configuration_spec import ApplyHostProfileConfigurationSpec
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
# TODO: Rewrite to not use raise_errors
ProfileExecuteResult.model_rebuild(raise_errors=False)

