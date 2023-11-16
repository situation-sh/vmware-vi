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
from pydantic import StrictBool, StrictBytes, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from vmware_vi.models.about_info import AboutInfo
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_assignable_hardware_binding import HostAssignableHardwareBinding
from vmware_vi.models.host_assignable_hardware_config import HostAssignableHardwareConfig
from vmware_vi.models.host_authentication_manager_info import HostAuthenticationManagerInfo
from vmware_vi.models.host_auto_start_manager_config import HostAutoStartManagerConfig
from vmware_vi.models.host_cache_configuration_info import HostCacheConfigurationInfo
from vmware_vi.models.host_datastore_system_capabilities import HostDatastoreSystemCapabilities
from vmware_vi.models.host_date_time_info import HostDateTimeInfo
from vmware_vi.models.host_deployment_info import HostDeploymentInfo
from vmware_vi.models.host_diagnostic_partition import HostDiagnosticPartition
from vmware_vi.models.host_feature_capability import HostFeatureCapability
from vmware_vi.models.host_feature_version_info import HostFeatureVersionInfo
from vmware_vi.models.host_file_system_volume_info import HostFileSystemVolumeInfo
from vmware_vi.models.host_firewall_info import HostFirewallInfo
from vmware_vi.models.host_flag_info import HostFlagInfo
from vmware_vi.models.host_graphics_config import HostGraphicsConfig
from vmware_vi.models.host_graphics_info import HostGraphicsInfo
from vmware_vi.models.host_hyper_thread_schedule_info import HostHyperThreadScheduleInfo
from vmware_vi.models.host_io_filter_info import HostIoFilterInfo
from vmware_vi.models.host_ipmi_info import HostIpmiInfo
from vmware_vi.models.host_lockdown_mode_enum import HostLockdownModeEnum
from vmware_vi.models.host_multipath_state_info import HostMultipathStateInfo
from vmware_vi.models.host_net_capabilities import HostNetCapabilities
from vmware_vi.models.host_net_offload_capabilities import HostNetOffloadCapabilities
from vmware_vi.models.host_network_info import HostNetworkInfo
from vmware_vi.models.host_pci_passthru_info import HostPciPassthruInfo
from vmware_vi.models.host_service_info import HostServiceInfo
from vmware_vi.models.host_shared_gpu_capabilities import HostSharedGpuCapabilities
from vmware_vi.models.host_sriov_device_pool_info import HostSriovDevicePoolInfo
from vmware_vi.models.host_ssl_thumbprint_info import HostSslThumbprintInfo
from vmware_vi.models.host_storage_device_info import HostStorageDeviceInfo
from vmware_vi.models.host_system_resource_info import HostSystemResourceInfo
from vmware_vi.models.host_system_swap_configuration import HostSystemSwapConfiguration
from vmware_vi.models.host_v_flash_manager_v_flash_config_info import HostVFlashManagerVFlashConfigInfo
from vmware_vi.models.host_v_motion_info import HostVMotionInfo
from vmware_vi.models.host_virtual_nic_manager_info import HostVirtualNicManagerInfo
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.option_def import OptionDef
from vmware_vi.models.option_value import OptionValue
from vmware_vi.models.power_system_capability import PowerSystemCapability
from vmware_vi.models.power_system_info import PowerSystemInfo
from vmware_vi.models.service_console_reservation_info import ServiceConsoleReservationInfo
from vmware_vi.models.virtual_machine_memory_reservation_info import VirtualMachineMemoryReservationInfo
from vmware_vi.models.vsan_host_config_info import VsanHostConfigInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostConfigInfo(DataObject):
    """
    This data object type encapsulates a typical set of host configuration information that is useful for displaying and configuring a host.  VirtualCenter can retrieve this set of information very efficiently even for a large set of hosts. 
    """ # noqa: E501
    host: ManagedObjectReference
    product: AboutInfo
    deployment_info: Optional[HostDeploymentInfo] = Field(default=None, alias="deploymentInfo")
    hyper_thread: Optional[HostHyperThreadScheduleInfo] = Field(default=None, alias="hyperThread")
    console_reservation: Optional[ServiceConsoleReservationInfo] = Field(default=None, alias="consoleReservation")
    virtual_machine_reservation: Optional[VirtualMachineMemoryReservationInfo] = Field(default=None, alias="virtualMachineReservation")
    storage_device: Optional[HostStorageDeviceInfo] = Field(default=None, alias="storageDevice")
    multipath_state: Optional[HostMultipathStateInfo] = Field(default=None, alias="multipathState")
    file_system_volume: Optional[HostFileSystemVolumeInfo] = Field(default=None, alias="fileSystemVolume")
    system_file: Optional[List[StrictStr]] = Field(default=None, description="Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host.  For information on datastore paths, see *Datastore*.  ***Since:*** vSphere API 4.1 ", alias="systemFile")
    network: Optional[HostNetworkInfo] = None
    vmotion: Optional[HostVMotionInfo] = None
    virtual_nic_manager_info: Optional[HostVirtualNicManagerInfo] = Field(default=None, alias="virtualNicManagerInfo")
    capabilities: Optional[HostNetCapabilities] = None
    datastore_capabilities: Optional[HostDatastoreSystemCapabilities] = Field(default=None, alias="datastoreCapabilities")
    offload_capabilities: Optional[HostNetOffloadCapabilities] = Field(default=None, alias="offloadCapabilities")
    service: Optional[HostServiceInfo] = None
    firewall: Optional[HostFirewallInfo] = None
    auto_start: Optional[HostAutoStartManagerConfig] = Field(default=None, alias="autoStart")
    active_diagnostic_partition: Optional[HostDiagnosticPartition] = Field(default=None, alias="activeDiagnosticPartition")
    option: Optional[List[OptionValue]] = Field(default=None, description="Host configuration options as defined by the *OptionValue* data object type. ")
    option_def: Optional[List[OptionDef]] = Field(default=None, description="A list of supported options. ", alias="optionDef")
    datastore_principal: Optional[StrictStr] = Field(default=None, description="Datastore principal user ", alias="datastorePrincipal")
    local_swap_datastore: Optional[ManagedObjectReference] = Field(default=None, alias="localSwapDatastore")
    system_swap_configuration: Optional[HostSystemSwapConfiguration] = Field(default=None, alias="systemSwapConfiguration")
    system_resources: Optional[HostSystemResourceInfo] = Field(default=None, alias="systemResources")
    date_time_info: Optional[HostDateTimeInfo] = Field(default=None, alias="dateTimeInfo")
    flags: Optional[HostFlagInfo] = None
    admin_disabled: Optional[StrictBool] = Field(default=None, description="Deprecated as of vSphere API 6.0, use *HostConfigInfo.lockdownMode*.  If the flag is true, the permissions on the host have been modified such that it is only accessible through local console or an authorized centralized management application.  This flag is affected by the *HostSystem.EnterLockdownMode* and *HostSystem.ExitLockdownMode* operations.  This flag is supported in VirtualCenter only. The value returned from host should be ignored.  See also *HostSystem.EnterLockdownMode*, *HostSystem.ExitLockdownMode*.  ***Since:*** VI API 2.5 ", alias="adminDisabled")
    lockdown_mode: Optional[HostLockdownModeEnum] = Field(default=None, alias="lockdownMode")
    ipmi: Optional[HostIpmiInfo] = None
    ssl_thumbprint_info: Optional[HostSslThumbprintInfo] = Field(default=None, alias="sslThumbprintInfo")
    ssl_thumbprint_data: Optional[List[HostSslThumbprintInfo]] = Field(default=None, description="SSL Thumbprints registered on this host.  ***Since:*** vSphere API 5.0 ", alias="sslThumbprintData")
    certificate: Optional[List[Annotated[int, Field(le=127, strict=True, ge=-128)]]] = Field(default=None, description="Full Host Certificate in PEM format, if known  ***Since:*** vSphere API 5.0 ")
    pci_passthru_info: Optional[List[HostPciPassthruInfo]] = Field(default=None, description="PCI passthrough information.  ***Since:*** vSphere API 4.0 ", alias="pciPassthruInfo")
    authentication_manager_info: Optional[HostAuthenticationManagerInfo] = Field(default=None, alias="authenticationManagerInfo")
    feature_version: Optional[List[HostFeatureVersionInfo]] = Field(default=None, description="List of feature-specific version information.  Each element refers to the version information for a specific feature.  ***Since:*** vSphere API 4.1 ", alias="featureVersion")
    power_system_capability: Optional[PowerSystemCapability] = Field(default=None, alias="powerSystemCapability")
    power_system_info: Optional[PowerSystemInfo] = Field(default=None, alias="powerSystemInfo")
    cache_configuration_info: Optional[List[HostCacheConfigurationInfo]] = Field(default=None, description="Host solid stats drive cache configuration information.  ***Since:*** vSphere API 5.0 ", alias="cacheConfigurationInfo")
    wake_on_lan_capable: Optional[StrictBool] = Field(default=None, description="Indicates if a host is wake on lan capable.  A host is deemed wake on lan capable if there exists at least one physical network card that is both backing the vmotion interface and is itself wake on lan capable.  ***Since:*** vSphere API 5.0 ", alias="wakeOnLanCapable")
    feature_capability: Optional[List[HostFeatureCapability]] = Field(default=None, description="Array of host feature capabilities.  This is expected to change infrequently. It may change while host is in maintenance mode and between reboots if hardware, firmware, or a device driver is changed or upgraded.  ***Since:*** vSphere API 5.1 ", alias="featureCapability")
    masked_feature_capability: Optional[List[HostFeatureCapability]] = Field(default=None, description="Array of the feature capabilities that the host has after the mask has been applied.  ***Since:*** vSphere API 5.1 ", alias="maskedFeatureCapability")
    v_flash_config_info: Optional[HostVFlashManagerVFlashConfigInfo] = Field(default=None, alias="vFlashConfigInfo")
    vsan_host_config: Optional[VsanHostConfigInfo] = Field(default=None, alias="vsanHostConfig")
    domain_list: Optional[List[StrictStr]] = Field(default=None, description="List of Windows domains available for user searches, if the underlying system supports windows domain membership.  See *UserDirectory.domainList*.  ***Since:*** vSphere API 6.0 ", alias="domainList")
    script_check_sum: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="A checksum of overhead computation script.  (For VMware internal usage only)  ***Since:*** vSphere API 6.0 ", alias="scriptCheckSum")
    host_config_check_sum: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="A checksum of host configuration option set.  (For VMware internal usage only)  ***Since:*** vSphere API 6.0 ", alias="hostConfigCheckSum")
    description_tree_check_sum: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="A checksum of the Assignable Hardware Description Tree.  (For VMware internal usage only)  ***Since:*** vSphere API 7.0 ", alias="descriptionTreeCheckSum")
    graphics_info: Optional[List[HostGraphicsInfo]] = Field(default=None, description="The list of graphics devices available on this host.  ***Since:*** vSphere API 5.5 ", alias="graphicsInfo")
    shared_passthru_gpu_types: Optional[List[StrictStr]] = Field(default=None, description="Array of shared passthru GPU types.  These GPU types may be enabled when specific host hardware is present.  ***Since:*** vSphere API 6.0 ", alias="sharedPassthruGpuTypes")
    graphics_config: Optional[HostGraphicsConfig] = Field(default=None, alias="graphicsConfig")
    shared_gpu_capabilities: Optional[List[HostSharedGpuCapabilities]] = Field(default=None, description="Array of shared passthru GPU capablities.  See also *HostSharedGpuCapabilities*.  ***Since:*** vSphere API 6.7 ", alias="sharedGpuCapabilities")
    io_filter_info: Optional[List[HostIoFilterInfo]] = Field(default=None, description="Information of the IO Filters installed on the host.  See *HostIoFilterInfo*.  ***Since:*** vSphere API 6.0 ", alias="ioFilterInfo")
    sriov_device_pool: Optional[List[HostSriovDevicePoolInfo]] = Field(default=None, description="Information on SRIOV device pools present on host.  ***Since:*** vSphere API 6.5 ", alias="sriovDevicePool")
    assignable_hardware_binding: Optional[List[HostAssignableHardwareBinding]] = Field(default=None, description="Information describing Assignable Hardware device bindings on host.  See *HostAssignableHardwareBinding*.  ***Since:*** vSphere API 7.0 ", alias="assignableHardwareBinding")
    assignable_hardware_config: Optional[HostAssignableHardwareConfig] = Field(default=None, alias="assignableHardwareConfig")
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
        """Create an instance of HostConfigInfo from a JSON string"""
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
        """Create an instance of HostConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

