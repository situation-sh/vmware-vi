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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.key_value import KeyValue
from vmware_vi.models.method_fault import MethodFault
from vmware_vi.models.ovf_consumer_ost_node import OvfConsumerOstNode
from vmware_vi.models.ovf_deployment_option import OvfDeploymentOption
from vmware_vi.models.ovf_network_info import OvfNetworkInfo
from vmware_vi.models.v_app_product_info import VAppProductInfo
from vmware_vi.models.v_app_property_info import VAppPropertyInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OvfParseDescriptorResult(DataObject):
    """
    OvfParseDescriptorResult
    """ # noqa: E501
    eula: Optional[List[StrictStr]] = Field(default=None, description="The list of all EULAs contained in the OVF  ***Since:*** vSphere API 4.0 ")
    network: Optional[List[OvfNetworkInfo]] = Field(default=None, description="The list of networks required by the OVF  ***Since:*** vSphere API 4.0 ")
    ip_allocation_scheme: Optional[List[StrictStr]] = Field(default=None, description="The kind of IP allocation supported by the guest.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0 ", alias="ipAllocationScheme")
    ip_protocols: Optional[List[StrictStr]] = Field(default=None, description="The IP protocols supported by the guest.  See *VAppIPAssignmentInfo*.  ***Since:*** vSphere API 4.0 ", alias="ipProtocols")
    var_property: Optional[List[VAppPropertyInfo]] = Field(default=None, description="Metadata about the properties contained in the OVF  ***Since:*** vSphere API 4.0 ", alias="property")
    product_info: Optional[VAppProductInfo] = Field(default=None, alias="productInfo")
    annotation: StrictStr = Field(description="The annotation info contained in the OVF  ***Since:*** vSphere API 4.0 ")
    approximate_download_size: Optional[StrictInt] = Field(default=None, description="The OVF Manager's best guess as to the total amount of data that must be transferred to download the entity.  This may be inaccurate due to disk compression etc.  ***Since:*** vSphere API 4.0 ", alias="approximateDownloadSize")
    approximate_flat_deployment_size: Optional[StrictInt] = Field(default=None, description="The OVF Manager's best guess as to the total amount of space required to deploy the entity if using flat disks.  ***Since:*** vSphere API 4.0 ", alias="approximateFlatDeploymentSize")
    approximate_sparse_deployment_size: Optional[StrictInt] = Field(default=None, description="The OVF Manager's best guess as to the total amount of space required to deploy the entity using sparse disks.  ***Since:*** vSphere API 4.0 ", alias="approximateSparseDeploymentSize")
    default_entity_name: StrictStr = Field(description="The default name to use for the entity, if a product name is not specified.  This is the ID of the OVF top-level entity, or taken from a ProductSection.  ***Since:*** vSphere API 4.0 ", alias="defaultEntityName")
    virtual_app: StrictBool = Field(description="True if the OVF contains a vApp (containing one or more vApps and/or virtual machines), as opposed to a single virtual machine.  ***Since:*** vSphere API 4.0 ", alias="virtualApp")
    deployment_option: Optional[List[OvfDeploymentOption]] = Field(default=None, description="The list of possible deployment options.  ***Since:*** vSphere API 4.0 ", alias="deploymentOption")
    default_deployment_option: StrictStr = Field(description="The key of the default deployment option.  Empty only if there are no deployment options.  ***Since:*** vSphere API 4.0 ", alias="defaultDeploymentOption")
    entity_name: Optional[List[KeyValue]] = Field(default=None, description="A list of the child entities contained in this package and their location in the vApp hierarchy.  Each entry is a (key,value) pair, where the key is the display name, and the value is a unique path identifier for the entity in the vApp. The path is constructed by appending the id of each entity of the path down to the entity, separated by slashes. For example, the path for a child of the root entity with id = \"vm1\", would simply be \"vm1\". If the vm is the child of a VirtualSystemCollection called \"webTier\", then the path would be \"webTier/vm\".  ***Since:*** vSphere API 4.1 ", alias="entityName")
    annotated_ost: Optional[OvfConsumerOstNode] = Field(default=None, alias="annotatedOst")
    error: Optional[List[MethodFault]] = Field(default=None, description="Errors that happened during processing.  Something will be wrong with the result.  For example, during export, devices could be missing (in which case this array will contain one or more instances of Unsupported-/UnknownDevice).  ***Since:*** vSphere API 4.0 ")
    warning: Optional[List[MethodFault]] = Field(default=None, description="Non-fatal warnings from the processing.  The result will be valid, but the user may choose to reject it based on these warnings.  ***Since:*** vSphere API 4.0 ")
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
        """Create an instance of OvfParseDescriptorResult from a JSON string"""
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
        """Create an instance of OvfParseDescriptorResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


