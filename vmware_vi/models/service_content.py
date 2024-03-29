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
from vmware_vi.models.about_info import AboutInfo
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceContent(DataObject):
    """
    The *ServiceContent* data object defines properties for the ServiceInstance managed object.  The ServiceInstance itself does not have directly-accessible properties because reading the properties of a managed object requires the use of a property collector, and the property collector itself is a property of the *ServiceInstance*. For this reason, use the method *ServiceInstance.RetrieveServiceContent* to retrieve the *ServiceContent* object. 
    """ # noqa: E501
    root_folder: ManagedObjectReference = Field(alias="rootFolder")
    property_collector: ManagedObjectReference = Field(alias="propertyCollector")
    view_manager: Optional[ManagedObjectReference] = Field(default=None, alias="viewManager")
    about: AboutInfo
    setting: Optional[ManagedObjectReference] = None
    user_directory: Optional[ManagedObjectReference] = Field(default=None, alias="userDirectory")
    session_manager: Optional[ManagedObjectReference] = Field(default=None, alias="sessionManager")
    authorization_manager: Optional[ManagedObjectReference] = Field(default=None, alias="authorizationManager")
    service_manager: Optional[ManagedObjectReference] = Field(default=None, alias="serviceManager")
    perf_manager: Optional[ManagedObjectReference] = Field(default=None, alias="perfManager")
    scheduled_task_manager: Optional[ManagedObjectReference] = Field(default=None, alias="scheduledTaskManager")
    alarm_manager: Optional[ManagedObjectReference] = Field(default=None, alias="alarmManager")
    event_manager: Optional[ManagedObjectReference] = Field(default=None, alias="eventManager")
    task_manager: Optional[ManagedObjectReference] = Field(default=None, alias="taskManager")
    extension_manager: Optional[ManagedObjectReference] = Field(default=None, alias="extensionManager")
    customization_spec_manager: Optional[ManagedObjectReference] = Field(default=None, alias="customizationSpecManager")
    guest_customization_manager: Optional[ManagedObjectReference] = Field(default=None, alias="guestCustomizationManager")
    custom_fields_manager: Optional[ManagedObjectReference] = Field(default=None, alias="customFieldsManager")
    account_manager: Optional[ManagedObjectReference] = Field(default=None, alias="accountManager")
    diagnostic_manager: Optional[ManagedObjectReference] = Field(default=None, alias="diagnosticManager")
    license_manager: Optional[ManagedObjectReference] = Field(default=None, alias="licenseManager")
    search_index: Optional[ManagedObjectReference] = Field(default=None, alias="searchIndex")
    file_manager: Optional[ManagedObjectReference] = Field(default=None, alias="fileManager")
    datastore_namespace_manager: Optional[ManagedObjectReference] = Field(default=None, alias="datastoreNamespaceManager")
    virtual_disk_manager: Optional[ManagedObjectReference] = Field(default=None, alias="virtualDiskManager")
    virtualization_manager: Optional[ManagedObjectReference] = Field(default=None, alias="virtualizationManager")
    snmp_system: Optional[ManagedObjectReference] = Field(default=None, alias="snmpSystem")
    vm_provisioning_checker: Optional[ManagedObjectReference] = Field(default=None, alias="vmProvisioningChecker")
    vm_compatibility_checker: Optional[ManagedObjectReference] = Field(default=None, alias="vmCompatibilityChecker")
    ovf_manager: Optional[ManagedObjectReference] = Field(default=None, alias="ovfManager")
    ip_pool_manager: Optional[ManagedObjectReference] = Field(default=None, alias="ipPoolManager")
    dv_switch_manager: Optional[ManagedObjectReference] = Field(default=None, alias="dvSwitchManager")
    host_profile_manager: Optional[ManagedObjectReference] = Field(default=None, alias="hostProfileManager")
    cluster_profile_manager: Optional[ManagedObjectReference] = Field(default=None, alias="clusterProfileManager")
    compliance_manager: Optional[ManagedObjectReference] = Field(default=None, alias="complianceManager")
    localization_manager: Optional[ManagedObjectReference] = Field(default=None, alias="localizationManager")
    storage_resource_manager: Optional[ManagedObjectReference] = Field(default=None, alias="storageResourceManager")
    guest_operations_manager: Optional[ManagedObjectReference] = Field(default=None, alias="guestOperationsManager")
    overhead_memory_manager: Optional[ManagedObjectReference] = Field(default=None, alias="overheadMemoryManager")
    certificate_manager: Optional[ManagedObjectReference] = Field(default=None, alias="certificateManager")
    io_filter_manager: Optional[ManagedObjectReference] = Field(default=None, alias="ioFilterManager")
    v_storage_object_manager: Optional[ManagedObjectReference] = Field(default=None, alias="vStorageObjectManager")
    host_spec_manager: Optional[ManagedObjectReference] = Field(default=None, alias="hostSpecManager")
    crypto_manager: Optional[ManagedObjectReference] = Field(default=None, alias="cryptoManager")
    health_update_manager: Optional[ManagedObjectReference] = Field(default=None, alias="healthUpdateManager")
    failover_cluster_configurator: Optional[ManagedObjectReference] = Field(default=None, alias="failoverClusterConfigurator")
    failover_cluster_manager: Optional[ManagedObjectReference] = Field(default=None, alias="failoverClusterManager")
    tenant_manager: Optional[ManagedObjectReference] = Field(default=None, alias="tenantManager")
    site_info_manager: Optional[ManagedObjectReference] = Field(default=None, alias="siteInfoManager")
    storage_query_manager: Optional[ManagedObjectReference] = Field(default=None, alias="storageQueryManager")
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
        """Create an instance of ServiceContent from a JSON string"""
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
        """Create an instance of ServiceContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


