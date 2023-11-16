# vmware_vi.HostStorageSystemApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_storage_system_add_internet_scsi_send_targets**](HostStorageSystemApi.md#host_storage_system_add_internet_scsi_send_targets) | **POST** /HostStorageSystem/{moId}/AddInternetScsiSendTargets | Adds Send Target entries to the host bus adapter discovery list. 
[**host_storage_system_add_internet_scsi_static_targets**](HostStorageSystemApi.md#host_storage_system_add_internet_scsi_static_targets) | **POST** /HostStorageSystem/{moId}/AddInternetScsiStaticTargets | Adds Static Target entries to the host bus adapter discovery list. 
[**host_storage_system_attach_scsi_lun**](HostStorageSystemApi.md#host_storage_system_attach_scsi_lun) | **POST** /HostStorageSystem/{moId}/AttachScsiLun | Allow I/O issue to the specified detached ScsiLun. 
[**host_storage_system_attach_scsi_lun_ex_task**](HostStorageSystemApi.md#host_storage_system_attach_scsi_lun_ex_task) | **POST** /HostStorageSystem/{moId}/AttachScsiLunEx_Task | Attach one or more SCSI LUNs. 
[**host_storage_system_attach_vmfs_extent**](HostStorageSystemApi.md#host_storage_system_attach_vmfs_extent) | **POST** /HostStorageSystem/{moId}/AttachVmfsExtent | Extends a VMFS by attaching a disk partition as an extent. 
[**host_storage_system_change_nfs_user_password**](HostStorageSystemApi.md#host_storage_system_change_nfs_user_password) | **POST** /HostStorageSystem/{moId}/ChangeNFSUserPassword | Change password for existing NFS user. 
[**host_storage_system_clear_nfs_user**](HostStorageSystemApi.md#host_storage_system_clear_nfs_user) | **POST** /HostStorageSystem/{moId}/ClearNFSUser | Clear the NFS user configured on the esx host 
[**host_storage_system_compute_disk_partition_info**](HostStorageSystemApi.md#host_storage_system_compute_disk_partition_info) | **POST** /HostStorageSystem/{moId}/ComputeDiskPartitionInfo | Computes the disk partition information given the desired disk layout. 
[**host_storage_system_compute_disk_partition_info_for_resize**](HostStorageSystemApi.md#host_storage_system_compute_disk_partition_info_for_resize) | **POST** /HostStorageSystem/{moId}/ComputeDiskPartitionInfoForResize | Computes the disk partition information for the purpose of resizing a given partition. 
[**host_storage_system_connect_nvme_controller**](HostStorageSystemApi.md#host_storage_system_connect_nvme_controller) | **POST** /HostStorageSystem/{moId}/ConnectNvmeController | Establish a connection to an NVME controller. 
[**host_storage_system_connect_nvme_controller_ex_task**](HostStorageSystemApi.md#host_storage_system_connect_nvme_controller_ex_task) | **POST** /HostStorageSystem/{moId}/ConnectNvmeControllerEx_Task | Establish a connection to one or more NVMe controllers. 
[**host_storage_system_create_nvme_over_rdma_adapter**](HostStorageSystemApi.md#host_storage_system_create_nvme_over_rdma_adapter) | **POST** /HostStorageSystem/{moId}/CreateNvmeOverRdmaAdapter | Creates a software NVME over RDMA adapter. 
[**host_storage_system_create_software_adapter**](HostStorageSystemApi.md#host_storage_system_create_software_adapter) | **POST** /HostStorageSystem/{moId}/CreateSoftwareAdapter | Creates a software host bus adapter based on the provided spec. 
[**host_storage_system_delete_scsi_lun_state**](HostStorageSystemApi.md#host_storage_system_delete_scsi_lun_state) | **POST** /HostStorageSystem/{moId}/DeleteScsiLunState | For previously detached SCSI Lun, remove the state information from host. 
[**host_storage_system_delete_vffs_volume_state**](HostStorageSystemApi.md#host_storage_system_delete_vffs_volume_state) | **POST** /HostStorageSystem/{moId}/DeleteVffsVolumeState | For previously unmounted VFFS volume, remove the state information from host. 
[**host_storage_system_delete_vmfs_volume_state**](HostStorageSystemApi.md#host_storage_system_delete_vmfs_volume_state) | **POST** /HostStorageSystem/{moId}/DeleteVmfsVolumeState | For previously unmounted VMFS volume, remove the state information from host. 
[**host_storage_system_destroy_vffs**](HostStorageSystemApi.md#host_storage_system_destroy_vffs) | **POST** /HostStorageSystem/{moId}/DestroyVffs | Destroy a VFFS volume. 
[**host_storage_system_detach_scsi_lun**](HostStorageSystemApi.md#host_storage_system_detach_scsi_lun) | **POST** /HostStorageSystem/{moId}/DetachScsiLun | Disallow I/O issue to the specified ScsiLun. 
[**host_storage_system_detach_scsi_lun_ex_task**](HostStorageSystemApi.md#host_storage_system_detach_scsi_lun_ex_task) | **POST** /HostStorageSystem/{moId}/DetachScsiLunEx_Task | Detach one or more SCSI LUNs. 
[**host_storage_system_disable_multipath_path**](HostStorageSystemApi.md#host_storage_system_disable_multipath_path) | **POST** /HostStorageSystem/{moId}/DisableMultipathPath | Disables an enabled path for a Logical Unit. 
[**host_storage_system_disconnect_nvme_controller**](HostStorageSystemApi.md#host_storage_system_disconnect_nvme_controller) | **POST** /HostStorageSystem/{moId}/DisconnectNvmeController | Disconnect from an NVME controller. 
[**host_storage_system_disconnect_nvme_controller_ex_task**](HostStorageSystemApi.md#host_storage_system_disconnect_nvme_controller_ex_task) | **POST** /HostStorageSystem/{moId}/DisconnectNvmeControllerEx_Task | Disconnect from one or more NVMe controllers. 
[**host_storage_system_discover_fcoe_hbas**](HostStorageSystemApi.md#host_storage_system_discover_fcoe_hbas) | **POST** /HostStorageSystem/{moId}/DiscoverFcoeHbas | Initiates FCoE discovery using the given FcoeSpecification. 
[**host_storage_system_discover_nvme_controllers**](HostStorageSystemApi.md#host_storage_system_discover_nvme_controllers) | **POST** /HostStorageSystem/{moId}/DiscoverNvmeControllers | Connects to a Discovery Controller and retrieves the Discovery Log using the provided NvmeDiscoverSpec. 
[**host_storage_system_enable_multipath_path**](HostStorageSystemApi.md#host_storage_system_enable_multipath_path) | **POST** /HostStorageSystem/{moId}/EnableMultipathPath | Enables a disabled path for a Logical Unit. 
[**host_storage_system_expand_vmfs_extent**](HostStorageSystemApi.md#host_storage_system_expand_vmfs_extent) | **POST** /HostStorageSystem/{moId}/ExpandVmfsExtent | Expands a VMFS extent as specified by the Disk partition specification. 
[**host_storage_system_extend_vffs**](HostStorageSystemApi.md#host_storage_system_extend_vffs) | **POST** /HostStorageSystem/{moId}/ExtendVffs | Extends a VFFS by attaching a SSD. 
[**host_storage_system_format_vffs**](HostStorageSystemApi.md#host_storage_system_format_vffs) | **POST** /HostStorageSystem/{moId}/FormatVffs | Format a new VFFS on a SSD disk 
[**host_storage_system_format_vmfs**](HostStorageSystemApi.md#host_storage_system_format_vmfs) | **POST** /HostStorageSystem/{moId}/FormatVmfs | Formats a new VMFS on a disk partition. 
[**host_storage_system_get_available_field**](HostStorageSystemApi.md#host_storage_system_get_available_field) | **GET** /HostStorageSystem/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**host_storage_system_get_file_system_volume_info**](HostStorageSystemApi.md#host_storage_system_get_file_system_volume_info) | **GET** /HostStorageSystem/{moId}/fileSystemVolumeInfo | File system volume information for the host. 
[**host_storage_system_get_multipath_state_info**](HostStorageSystemApi.md#host_storage_system_get_multipath_state_info) | **GET** /HostStorageSystem/{moId}/multipathStateInfo | Runtime information about the state of a multipath path. 
[**host_storage_system_get_storage_device_info**](HostStorageSystemApi.md#host_storage_system_get_storage_device_info) | **GET** /HostStorageSystem/{moId}/storageDeviceInfo | Host storage information up to the device level. 
[**host_storage_system_get_system_file**](HostStorageSystemApi.md#host_storage_system_get_system_file) | **GET** /HostStorageSystem/{moId}/systemFile | Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. 
[**host_storage_system_get_value**](HostStorageSystemApi.md#host_storage_system_get_value) | **GET** /HostStorageSystem/{moId}/value | List of custom field values. 
[**host_storage_system_mark_as_local_task**](HostStorageSystemApi.md#host_storage_system_mark_as_local_task) | **POST** /HostStorageSystem/{moId}/MarkAsLocal_Task | Mark a disk to local disk, due to the reason that local disks behind some controllers might not be recongized as local correctly. 
[**host_storage_system_mark_as_non_local_task**](HostStorageSystemApi.md#host_storage_system_mark_as_non_local_task) | **POST** /HostStorageSystem/{moId}/MarkAsNonLocal_Task | Mark a disk to remote disk, which is the opposite operation of *HostStorageSystem.MarkAsLocal_Task* Task failure might lose existing claim rules on the disk. 
[**host_storage_system_mark_as_non_ssd_task**](HostStorageSystemApi.md#host_storage_system_mark_as_non_ssd_task) | **POST** /HostStorageSystem/{moId}/MarkAsNonSsd_Task | Mark a disk to Non-SSD, which is the opposite operation of *HostStorageSystem.MarkAsSsd_Task* Task failure might lose existing claim rules on the disk. 
[**host_storage_system_mark_as_ssd_task**](HostStorageSystemApi.md#host_storage_system_mark_as_ssd_task) | **POST** /HostStorageSystem/{moId}/MarkAsSsd_Task | Mark a disk to SSD, due to the reason that SSDs behind some controllers might not be recongized as SSD correctly. 
[**host_storage_system_mark_for_removal**](HostStorageSystemApi.md#host_storage_system_mark_for_removal) | **POST** /HostStorageSystem/{moId}/MarkForRemoval | Mark or unmark the given FCoE HBA for removal from the host system. 
[**host_storage_system_mark_perennially_reserved**](HostStorageSystemApi.md#host_storage_system_mark_perennially_reserved) | **POST** /HostStorageSystem/{moId}/MarkPerenniallyReserved | Marks the specified LUN as perennially reserved. 
[**host_storage_system_mark_perennially_reserved_ex_task**](HostStorageSystemApi.md#host_storage_system_mark_perennially_reserved_ex_task) | **POST** /HostStorageSystem/{moId}/MarkPerenniallyReservedEx_Task | Marks the specified one or more SCSI LUN&#39;s perennially reserved based on the sate. 
[**host_storage_system_mount_vffs_volume**](HostStorageSystemApi.md#host_storage_system_mount_vffs_volume) | **POST** /HostStorageSystem/{moId}/MountVffsVolume | Mount the unmounted VFFS volume. 
[**host_storage_system_mount_vmfs_volume**](HostStorageSystemApi.md#host_storage_system_mount_vmfs_volume) | **POST** /HostStorageSystem/{moId}/MountVmfsVolume | Mount the unmounted Vmfs volume. 
[**host_storage_system_mount_vmfs_volume_ex_task**](HostStorageSystemApi.md#host_storage_system_mount_vmfs_volume_ex_task) | **POST** /HostStorageSystem/{moId}/MountVmfsVolumeEx_Task | Mount one or more VMFS volumes. 
[**host_storage_system_query_available_ssds**](HostStorageSystemApi.md#host_storage_system_query_available_ssds) | **POST** /HostStorageSystem/{moId}/QueryAvailableSsds | Query the list SSD disks that can be used to contain a VFFS volume. 
[**host_storage_system_query_nfs_user**](HostStorageSystemApi.md#host_storage_system_query_nfs_user) | **POST** /HostStorageSystem/{moId}/QueryNFSUser | Query the NFS user configured on the esx host 
[**host_storage_system_query_path_selection_policy_options**](HostStorageSystemApi.md#host_storage_system_query_path_selection_policy_options) | **POST** /HostStorageSystem/{moId}/QueryPathSelectionPolicyOptions | Queries the set of path selection policy options. 
[**host_storage_system_query_storage_array_type_policy_options**](HostStorageSystemApi.md#host_storage_system_query_storage_array_type_policy_options) | **POST** /HostStorageSystem/{moId}/QueryStorageArrayTypePolicyOptions | Queries the set of storage array type policy options. 
[**host_storage_system_query_unresolved_vmfs_volume**](HostStorageSystemApi.md#host_storage_system_query_unresolved_vmfs_volume) | **POST** /HostStorageSystem/{moId}/QueryUnresolvedVmfsVolume | Get the list of unbound VMFS volumes. 
[**host_storage_system_query_vmfs_config_option**](HostStorageSystemApi.md#host_storage_system_query_vmfs_config_option) | **POST** /HostStorageSystem/{moId}/QueryVmfsConfigOption | Get the VMFS configuration options, including block size, unmap granularity. 
[**host_storage_system_refresh_storage_system**](HostStorageSystemApi.md#host_storage_system_refresh_storage_system) | **POST** /HostStorageSystem/{moId}/RefreshStorageSystem | Obtains the latest host storage information related to storage devices, topology, and file systems. 
[**host_storage_system_remove_internet_scsi_send_targets**](HostStorageSystemApi.md#host_storage_system_remove_internet_scsi_send_targets) | **POST** /HostStorageSystem/{moId}/RemoveInternetScsiSendTargets | Removes Send Target entries from the host bus adapter discovery list. 
[**host_storage_system_remove_internet_scsi_static_targets**](HostStorageSystemApi.md#host_storage_system_remove_internet_scsi_static_targets) | **POST** /HostStorageSystem/{moId}/RemoveInternetScsiStaticTargets | Removes static target entries from the host bus adapter discovery list. 
[**host_storage_system_remove_nvme_over_rdma_adapter**](HostStorageSystemApi.md#host_storage_system_remove_nvme_over_rdma_adapter) | **POST** /HostStorageSystem/{moId}/RemoveNvmeOverRdmaAdapter | Removes a software NVME over RDMA adapter. 
[**host_storage_system_remove_software_adapter**](HostStorageSystemApi.md#host_storage_system_remove_software_adapter) | **POST** /HostStorageSystem/{moId}/RemoveSoftwareAdapter | Removes a software host bus adapter, if the adapter type allows it. 
[**host_storage_system_rescan_all_hba**](HostStorageSystemApi.md#host_storage_system_rescan_all_hba) | **POST** /HostStorageSystem/{moId}/RescanAllHba | Scans all host bus adapters to obtain the current list of devices and device topology. 
[**host_storage_system_rescan_hba**](HostStorageSystemApi.md#host_storage_system_rescan_hba) | **POST** /HostStorageSystem/{moId}/RescanHba | Issues a request to rescan a specific host bus adapter for new storage devices. 
[**host_storage_system_rescan_vffs**](HostStorageSystemApi.md#host_storage_system_rescan_vffs) | **POST** /HostStorageSystem/{moId}/RescanVffs | Rescans for new VFFS. 
[**host_storage_system_rescan_vmfs**](HostStorageSystemApi.md#host_storage_system_rescan_vmfs) | **POST** /HostStorageSystem/{moId}/RescanVmfs | Rescans for new Virtual Machine File Systems (VMFS). 
[**host_storage_system_resolve_multiple_unresolved_vmfs_volumes**](HostStorageSystemApi.md#host_storage_system_resolve_multiple_unresolved_vmfs_volumes) | **POST** /HostStorageSystem/{moId}/ResolveMultipleUnresolvedVmfsVolumes | Resignature or &#39;Force Mount&#39; list of unbound VMFS volumes. 
[**host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task**](HostStorageSystemApi.md#host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task) | **POST** /HostStorageSystem/{moId}/ResolveMultipleUnresolvedVmfsVolumesEx_Task | Resignature or &#39;Force Mount&#39; list of unbound VMFS volumes. 
[**host_storage_system_retrieve_disk_partition_info**](HostStorageSystemApi.md#host_storage_system_retrieve_disk_partition_info) | **POST** /HostStorageSystem/{moId}/RetrieveDiskPartitionInfo | Gets the partition information for the disks named by the device names. 
[**host_storage_system_set_custom_value**](HostStorageSystemApi.md#host_storage_system_set_custom_value) | **POST** /HostStorageSystem/{moId}/setCustomValue | Assigns a value to a custom field. 
[**host_storage_system_set_multipath_lun_policy**](HostStorageSystemApi.md#host_storage_system_set_multipath_lun_policy) | **POST** /HostStorageSystem/{moId}/SetMultipathLunPolicy | Updates the path selection policy for a Logical Unit. 
[**host_storage_system_set_nfs_user**](HostStorageSystemApi.md#host_storage_system_set_nfs_user) | **POST** /HostStorageSystem/{moId}/SetNFSUser | Set NFS username and password on the host. 
[**host_storage_system_turn_disk_locator_led_off_task**](HostStorageSystemApi.md#host_storage_system_turn_disk_locator_led_off_task) | **POST** /HostStorageSystem/{moId}/TurnDiskLocatorLedOff_Task | Turn off one or more disk locator LEDs. 
[**host_storage_system_turn_disk_locator_led_on_task**](HostStorageSystemApi.md#host_storage_system_turn_disk_locator_led_on_task) | **POST** /HostStorageSystem/{moId}/TurnDiskLocatorLedOn_Task | Turn on one or more disk locator LEDs, duration is the maximum that hardware can support. 
[**host_storage_system_unmap_vmfs_volume_ex_task**](HostStorageSystemApi.md#host_storage_system_unmap_vmfs_volume_ex_task) | **POST** /HostStorageSystem/{moId}/UnmapVmfsVolumeEx_Task | Unmap one or more VMFS volumes. 
[**host_storage_system_unmount_force_mounted_vmfs_volume**](HostStorageSystemApi.md#host_storage_system_unmount_force_mounted_vmfs_volume) | **POST** /HostStorageSystem/{moId}/UnmountForceMountedVmfsVolume | Unmount the &#39;forceMounted&#39; Vmfs volume. 
[**host_storage_system_unmount_vffs_volume**](HostStorageSystemApi.md#host_storage_system_unmount_vffs_volume) | **POST** /HostStorageSystem/{moId}/UnmountVffsVolume | Unmount the VFFS volume. 
[**host_storage_system_unmount_vmfs_volume**](HostStorageSystemApi.md#host_storage_system_unmount_vmfs_volume) | **POST** /HostStorageSystem/{moId}/UnmountVmfsVolume | Unmount the Vmfs volume. 
[**host_storage_system_unmount_vmfs_volume_ex_task**](HostStorageSystemApi.md#host_storage_system_unmount_vmfs_volume_ex_task) | **POST** /HostStorageSystem/{moId}/UnmountVmfsVolumeEx_Task | Unmount one or more VMFS volumes. 
[**host_storage_system_update_disk_partitions**](HostStorageSystemApi.md#host_storage_system_update_disk_partitions) | **POST** /HostStorageSystem/{moId}/UpdateDiskPartitions | Changes the partitions on the disk by supplying a partition specification and the device name. 
[**host_storage_system_update_hpp_multipath_lun_policy**](HostStorageSystemApi.md#host_storage_system_update_hpp_multipath_lun_policy) | **POST** /HostStorageSystem/{moId}/UpdateHppMultipathLunPolicy | Updates the path selection policy for a HPP claimed Logical Unit. 
[**host_storage_system_update_internet_scsi_advanced_options**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_advanced_options) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiAdvancedOptions | Updates the advanced options the iSCSI host bus adapter or the discovery addresses and targets associated with it. 
[**host_storage_system_update_internet_scsi_alias**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_alias) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiAlias | Updates the alias of an iSCSI host bus adapter. 
[**host_storage_system_update_internet_scsi_authentication_properties**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_authentication_properties) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiAuthenticationProperties | Updates the authentication properties for one or more targets or discovery addresses associated with an iSCSI host bus adapter. 
[**host_storage_system_update_internet_scsi_digest_properties**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_digest_properties) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiDigestProperties | Updates the digest properties for the iSCSI host bus adapter or the discovery addresses and targets associated with it. 
[**host_storage_system_update_internet_scsi_discovery_properties**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_discovery_properties) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiDiscoveryProperties | Updates the Discovery properties for an iSCSI host bus adapter. 
[**host_storage_system_update_internet_scsi_ip_properties**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_ip_properties) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiIPProperties | Updates the IP properties for an iSCSI host bus adapter. 
[**host_storage_system_update_internet_scsi_name**](HostStorageSystemApi.md#host_storage_system_update_internet_scsi_name) | **POST** /HostStorageSystem/{moId}/UpdateInternetScsiName | Updates the name of an iSCSI host bus adapter. 
[**host_storage_system_update_scsi_lun_display_name**](HostStorageSystemApi.md#host_storage_system_update_scsi_lun_display_name) | **POST** /HostStorageSystem/{moId}/UpdateScsiLunDisplayName | Update the mutable display name associated with a ScsiLun. 
[**host_storage_system_update_software_internet_scsi_enabled**](HostStorageSystemApi.md#host_storage_system_update_software_internet_scsi_enabled) | **POST** /HostStorageSystem/{moId}/UpdateSoftwareInternetScsiEnabled | Enables or disables Software iSCSI. 
[**host_storage_system_update_vmfs_unmap_bandwidth**](HostStorageSystemApi.md#host_storage_system_update_vmfs_unmap_bandwidth) | **POST** /HostStorageSystem/{moId}/UpdateVmfsUnmapBandwidth | Update VMFS unmap bandwidth. 
[**host_storage_system_update_vmfs_unmap_priority**](HostStorageSystemApi.md#host_storage_system_update_vmfs_unmap_priority) | **POST** /HostStorageSystem/{moId}/UpdateVmfsUnmapPriority | Update VMFS unmap priority. 
[**host_storage_system_upgrade_vm_layout**](HostStorageSystemApi.md#host_storage_system_upgrade_vm_layout) | **POST** /HostStorageSystem/{moId}/UpgradeVmLayout | Iterates over all registered virtual machines. 
[**host_storage_system_upgrade_vmfs**](HostStorageSystemApi.md#host_storage_system_upgrade_vmfs) | **POST** /HostStorageSystem/{moId}/UpgradeVmfs | Upgrades the VMFS to the *latest supported VMFS version*. 


# **host_storage_system_add_internet_scsi_send_targets**
> host_storage_system_add_internet_scsi_send_targets(mo_id, add_internet_scsi_send_targets_request_type)

Adds Send Target entries to the host bus adapter discovery list. 

Adds Send Target entries to the host bus adapter discovery list.  The DiscoveryProperties.sendTargetsDiscoveryEnabled flag must be set to true.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_internet_scsi_send_targets_request_type import AddInternetScsiSendTargetsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_internet_scsi_send_targets_request_type = vmware_vi.AddInternetScsiSendTargetsRequestType() # AddInternetScsiSendTargetsRequestType | 

    try:
        # Adds Send Target entries to the host bus adapter discovery list. 
        api_instance.host_storage_system_add_internet_scsi_send_targets(mo_id, add_internet_scsi_send_targets_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_add_internet_scsi_send_targets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_internet_scsi_send_targets_request_type** | [**AddInternetScsiSendTargetsRequestType**](AddInternetScsiSendTargetsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: for all other configuration failures.  ***NotFound***: if the discovery list could not be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_add_internet_scsi_static_targets**
> host_storage_system_add_internet_scsi_static_targets(mo_id, add_internet_scsi_static_targets_request_type)

Adds Static Target entries to the host bus adapter discovery list. 

Adds Static Target entries to the host bus adapter discovery list.  The DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.add_internet_scsi_static_targets_request_type import AddInternetScsiStaticTargetsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    add_internet_scsi_static_targets_request_type = vmware_vi.AddInternetScsiStaticTargetsRequestType() # AddInternetScsiStaticTargetsRequestType | 

    try:
        # Adds Static Target entries to the host bus adapter discovery list. 
        api_instance.host_storage_system_add_internet_scsi_static_targets(mo_id, add_internet_scsi_static_targets_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_add_internet_scsi_static_targets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **add_internet_scsi_static_targets_request_type** | [**AddInternetScsiStaticTargetsRequestType**](AddInternetScsiStaticTargetsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adaptor discovery list was not found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_attach_scsi_lun**
> host_storage_system_attach_scsi_lun(mo_id, attach_scsi_lun_request_type)

Allow I/O issue to the specified detached ScsiLun. 

Allow I/O issue to the specified detached ScsiLun.  The ScsiLun is administratively configured on, if the attach operation is successful. See *HostStorageSystem.DetachScsiLun*.  attachScsiLun is part of the Unmount, Detach workflow used when a device will be permanently removed. See also *HostStorageSystem.UnmountVmfsVolume*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.attach_scsi_lun_request_type import AttachScsiLunRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    attach_scsi_lun_request_type = vmware_vi.AttachScsiLunRequestType() # AttachScsiLunRequestType | 

    try:
        # Allow I/O issue to the specified detached ScsiLun. 
        api_instance.host_storage_system_attach_scsi_lun(mo_id, attach_scsi_lun_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_attach_scsi_lun: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **attach_scsi_lun_request_type** | [**AttachScsiLunRequestType**](AttachScsiLunRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidState***: if - The device is already attached.   i.e. Device state is not &#39;off&#39; in *ScsiLun.operationalState*. - The device is unreachable. See *ScsiLun.operationalState*.    ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_attach_scsi_lun_ex_task**
> ManagedObjectReference host_storage_system_attach_scsi_lun_ex_task(mo_id, attach_scsi_lun_ex_request_type)

Attach one or more SCSI LUNs. 

Attach one or more SCSI LUNs.  This is an asynchronous, batch operation of attachScisLun. Please see *HostStorageSystem.AttachScsiLun* for operational details.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.attach_scsi_lun_ex_request_type import AttachScsiLunExRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    attach_scsi_lun_ex_request_type = vmware_vi.AttachScsiLunExRequestType() # AttachScsiLunExRequestType | 

    try:
        # Attach one or more SCSI LUNs. 
        api_response = api_instance.host_storage_system_attach_scsi_lun_ex_task(mo_id, attach_scsi_lun_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_attach_scsi_lun_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_attach_scsi_lun_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **attach_scsi_lun_ex_request_type** | [**AttachScsiLunExRequestType**](AttachScsiLunExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_attach_vmfs_extent**
> host_storage_system_attach_vmfs_extent(mo_id, attach_vmfs_extent_request_type)

Extends a VMFS by attaching a disk partition as an extent. 

Extends a VMFS by attaching a disk partition as an extent.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.attach_vmfs_extent_request_type import AttachVmfsExtentRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    attach_vmfs_extent_request_type = vmware_vi.AttachVmfsExtentRequestType() # AttachVmfsExtentRequestType | 

    try:
        # Extends a VMFS by attaching a disk partition as an extent. 
        api_instance.host_storage_system_attach_vmfs_extent(mo_id, attach_vmfs_extent_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_attach_vmfs_extent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **attach_vmfs_extent_request_type** | [**AttachVmfsExtentRequestType**](AttachVmfsExtentRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the VMFS cannot be found or is unmounted.  ***InvalidArgument***: if the new extent is already used by another vmfs volume, does not exist, or is of an invalid partition type.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_change_nfs_user_password**
> host_storage_system_change_nfs_user_password(mo_id, change_nfs_user_password_request_type)

Change password for existing NFS user. 

Change password for existing NFS user.  This method shall be called after the NFS user has been created on the host.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.change_nfs_user_password_request_type import ChangeNFSUserPasswordRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    change_nfs_user_password_request_type = vmware_vi.ChangeNFSUserPasswordRequestType() # ChangeNFSUserPasswordRequestType | 

    try:
        # Change password for existing NFS user. 
        api_instance.host_storage_system_change_nfs_user_password(mo_id, change_nfs_user_password_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_change_nfs_user_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **change_nfs_user_password_request_type** | [**ChangeNFSUserPasswordRequestType**](ChangeNFSUserPasswordRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: NFS user is not set.  ***HostConfigFault***: Unable to set passwords due to host configuration problem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_clear_nfs_user**
> host_storage_system_clear_nfs_user(mo_id)

Clear the NFS user configured on the esx host 

Clear the NFS user configured on the esx host  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Clear the NFS user configured on the esx host 
        api_instance.host_storage_system_clear_nfs_user(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_clear_nfs_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: Unable to clear NFS user due to host configuration problem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_compute_disk_partition_info**
> HostDiskPartitionInfo host_storage_system_compute_disk_partition_info(mo_id, compute_disk_partition_info_request_type)

Computes the disk partition information given the desired disk layout. 

Computes the disk partition information given the desired disk layout.  The server computes a new partition information object for a specific disk representing the desired layout.  See also *HostDiskPartitionInfoPartitionFormat_enum*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.compute_disk_partition_info_request_type import ComputeDiskPartitionInfoRequestType
from vmware_vi.models.host_disk_partition_info import HostDiskPartitionInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    compute_disk_partition_info_request_type = vmware_vi.ComputeDiskPartitionInfoRequestType() # ComputeDiskPartitionInfoRequestType | 

    try:
        # Computes the disk partition information given the desired disk layout. 
        api_response = api_instance.host_storage_system_compute_disk_partition_info(mo_id, compute_disk_partition_info_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_compute_disk_partition_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_compute_disk_partition_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **compute_disk_partition_info_request_type** | [**ComputeDiskPartitionInfoRequestType**](ComputeDiskPartitionInfoRequestType.md)|  | 

### Return type

[**HostDiskPartitionInfo**](HostDiskPartitionInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data object that contains information about the partitions on a disk  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidArgument***: if the layout is invalid.  ***HostConfigFault***: if unable to get the current partition information for the device.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_compute_disk_partition_info_for_resize**
> HostDiskPartitionInfo host_storage_system_compute_disk_partition_info_for_resize(mo_id, compute_disk_partition_info_for_resize_request_type)

Computes the disk partition information for the purpose of resizing a given partition. 

Computes the disk partition information for the purpose of resizing a given partition.  See also *HostDiskPartitionInfoPartitionFormat_enum*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.compute_disk_partition_info_for_resize_request_type import ComputeDiskPartitionInfoForResizeRequestType
from vmware_vi.models.host_disk_partition_info import HostDiskPartitionInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    compute_disk_partition_info_for_resize_request_type = vmware_vi.ComputeDiskPartitionInfoForResizeRequestType() # ComputeDiskPartitionInfoForResizeRequestType | 

    try:
        # Computes the disk partition information for the purpose of resizing a given partition. 
        api_response = api_instance.host_storage_system_compute_disk_partition_info_for_resize(mo_id, compute_disk_partition_info_for_resize_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_compute_disk_partition_info_for_resize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_compute_disk_partition_info_for_resize: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **compute_disk_partition_info_for_resize_request_type** | [**ComputeDiskPartitionInfoForResizeRequestType**](ComputeDiskPartitionInfoForResizeRequestType.md)|  | 

### Return type

[**HostDiskPartitionInfo**](HostDiskPartitionInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resized disk partition information  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidArgument***: if blockRange or partition is invalid.  ***HostConfigFault***: if unable to get the current partition information for the device.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_connect_nvme_controller**
> host_storage_system_connect_nvme_controller(mo_id, connect_nvme_controller_request_type)

Establish a connection to an NVME controller. 

Establish a connection to an NVME controller.  As a result, all the namespaces attached to the controller will be accessible through the adapter. For more details, see: - \"NVM Express over Fabrics 1.0\", Section 3.3,   \"Connect command and response\"    ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.connect_nvme_controller_request_type import ConnectNvmeControllerRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    connect_nvme_controller_request_type = vmware_vi.ConnectNvmeControllerRequestType() # ConnectNvmeControllerRequestType | 

    try:
        # Establish a connection to an NVME controller. 
        api_instance.host_storage_system_connect_nvme_controller(mo_id, connect_nvme_controller_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_connect_nvme_controller: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **connect_nvme_controller_request_type** | [**ConnectNvmeControllerRequestType**](ConnectNvmeControllerRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the given HBA or transport target could not be found.  ***InvalidArgument***: if the provided spec is not valid.  ***NotSupported***: if the adapter does not support the provided combination of parameters.  ***HostConfigFault***: if the host is unable to establish the connection.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_connect_nvme_controller_ex_task**
> ManagedObjectReference host_storage_system_connect_nvme_controller_ex_task(mo_id, connect_nvme_controller_ex_request_type)

Establish a connection to one or more NVMe controllers. 

Establish a connection to one or more NVMe controllers.  This is an asynchronous, batch version of the connectNvmeController API. See *HostStorageSystem.ConnectNvmeController* for details. If supported on the host in question, *HostCapability.nvmeBatchOperationsSupported* will be set to true. An attempt will be made to establish a connection using each of the provided specifications. There are no transactional guarantees - some of the connections may succeed and some may fail. In case of any failures, a fault containing information about the failed attempts to establish a connection will be thrown.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.connect_nvme_controller_ex_request_type import ConnectNvmeControllerExRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    connect_nvme_controller_ex_request_type = vmware_vi.ConnectNvmeControllerExRequestType() # ConnectNvmeControllerExRequestType | 

    try:
        # Establish a connection to one or more NVMe controllers. 
        api_response = api_instance.host_storage_system_connect_nvme_controller_ex_task(mo_id, connect_nvme_controller_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_connect_nvme_controller_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_connect_nvme_controller_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **connect_nvme_controller_ex_request_type** | [**ConnectNvmeControllerExRequestType**](ConnectNvmeControllerExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if the batch API is not supported on the host in question.  ***HostConfigFault***: if any of the attempted connections failed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_create_nvme_over_rdma_adapter**
> host_storage_system_create_nvme_over_rdma_adapter(mo_id, create_nvme_over_rdma_adapter_request_type)

Creates a software NVME over RDMA adapter. 

Creates a software NVME over RDMA adapter.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_nvme_over_rdma_adapter_request_type import CreateNvmeOverRdmaAdapterRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_nvme_over_rdma_adapter_request_type = vmware_vi.CreateNvmeOverRdmaAdapterRequestType() # CreateNvmeOverRdmaAdapterRequestType | 

    try:
        # Creates a software NVME over RDMA adapter. 
        api_instance.host_storage_system_create_nvme_over_rdma_adapter(mo_id, create_nvme_over_rdma_adapter_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_create_nvme_over_rdma_adapter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_nvme_over_rdma_adapter_request_type** | [**CreateNvmeOverRdmaAdapterRequestType**](CreateNvmeOverRdmaAdapterRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***ResourceInUse***: if the RDMA device is already in use by an NVME over RDMA adapter.  ***NotFound***: if the given RDMA device could not be found.  ***NotSupported***: if the current configuration of the RDMA device does not permit the creation of the adapter.  ***HostConfigFault***: if the host is unable to create the adapter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_create_software_adapter**
> host_storage_system_create_software_adapter(mo_id, create_software_adapter_request_type)

Creates a software host bus adapter based on the provided spec. 

Creates a software host bus adapter based on the provided spec.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_software_adapter_request_type import CreateSoftwareAdapterRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_software_adapter_request_type = vmware_vi.CreateSoftwareAdapterRequestType() # CreateSoftwareAdapterRequestType | 

    try:
        # Creates a software host bus adapter based on the provided spec. 
        api_instance.host_storage_system_create_software_adapter(mo_id, create_software_adapter_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_create_software_adapter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_software_adapter_request_type** | [**CreateSoftwareAdapterRequestType**](CreateSoftwareAdapterRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***ResourceInUse***: if some of the resources specified in the spec and needed for adapter creation is in use  ***NotFound***: if any of the resources specified in the spec could not be found.  ***NotSupported***: if the configuration requested by the spec is not supported.  ***HostConfigFault***: if the host is unable to create the adapter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_delete_scsi_lun_state**
> host_storage_system_delete_scsi_lun_state(mo_id, delete_scsi_lun_state_request_type)

For previously detached SCSI Lun, remove the state information from host. 

For previously detached SCSI Lun, remove the state information from host.  Detach SCSI Lun marks the device where I/Os are not allowed. Host still maintains the entry of this device and its state. If a LUN is detached using detachScsiLun, ESX will not automatically attach this LUN durng a rescan or after a reboot. See *HostStorageSystem.DetachScsiLun*. Please note: The API takes 'canonicalName' of the ScsiLun object instead of the ScsiLun.uuid.  See also *ScsiLun.canonicalName*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_scsi_lun_state_request_type import DeleteScsiLunStateRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_scsi_lun_state_request_type = vmware_vi.DeleteScsiLunStateRequestType() # DeleteScsiLunStateRequestType | 

    try:
        # For previously detached SCSI Lun, remove the state information from host. 
        api_instance.host_storage_system_delete_scsi_lun_state(mo_id, delete_scsi_lun_state_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_delete_scsi_lun_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_scsi_lun_state_request_type** | [**DeleteScsiLunStateRequestType**](DeleteScsiLunStateRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: for any configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_delete_vffs_volume_state**
> host_storage_system_delete_vffs_volume_state(mo_id, delete_vffs_volume_state_request_type)

For previously unmounted VFFS volume, remove the state information from host. 

For previously unmounted VFFS volume, remove the state information from host.  VFFS volumes mount state is maintained by host.  deleteVffsVolumeState is part of the Unmount/Detach workflow used when the device will be permanently removed. See also *HostStorageSystem.UnmountVffsVolume*. If the VFFS volume is unmounted using unmountVffsVolume, ESX maintains the state of VFFS volume. This API will remove the state from the host. If the underlying storage device is going to be un-provisioned on the array side, please detach the storage device. See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_vffs_volume_state_request_type import DeleteVffsVolumeStateRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_vffs_volume_state_request_type = vmware_vi.DeleteVffsVolumeStateRequestType() # DeleteVffsVolumeStateRequestType | 

    try:
        # For previously unmounted VFFS volume, remove the state information from host. 
        api_instance.host_storage_system_delete_vffs_volume_state(mo_id, delete_vffs_volume_state_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_delete_vffs_volume_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_vffs_volume_state_request_type** | [**DeleteVffsVolumeStateRequestType**](DeleteVffsVolumeStateRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: for any configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_delete_vmfs_volume_state**
> host_storage_system_delete_vmfs_volume_state(mo_id, delete_vmfs_volume_state_request_type)

For previously unmounted VMFS volume, remove the state information from host. 

For previously unmounted VMFS volume, remove the state information from host.  VMFS volumes mount state is maintained by host.  deleteVmfsVolumeState is part of the Unmount/Detach workflow used when the device will be permanently removed. See also *HostStorageSystem.UnmountVmfsVolume*. If the VMFS volume is unmounted using unmountVmfsVolume, ESX maintains the state of VMFS volume. This API will remove the state from the host. If the underlying storage device is going to be un-provisioned on the array side, please detach the storage device. See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.delete_vmfs_volume_state_request_type import DeleteVmfsVolumeStateRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    delete_vmfs_volume_state_request_type = vmware_vi.DeleteVmfsVolumeStateRequestType() # DeleteVmfsVolumeStateRequestType | 

    try:
        # For previously unmounted VMFS volume, remove the state information from host. 
        api_instance.host_storage_system_delete_vmfs_volume_state(mo_id, delete_vmfs_volume_state_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_delete_vmfs_volume_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **delete_vmfs_volume_state_request_type** | [**DeleteVmfsVolumeStateRequestType**](DeleteVmfsVolumeStateRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: for any configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_destroy_vffs**
> host_storage_system_destroy_vffs(mo_id, destroy_vffs_request_type)

Destroy a VFFS volume. 

Destroy a VFFS volume.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.destroy_vffs_request_type import DestroyVffsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    destroy_vffs_request_type = vmware_vi.DestroyVffsRequestType() # DestroyVffsRequestType | 

    try:
        # Destroy a VFFS volume. 
        api_instance.host_storage_system_destroy_vffs(mo_id, destroy_vffs_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_destroy_vffs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **destroy_vffs_request_type** | [**DestroyVffsRequestType**](DestroyVffsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the VFFS cannot be found or is unmounted.  ***HostConfigFault***: for all other configuration failures.  ***ResourceInUse***: VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_detach_scsi_lun**
> host_storage_system_detach_scsi_lun(mo_id, detach_scsi_lun_request_type)

Disallow I/O issue to the specified ScsiLun. 

Disallow I/O issue to the specified ScsiLun.  The ScsiLun is detached, i.e. administratively configured off until a subsequent attachScsiLun is performed, if the operation is successful. See *HostStorageSystem.AttachScsiLun*.  detachScsiLun is part of the Unmount / Detach workflow used when a device will be permanently removed. See also *HostStorageSystem.UnmountVmfsVolume*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.detach_scsi_lun_request_type import DetachScsiLunRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    detach_scsi_lun_request_type = vmware_vi.DetachScsiLunRequestType() # DetachScsiLunRequestType | 

    try:
        # Disallow I/O issue to the specified ScsiLun. 
        api_instance.host_storage_system_detach_scsi_lun(mo_id, detach_scsi_lun_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_detach_scsi_lun: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **detach_scsi_lun_request_type** | [**DetachScsiLunRequestType**](DetachScsiLunRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidState***: if - The device is already detached(turned &#39;off&#39;).   See *ScsiLun.operationalState*.    ***ResourceInUse***: if - This device is backing a Vm with a Raw Device Mapped Virtual   Disk. - 1 or more programs have I/O outstanding on this device. - 1 or more mounted vmfs volumes have extents residing on this   device. - The device is configured for use by the host e.g. diagnostic   partition is configured on this device.    ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_detach_scsi_lun_ex_task**
> ManagedObjectReference host_storage_system_detach_scsi_lun_ex_task(mo_id, detach_scsi_lun_ex_request_type)

Detach one or more SCSI LUNs. 

Detach one or more SCSI LUNs.  This is an asynchronous, batch operation of detachScisLun. Please see *HostStorageSystem.DetachScsiLun* for operational details.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.detach_scsi_lun_ex_request_type import DetachScsiLunExRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    detach_scsi_lun_ex_request_type = vmware_vi.DetachScsiLunExRequestType() # DetachScsiLunExRequestType | 

    try:
        # Detach one or more SCSI LUNs. 
        api_response = api_instance.host_storage_system_detach_scsi_lun_ex_task(mo_id, detach_scsi_lun_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_detach_scsi_lun_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_detach_scsi_lun_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **detach_scsi_lun_ex_request_type** | [**DetachScsiLunExRequestType**](DetachScsiLunExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_disable_multipath_path**
> host_storage_system_disable_multipath_path(mo_id, disable_multipath_path_request_type)

Disables an enabled path for a Logical Unit. 

Disables an enabled path for a Logical Unit.  Use the path name from *HostMultipathStateInfoPath* or *HostMultipathInfoPath*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disable_multipath_path_request_type import DisableMultipathPathRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disable_multipath_path_request_type = vmware_vi.DisableMultipathPathRequestType() # DisableMultipathPathRequestType | 

    try:
        # Disables an enabled path for a Logical Unit. 
        api_instance.host_storage_system_disable_multipath_path(mo_id, disable_multipath_path_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_disable_multipath_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disable_multipath_path_request_type** | [**DisableMultipathPathRequestType**](DisableMultipathPathRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the LUN could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_disconnect_nvme_controller**
> host_storage_system_disconnect_nvme_controller(mo_id, disconnect_nvme_controller_request_type)

Disconnect from an NVME controller. 

Disconnect from an NVME controller.  As a result, all the namespaces attached to the controller will no longer be accessible through the adapter.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disconnect_nvme_controller_request_type import DisconnectNvmeControllerRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disconnect_nvme_controller_request_type = vmware_vi.DisconnectNvmeControllerRequestType() # DisconnectNvmeControllerRequestType | 

    try:
        # Disconnect from an NVME controller. 
        api_instance.host_storage_system_disconnect_nvme_controller(mo_id, disconnect_nvme_controller_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_disconnect_nvme_controller: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disconnect_nvme_controller_request_type** | [**DisconnectNvmeControllerRequestType**](DisconnectNvmeControllerRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the given HBA or controller could not be found.  ***InvalidArgument***: if the provided spec is not valid.  ***NotSupported***: if the adapter does not support the provided combination of parameters.  ***HostConfigFault***: if the host is unable to perform the disconnect.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_disconnect_nvme_controller_ex_task**
> ManagedObjectReference host_storage_system_disconnect_nvme_controller_ex_task(mo_id, disconnect_nvme_controller_ex_request_type)

Disconnect from one or more NVMe controllers. 

Disconnect from one or more NVMe controllers.  This is an asynchronous, batch version of the disconnectNvmeController API. See *HostStorageSystem.DisconnectNvmeController* for details. If supported on the host in question, *HostCapability.nvmeBatchOperationsSupported* will be set to true. An attempt will be made to disconnect a controller using each of the provided specifications. There are no transactional guarantees - some of the disconnections may succeed and some may fail. In case of any failures, a fault containing information about the failed attempts to disconnect a controller will be thrown.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disconnect_nvme_controller_ex_request_type import DisconnectNvmeControllerExRequestType
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disconnect_nvme_controller_ex_request_type = vmware_vi.DisconnectNvmeControllerExRequestType() # DisconnectNvmeControllerExRequestType | 

    try:
        # Disconnect from one or more NVMe controllers. 
        api_response = api_instance.host_storage_system_disconnect_nvme_controller_ex_task(mo_id, disconnect_nvme_controller_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_disconnect_nvme_controller_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_disconnect_nvme_controller_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disconnect_nvme_controller_ex_request_type** | [**DisconnectNvmeControllerExRequestType**](DisconnectNvmeControllerExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if the batch API is not supported on the host in question.  ***HostConfigFault***: if any of the attempts to disconnect a controller fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_discover_fcoe_hbas**
> host_storage_system_discover_fcoe_hbas(mo_id, discover_fcoe_hbas_request_type)

Initiates FCoE discovery using the given FcoeSpecification. 

Deprecated as of vSphere API 8.0. Software FCoE not supported.  Initiates FCoE discovery using the given FcoeSpecification.  Upon success, discovered VNPorts will have registered with the system as FCoE HBAs.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.discover_fcoe_hbas_request_type import DiscoverFcoeHbasRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    discover_fcoe_hbas_request_type = vmware_vi.DiscoverFcoeHbasRequestType() # DiscoverFcoeHbasRequestType | 

    try:
        # Initiates FCoE discovery using the given FcoeSpecification. 
        api_instance.host_storage_system_discover_fcoe_hbas(mo_id, discover_fcoe_hbas_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_discover_fcoe_hbas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **discover_fcoe_hbas_request_type** | [**DiscoverFcoeHbasRequestType**](DiscoverFcoeHbasRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***InvalidArgument***: if any parameter in the given FcoeSpecification is invalid.  ***HostConfigFault***: if the host is unable to issue FCoE discovery.  ***NotFound***: if the given HBA could not be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_discover_nvme_controllers**
> HostNvmeDiscoveryLog host_storage_system_discover_nvme_controllers(mo_id, discover_nvme_controllers_request_type)

Connects to a Discovery Controller and retrieves the Discovery Log using the provided NvmeDiscoverSpec. 

Connects to a Discovery Controller and retrieves the Discovery Log using the provided NvmeDiscoverSpec.  For more details, see: - \"NVM Express over Fabrics 1.0\", Section 5, \"Discovery service\"    ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.discover_nvme_controllers_request_type import DiscoverNvmeControllersRequestType
from vmware_vi.models.host_nvme_discovery_log import HostNvmeDiscoveryLog
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    discover_nvme_controllers_request_type = vmware_vi.DiscoverNvmeControllersRequestType() # DiscoverNvmeControllersRequestType | 

    try:
        # Connects to a Discovery Controller and retrieves the Discovery Log using the provided NvmeDiscoverSpec. 
        api_response = api_instance.host_storage_system_discover_nvme_controllers(mo_id, discover_nvme_controllers_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_discover_nvme_controllers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_discover_nvme_controllers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **discover_nvme_controllers_request_type** | [**DiscoverNvmeControllersRequestType**](DiscoverNvmeControllersRequestType.md)|  | 

### Return type

[**HostNvmeDiscoveryLog**](HostNvmeDiscoveryLog.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | discoveryLog A data object that represents the Discovery Log.  |  -  |
**500** | ***NotFound***: if the given HBA or transport target could not be found.  ***InvalidArgument***: if the provided spec is not valid.  ***NotSupported***: if the adapter does not support the provided combination of parameters.  ***HostConfigFault***: if the host is unable to retrieve the discovery log.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_enable_multipath_path**
> host_storage_system_enable_multipath_path(mo_id, enable_multipath_path_request_type)

Enables a disabled path for a Logical Unit. 

Enables a disabled path for a Logical Unit.  Use the path name from *HostMultipathStateInfoPath* or *HostMultipathInfoPath*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_multipath_path_request_type import EnableMultipathPathRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_multipath_path_request_type = vmware_vi.EnableMultipathPathRequestType() # EnableMultipathPathRequestType | 

    try:
        # Enables a disabled path for a Logical Unit. 
        api_instance.host_storage_system_enable_multipath_path(mo_id, enable_multipath_path_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_enable_multipath_path: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_multipath_path_request_type** | [**EnableMultipathPathRequestType**](EnableMultipathPathRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the LUN could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_expand_vmfs_extent**
> host_storage_system_expand_vmfs_extent(mo_id, expand_vmfs_extent_request_type)

Expands a VMFS extent as specified by the Disk partition specification. 

Expands a VMFS extent as specified by the Disk partition specification.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.expand_vmfs_extent_request_type import ExpandVmfsExtentRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    expand_vmfs_extent_request_type = vmware_vi.ExpandVmfsExtentRequestType() # ExpandVmfsExtentRequestType | 

    try:
        # Expands a VMFS extent as specified by the Disk partition specification. 
        api_instance.host_storage_system_expand_vmfs_extent(mo_id, expand_vmfs_extent_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_expand_vmfs_extent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **expand_vmfs_extent_request_type** | [**ExpandVmfsExtentRequestType**](ExpandVmfsExtentRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the VMFS cannot be found or is unmounted.  ***InvalidArgument***: if the extent is not part of the VMFS volume.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_extend_vffs**
> host_storage_system_extend_vffs(mo_id, extend_vffs_request_type)

Extends a VFFS by attaching a SSD. 

Extends a VFFS by attaching a SSD.  See also *HostScsiDisk.devicePath*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.extend_vffs_request_type import ExtendVffsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    extend_vffs_request_type = vmware_vi.ExtendVffsRequestType() # ExtendVffsRequestType | 

    try:
        # Extends a VFFS by attaching a SSD. 
        api_instance.host_storage_system_extend_vffs(mo_id, extend_vffs_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_extend_vffs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **extend_vffs_request_type** | [**ExtendVffsRequestType**](ExtendVffsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the VFFS cannot be found or is unmounted.  ***InvalidArgument***: if the new SSD is already used by another VFFS volume, does not exist, or is of an invalid partition type.  ***HostConfigFault***: for all other configuration failures.  ***ResourceInUse***: VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_format_vffs**
> HostVffsVolume host_storage_system_format_vffs(mo_id, format_vffs_request_type)

Format a new VFFS on a SSD disk 

Format a new VFFS on a SSD disk  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.format_vffs_request_type import FormatVffsRequestType
from vmware_vi.models.host_vffs_volume import HostVffsVolume
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    format_vffs_request_type = vmware_vi.FormatVffsRequestType() # FormatVffsRequestType | 

    try:
        # Format a new VFFS on a SSD disk 
        api_response = api_instance.host_storage_system_format_vffs(mo_id, format_vffs_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_format_vffs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_format_vffs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **format_vffs_request_type** | [**FormatVffsRequestType**](FormatVffsRequestType.md)|  | 

### Return type

[**HostVffsVolume**](HostVffsVolume.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data object that represents the VFFS file system.  |  -  |
**500** | ***InvalidArgument***: if VFFS version is invalid, the SSD disk does not exist or is of an invalid type.  ***AlreadyExists***: if the volume name is already being used by another volume on the host.  ***HostConfigFault***: for all other configuration failures.  ***ResourceInUse***: VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_format_vmfs**
> HostVmfsVolume host_storage_system_format_vmfs(mo_id, format_vmfs_request_type)

Formats a new VMFS on a disk partition. 

Formats a new VMFS on a disk partition.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.format_vmfs_request_type import FormatVmfsRequestType
from vmware_vi.models.host_vmfs_volume import HostVmfsVolume
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    format_vmfs_request_type = vmware_vi.FormatVmfsRequestType() # FormatVmfsRequestType | 

    try:
        # Formats a new VMFS on a disk partition. 
        api_response = api_instance.host_storage_system_format_vmfs(mo_id, format_vmfs_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_format_vmfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_format_vmfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **format_vmfs_request_type** | [**FormatVmfsRequestType**](FormatVmfsRequestType.md)|  | 

### Return type

[**HostVmfsVolume**](HostVmfsVolume.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data object that represents the VMFS file system.  |  -  |
**500** | ***InvalidArgument***: if VMFS version specified is not 2 or 3, if blocksize, lock mode, or volume label are invalid, the partition does not exist or is of an invalid type.  ***AlreadyExists***: if the volume name is already being used by another volume on the host.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_available_field**
> List[CustomFieldDef] host_storage_system_get_available_field(mo_id)

List of custom field definitions that are valid for the object's type. 

List of custom field definitions that are valid for the object's type.  The fields are sorted by *CustomFieldDef.name*.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_def import CustomFieldDef
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.host_storage_system_get_available_field(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_available_field: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldDef]**](CustomFieldDef.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_file_system_volume_info**
> HostFileSystemVolumeInfo host_storage_system_get_file_system_volume_info(mo_id)

File system volume information for the host. 

File system volume information for the host.  See the *FileSystemVolumeInfo* data object type for more information. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_file_system_volume_info import HostFileSystemVolumeInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # File system volume information for the host. 
        api_response = api_instance.host_storage_system_get_file_system_volume_info(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_file_system_volume_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_file_system_volume_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostFileSystemVolumeInfo**](HostFileSystemVolumeInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_multipath_state_info**
> HostMultipathStateInfo host_storage_system_get_multipath_state_info(mo_id)

Runtime information about the state of a multipath path. 

Runtime information about the state of a multipath path.  A null value will be returned if path state information is not available for this system.  In systems prior to the plug-store architecture, the state of a path may be accessible on the *HostMultipathInfo* data object of the *HostStorageSystem.storageDeviceInfo* property.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_multipath_state_info import HostMultipathStateInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Runtime information about the state of a multipath path. 
        api_response = api_instance.host_storage_system_get_multipath_state_info(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_multipath_state_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_multipath_state_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostMultipathStateInfo**](HostMultipathStateInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_storage_device_info**
> HostStorageDeviceInfo host_storage_system_get_storage_device_info(mo_id)

Host storage information up to the device level. 

Host storage information up to the device level. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_storage_device_info import HostStorageDeviceInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Host storage information up to the device level. 
        api_response = api_instance.host_storage_system_get_storage_device_info(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_storage_device_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_storage_device_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostStorageDeviceInfo**](HostStorageDeviceInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_system_file**
> List[str] host_storage_system_get_system_file(mo_id)

Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. 

Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host.  For information on datastore paths, see *Datastore*.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host. 
        api_response = api_instance.host_storage_system_get_system_file(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_system_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_system_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[str]**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_get_value**
> List[CustomFieldValue] host_storage_system_get_value(mo_id)

List of custom field values. 

List of custom field values.  Each value uses a key to associate an instance of a *CustomFieldStringValue* with a custom field definition.  ***Since:*** VI API 2.5  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.custom_field_value import CustomFieldValue
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.host_storage_system_get_value(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_get_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[CustomFieldValue]**](CustomFieldValue.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_as_local_task**
> ManagedObjectReference host_storage_system_mark_as_local_task(mo_id, mark_as_local_request_type)

Mark a disk to local disk, due to the reason that local disks behind some controllers might not be recongized as local correctly. 

Mark a disk to local disk, due to the reason that local disks behind some controllers might not be recongized as local correctly.  Task failure might lose existing claim rules on the disk.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mark_as_local_request_type import MarkAsLocalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_as_local_request_type = vmware_vi.MarkAsLocalRequestType() # MarkAsLocalRequestType | 

    try:
        # Mark a disk to local disk, due to the reason that local disks behind some controllers might not be recongized as local correctly. 
        api_response = api_instance.host_storage_system_mark_as_local_task(mo_id, mark_as_local_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mark_as_local_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_as_local_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_as_local_request_type** | [**MarkAsLocalRequestType**](MarkAsLocalRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_as_non_local_task**
> ManagedObjectReference host_storage_system_mark_as_non_local_task(mo_id, mark_as_non_local_request_type)

Mark a disk to remote disk, which is the opposite operation of *HostStorageSystem.MarkAsLocal_Task* Task failure might lose existing claim rules on the disk. 

Mark a disk to remote disk, which is the opposite operation of *HostStorageSystem.MarkAsLocal_Task* Task failure might lose existing claim rules on the disk.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mark_as_non_local_request_type import MarkAsNonLocalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_as_non_local_request_type = vmware_vi.MarkAsNonLocalRequestType() # MarkAsNonLocalRequestType | 

    try:
        # Mark a disk to remote disk, which is the opposite operation of *HostStorageSystem.MarkAsLocal_Task* Task failure might lose existing claim rules on the disk. 
        api_response = api_instance.host_storage_system_mark_as_non_local_task(mo_id, mark_as_non_local_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mark_as_non_local_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_as_non_local_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_as_non_local_request_type** | [**MarkAsNonLocalRequestType**](MarkAsNonLocalRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_as_non_ssd_task**
> ManagedObjectReference host_storage_system_mark_as_non_ssd_task(mo_id, mark_as_non_ssd_request_type)

Mark a disk to Non-SSD, which is the opposite operation of *HostStorageSystem.MarkAsSsd_Task* Task failure might lose existing claim rules on the disk. 

Mark a disk to Non-SSD, which is the opposite operation of *HostStorageSystem.MarkAsSsd_Task* Task failure might lose existing claim rules on the disk.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mark_as_non_ssd_request_type import MarkAsNonSsdRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_as_non_ssd_request_type = vmware_vi.MarkAsNonSsdRequestType() # MarkAsNonSsdRequestType | 

    try:
        # Mark a disk to Non-SSD, which is the opposite operation of *HostStorageSystem.MarkAsSsd_Task* Task failure might lose existing claim rules on the disk. 
        api_response = api_instance.host_storage_system_mark_as_non_ssd_task(mo_id, mark_as_non_ssd_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mark_as_non_ssd_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_as_non_ssd_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_as_non_ssd_request_type** | [**MarkAsNonSsdRequestType**](MarkAsNonSsdRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_as_ssd_task**
> ManagedObjectReference host_storage_system_mark_as_ssd_task(mo_id, mark_as_ssd_request_type)

Mark a disk to SSD, due to the reason that SSDs behind some controllers might not be recongized as SSD correctly. 

Mark a disk to SSD, due to the reason that SSDs behind some controllers might not be recongized as SSD correctly.  Task failure might lose existing claim rules on the disk.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mark_as_ssd_request_type import MarkAsSsdRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_as_ssd_request_type = vmware_vi.MarkAsSsdRequestType() # MarkAsSsdRequestType | 

    try:
        # Mark a disk to SSD, due to the reason that SSDs behind some controllers might not be recongized as SSD correctly. 
        api_response = api_instance.host_storage_system_mark_as_ssd_task(mo_id, mark_as_ssd_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mark_as_ssd_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_as_ssd_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_as_ssd_request_type** | [**MarkAsSsdRequestType**](MarkAsSsdRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_for_removal**
> host_storage_system_mark_for_removal(mo_id, mark_for_removal_request_type)

Mark or unmark the given FCoE HBA for removal from the host system. 

Deprecated as of vSphere API 8.0. Software FCoE not supported.  Mark or unmark the given FCoE HBA for removal from the host system.  Marking an FCoE HBA for removal will result in the HBA not being discovered upon host reboot. Until reboot, the HBA remains visible in the storage topology.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mark_for_removal_request_type import MarkForRemovalRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_for_removal_request_type = vmware_vi.MarkForRemovalRequestType() # MarkForRemovalRequestType | 

    try:
        # Mark or unmark the given FCoE HBA for removal from the host system. 
        api_instance.host_storage_system_mark_for_removal(mo_id, mark_for_removal_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_for_removal: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_for_removal_request_type** | [**MarkForRemovalRequestType**](MarkForRemovalRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the given HBA could not be found.  ***InvalidArgument***: if the given HBA is not an FCoE HBA.  ***HostConfigFault***: if the host does not support removing the given HBA.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_perennially_reserved**
> host_storage_system_mark_perennially_reserved(mo_id, mark_perennially_reserved_request_type)

Marks the specified LUN as perennially reserved. 

Marks the specified LUN as perennially reserved.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mark_perennially_reserved_request_type import MarkPerenniallyReservedRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_perennially_reserved_request_type = vmware_vi.MarkPerenniallyReservedRequestType() # MarkPerenniallyReservedRequestType | 

    try:
        # Marks the specified LUN as perennially reserved. 
        api_instance.host_storage_system_mark_perennially_reserved(mo_id, mark_perennially_reserved_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_perennially_reserved: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_perennially_reserved_request_type** | [**MarkPerenniallyReservedRequestType**](MarkPerenniallyReservedRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: if unable to change perennially reserved state.  ***NotFound***: if the device could not be found.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mark_perennially_reserved_ex_task**
> ManagedObjectReference host_storage_system_mark_perennially_reserved_ex_task(mo_id, mark_perennially_reserved_ex_request_type)

Marks the specified one or more SCSI LUN's perennially reserved based on the sate. 

Marks the specified one or more SCSI LUN's perennially reserved based on the sate.  ***Since:*** vSphere API 6.7.2  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mark_perennially_reserved_ex_request_type import MarkPerenniallyReservedExRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_perennially_reserved_ex_request_type = vmware_vi.MarkPerenniallyReservedExRequestType() # MarkPerenniallyReservedExRequestType | 

    try:
        # Marks the specified one or more SCSI LUN's perennially reserved based on the sate. 
        api_response = api_instance.host_storage_system_mark_perennially_reserved_ex_task(mo_id, mark_perennially_reserved_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mark_perennially_reserved_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mark_perennially_reserved_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_perennially_reserved_ex_request_type** | [**MarkPerenniallyReservedExRequestType**](MarkPerenniallyReservedExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mount_vffs_volume**
> host_storage_system_mount_vffs_volume(mo_id, mount_vffs_volume_request_type)

Mount the unmounted VFFS volume. 

Mount the unmounted VFFS volume.  See *HostStorageSystem.UnmountVffsVolume*.  mountVffsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mount_vffs_volume_request_type import MountVffsVolumeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mount_vffs_volume_request_type = vmware_vi.MountVffsVolumeRequestType() # MountVffsVolumeRequestType | 

    try:
        # Mount the unmounted VFFS volume. 
        api_instance.host_storage_system_mount_vffs_volume(mo_id, mount_vffs_volume_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mount_vffs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mount_vffs_volume_request_type** | [**MountVffsVolumeRequestType**](MountVffsVolumeRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if VFFS uuid is not found on the host.  ***InvalidState***: if - The volume is already mounted. - The volume is inaccessible.     ***HostConfigFault***: for all other configuration failures.  ***ResourceInUse***: VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mount_vmfs_volume**
> host_storage_system_mount_vmfs_volume(mo_id, mount_vmfs_volume_request_type)

Mount the unmounted Vmfs volume. 

Mount the unmounted Vmfs volume.  A newly discovered vmfs volume will be mounted unless, it has been explicitly unmounted. The default mount behavior of Vmfs volumes is auto-mount. See *HostStorageSystem.UnmountVmfsVolume*.  mountVmfsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mount_vmfs_volume_request_type import MountVmfsVolumeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mount_vmfs_volume_request_type = vmware_vi.MountVmfsVolumeRequestType() # MountVmfsVolumeRequestType | 

    try:
        # Mount the unmounted Vmfs volume. 
        api_instance.host_storage_system_mount_vmfs_volume(mo_id, mount_vmfs_volume_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mount_vmfs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mount_vmfs_volume_request_type** | [**MountVmfsVolumeRequestType**](MountVmfsVolumeRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if VMFS Uuid is not found on the host.  ***InvalidState***: if - The volume is already mounted. - The volume is inaccessible.     ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_mount_vmfs_volume_ex_task**
> ManagedObjectReference host_storage_system_mount_vmfs_volume_ex_task(mo_id, mount_vmfs_volume_ex_request_type)

Mount one or more VMFS volumes. 

Mount one or more VMFS volumes.  This is an asynchronous, batch operation of mountVmfsVolume. Please see *HostStorageSystem.MountVmfsVolume* for operational details.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.mount_vmfs_volume_ex_request_type import MountVmfsVolumeExRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mount_vmfs_volume_ex_request_type = vmware_vi.MountVmfsVolumeExRequestType() # MountVmfsVolumeExRequestType | 

    try:
        # Mount one or more VMFS volumes. 
        api_response = api_instance.host_storage_system_mount_vmfs_volume_ex_task(mo_id, mount_vmfs_volume_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_mount_vmfs_volume_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_mount_vmfs_volume_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mount_vmfs_volume_ex_request_type** | [**MountVmfsVolumeExRequestType**](MountVmfsVolumeExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_available_ssds**
> List[HostScsiDisk] host_storage_system_query_available_ssds(mo_id, query_available_ssds_request_type)

Query the list SSD disks that can be used to contain a VFFS volume. 

Query the list SSD disks that can be used to contain a VFFS volume.  If the optional parameter name is supplied, queries for the SSD disks that can be used to contain extents of the specified VFFS volume. Otherwise, the method retrieves the SSD disks that can be used to contain the new VFFS volume.  This operation will filter out SSD disks that are currently in use by an existing VFFS volume.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_scsi_disk import HostScsiDisk
from vmware_vi.models.query_available_ssds_request_type import QueryAvailableSsdsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_available_ssds_request_type = vmware_vi.QueryAvailableSsdsRequestType() # QueryAvailableSsdsRequestType | 

    try:
        # Query the list SSD disks that can be used to contain a VFFS volume. 
        api_response = api_instance.host_storage_system_query_available_ssds(mo_id, query_available_ssds_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_query_available_ssds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_available_ssds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_available_ssds_request_type** | [**QueryAvailableSsdsRequestType**](QueryAvailableSsdsRequestType.md)|  | 

### Return type

[**List[HostScsiDisk]**](HostScsiDisk.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of data objects descrbing SSD disks.  |  -  |
**500** | ***NotFound***: if the named VFFS volume is not found.  ***InvalidArgument***: if named VFFS volume is not a VFFS volume  ***HostConfigFault***: if unable to query disk information.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_nfs_user**
> HostNasVolumeUserInfo host_storage_system_query_nfs_user(mo_id)

Query the NFS user configured on the esx host 

Query the NFS user configured on the esx host  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_nas_volume_user_info import HostNasVolumeUserInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Query the NFS user configured on the esx host 
        api_response = api_instance.host_storage_system_query_nfs_user(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_query_nfs_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_nfs_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostNasVolumeUserInfo**](HostNasVolumeUserInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserInfo objects. See *HostNasVolumeUserInfo*  |  -  |
**500** | ***HostConfigFault***: Unable to get NFS user due to host configuration problem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_path_selection_policy_options**
> List[HostPathSelectionPolicyOption] host_storage_system_query_path_selection_policy_options(mo_id)

Queries the set of path selection policy options. 

Queries the set of path selection policy options.  The set of policy options indicates what path selection policies can be used by a device managed by native multipathing. Devices managed through native multipathing are described in the *HostMultipathInfo* data object.  Filtering capabilities are not currently present but may be added in the future.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_path_selection_policy_option import HostPathSelectionPolicyOption
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Queries the set of path selection policy options. 
        api_response = api_instance.host_storage_system_query_path_selection_policy_options(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_query_path_selection_policy_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_path_selection_policy_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostPathSelectionPolicyOption]**](HostPathSelectionPolicyOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of path selection policy descriptions that match the search criteria. Details about the policies will also be provided in accordance to the query specification.  |  -  |
**500** | ***HostConfigFault***: for system configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_storage_array_type_policy_options**
> List[HostStorageArrayTypePolicyOption] host_storage_system_query_storage_array_type_policy_options(mo_id)

Queries the set of storage array type policy options. 

Queries the set of storage array type policy options.  The set of policy options indicates what storage array type policies can be used by a device managed by native multipathing. Devices managed through native multipathing are described in the *HostMultipathInfo* data object.  Filtering capabilities are not currently present but may be added in the future.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_storage_array_type_policy_option import HostStorageArrayTypePolicyOption
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Queries the set of storage array type policy options. 
        api_response = api_instance.host_storage_system_query_storage_array_type_policy_options(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_query_storage_array_type_policy_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_storage_array_type_policy_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostStorageArrayTypePolicyOption]**](HostStorageArrayTypePolicyOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of storage array type policy descriptions.  |  -  |
**500** | ***HostConfigFault***: for system configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_unresolved_vmfs_volume**
> List[HostUnresolvedVmfsVolume] host_storage_system_query_unresolved_vmfs_volume(mo_id)

Get the list of unbound VMFS volumes. 

Get the list of unbound VMFS volumes.  For sharing a volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_unresolved_vmfs_volume import HostUnresolvedVmfsVolume
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the list of unbound VMFS volumes. 
        api_response = api_instance.host_storage_system_query_unresolved_vmfs_volume(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_query_unresolved_vmfs_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_unresolved_vmfs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[HostUnresolvedVmfsVolume]**](HostUnresolvedVmfsVolume.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of unbound VMFS volumes.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_query_vmfs_config_option**
> List[VmfsConfigOption] host_storage_system_query_vmfs_config_option(mo_id)

Get the VMFS configuration options, including block size, unmap granularity. 

Get the VMFS configuration options, including block size, unmap granularity.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.vmfs_config_option import VmfsConfigOption
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Get the VMFS configuration options, including block size, unmap granularity. 
        api_response = api_instance.host_storage_system_query_vmfs_config_option(mo_id)
        print("The response of HostStorageSystemApi->host_storage_system_query_vmfs_config_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_query_vmfs_config_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VmfsConfigOption]**](VmfsConfigOption.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VMFS configuration options.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_refresh_storage_system**
> host_storage_system_refresh_storage_system(mo_id)

Obtains the latest host storage information related to storage devices, topology, and file systems. 

Obtains the latest host storage information related to storage devices, topology, and file systems.  The ESX host updates its storage information asynchronously.  This method may update the following inventory elements: - Devices and storage topology   (*HostSystem*.*HostSystem.config*.*HostConfigInfo.storageDevice*). - VMFS and NFS datastores (*HostSystem*.*HostSystem.datastore*). - File system volumes   (*HostSystem*.*HostSystem.config*.*HostConfigInfo.fileSystemVolume*).    The Server performs asynchronous updates to the inventory. Use the *PropertyCollector*.*PropertyCollector.WaitForUpdatesEx* method to obtain the property changes.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Obtains the latest host storage information related to storage devices, topology, and file systems. 
        api_instance.host_storage_system_refresh_storage_system(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_refresh_storage_system: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_remove_internet_scsi_send_targets**
> host_storage_system_remove_internet_scsi_send_targets(mo_id, remove_internet_scsi_send_targets_request_type)

Removes Send Target entries from the host bus adapter discovery list. 

Removes Send Target entries from the host bus adapter discovery list.  The DiscoveryProperty.sendTargetsDiscoveryEnabled must be set to true. If any of the targets provided as parameters are not found in the existing list, the other targets are removed and an exception is thrown.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_internet_scsi_send_targets_request_type import RemoveInternetScsiSendTargetsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_internet_scsi_send_targets_request_type = vmware_vi.RemoveInternetScsiSendTargetsRequestType() # RemoveInternetScsiSendTargetsRequestType | 

    try:
        # Removes Send Target entries from the host bus adapter discovery list. 
        api_instance.host_storage_system_remove_internet_scsi_send_targets(mo_id, remove_internet_scsi_send_targets_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_remove_internet_scsi_send_targets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_internet_scsi_send_targets_request_type** | [**RemoveInternetScsiSendTargetsRequestType**](RemoveInternetScsiSendTargetsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if at least one target was not found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_remove_internet_scsi_static_targets**
> host_storage_system_remove_internet_scsi_static_targets(mo_id, remove_internet_scsi_static_targets_request_type)

Removes static target entries from the host bus adapter discovery list. 

Removes static target entries from the host bus adapter discovery list.  The DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true. If any of the targets provided as parameters are not found in the existing list, the other targets are removed and an exception is thrown.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_internet_scsi_static_targets_request_type import RemoveInternetScsiStaticTargetsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_internet_scsi_static_targets_request_type = vmware_vi.RemoveInternetScsiStaticTargetsRequestType() # RemoveInternetScsiStaticTargetsRequestType | 

    try:
        # Removes static target entries from the host bus adapter discovery list. 
        api_instance.host_storage_system_remove_internet_scsi_static_targets(mo_id, remove_internet_scsi_static_targets_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_remove_internet_scsi_static_targets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_internet_scsi_static_targets_request_type** | [**RemoveInternetScsiStaticTargetsRequestType**](RemoveInternetScsiStaticTargetsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if at least one target was not found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_remove_nvme_over_rdma_adapter**
> host_storage_system_remove_nvme_over_rdma_adapter(mo_id, remove_nvme_over_rdma_adapter_request_type)

Removes a software NVME over RDMA adapter. 

Removes a software NVME over RDMA adapter.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_nvme_over_rdma_adapter_request_type import RemoveNvmeOverRdmaAdapterRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_nvme_over_rdma_adapter_request_type = vmware_vi.RemoveNvmeOverRdmaAdapterRequestType() # RemoveNvmeOverRdmaAdapterRequestType | 

    try:
        # Removes a software NVME over RDMA adapter. 
        api_instance.host_storage_system_remove_nvme_over_rdma_adapter(mo_id, remove_nvme_over_rdma_adapter_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_remove_nvme_over_rdma_adapter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_nvme_over_rdma_adapter_request_type** | [**RemoveNvmeOverRdmaAdapterRequestType**](RemoveNvmeOverRdmaAdapterRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the given HBA could not be found.  ***InvalidArgument***: if the given HBA is not an NVMe over RDMA HBA.  ***ResourceInUse***: if the given HBA is in use.  ***HostConfigFault***: if the host is unable to remove the given HBA.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_remove_software_adapter**
> host_storage_system_remove_software_adapter(mo_id, remove_software_adapter_request_type)

Removes a software host bus adapter, if the adapter type allows it. 

Removes a software host bus adapter, if the adapter type allows it.  ***Since:*** vSphere API 7.0.3.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.remove_software_adapter_request_type import RemoveSoftwareAdapterRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_software_adapter_request_type = vmware_vi.RemoveSoftwareAdapterRequestType() # RemoveSoftwareAdapterRequestType | 

    try:
        # Removes a software host bus adapter, if the adapter type allows it. 
        api_instance.host_storage_system_remove_software_adapter(mo_id, remove_software_adapter_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_remove_software_adapter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_software_adapter_request_type** | [**RemoveSoftwareAdapterRequestType**](RemoveSoftwareAdapterRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the given HBA could not be found.  ***InvalidArgument***: if the given adapter type cannot be removed.  ***ResourceInUse***: if the given HBA is in use.  ***HostConfigFault***: if the host is unable to remove the given HBA.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_rescan_all_hba**
> host_storage_system_rescan_all_hba(mo_id)

Scans all host bus adapters to obtain the current list of devices and device topology. 

Scans all host bus adapters to obtain the current list of devices and device topology.  The *HostStorageSystem.RescanAllHba* method looks for new devices, removed devices, and path changes.  This method may update the following inventory elements: - Devices and storage topology   (*HostSystem*.*HostSystem.config*.*HostConfigInfo.storageDevice*). - VMFS and NFS datastores (*HostSystem*.*HostSystem.datastore*). - File system volumes (*HostSystem*.*HostSystem.config*.*HostConfigInfo.fileSystemVolume*).    The Server performs asynchronous updates to the inventory. Use the *PropertyCollector*.*PropertyCollector.WaitForUpdatesEx* method to obtain the property changes.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Scans all host bus adapters to obtain the current list of devices and device topology. 
        api_instance.host_storage_system_rescan_all_hba(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_rescan_all_hba: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: if rescan failed.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_rescan_hba**
> host_storage_system_rescan_hba(mo_id, rescan_hba_request_type)

Issues a request to rescan a specific host bus adapter for new storage devices. 

Issues a request to rescan a specific host bus adapter for new storage devices.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.rescan_hba_request_type import RescanHbaRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rescan_hba_request_type = vmware_vi.RescanHbaRequestType() # RescanHbaRequestType | 

    try:
        # Issues a request to rescan a specific host bus adapter for new storage devices. 
        api_instance.host_storage_system_rescan_hba(mo_id, rescan_hba_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_rescan_hba: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rescan_hba_request_type** | [**RescanHbaRequestType**](RescanHbaRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter cannot be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_rescan_vffs**
> host_storage_system_rescan_vffs(mo_id)

Rescans for new VFFS. 

Rescans for new VFFS.  The *HostStorageSystem.RefreshStorageSystem* method also performs a VFFS rescan.  *HostStorageSystem.RescanVffs* may update the *HostSystem*.*HostSystem.config*.*HostConfigInfo.fileSystemVolume* property. The Server performs asynchronous updates to the inventory. Use the *PropertyCollector*.*PropertyCollector.WaitForUpdatesEx* method to obtain the property changes.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Rescans for new VFFS. 
        api_instance.host_storage_system_rescan_vffs(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_rescan_vffs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: if configuration fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_rescan_vmfs**
> host_storage_system_rescan_vmfs(mo_id)

Rescans for new Virtual Machine File Systems (VMFS). 

Rescans for new Virtual Machine File Systems (VMFS).  The *HostStorageSystem.RefreshStorageSystem* method also performs a VMFS rescan.  *HostStorageSystem.RescanVmfs* may update the *HostSystem*.*HostSystem.config*.*HostConfigInfo.fileSystemVolume* property. The Server performs asynchronous updates to the inventory. Use the *PropertyCollector*.*PropertyCollector.WaitForUpdatesEx* method to obtain the property changes.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Rescans for new Virtual Machine File Systems (VMFS). 
        api_instance.host_storage_system_rescan_vmfs(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_rescan_vmfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: if configuration fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_resolve_multiple_unresolved_vmfs_volumes**
> List[HostUnresolvedVmfsResolutionResult] host_storage_system_resolve_multiple_unresolved_vmfs_volumes(mo_id, resolve_multiple_unresolved_vmfs_volumes_request_type)

Resignature or 'Force Mount' list of unbound VMFS volumes. 

Resignature or 'Force Mount' list of unbound VMFS volumes.  To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.  Resignature results in a new VMFS volume on the host. Operations performed at the StorageSystem interface apply only to a specific host. Hence, callers of this method are responsible for issuing rescan operations to detect the new VMFS volume on other hosts. Alternatively, callers that want VirtualCenter to handle rescanning the necessary hosts should use the DatastoreSystem interface.  When user wants to keep the original Vmfs Uuid and mount it on the host, set the 'resolutionSpec.uuidResolution' to 'forceMounted' This is per-host operation. It will return an array of ResolutionResult describing success or failure associated with each specification.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_unresolved_vmfs_resolution_result import HostUnresolvedVmfsResolutionResult
from vmware_vi.models.resolve_multiple_unresolved_vmfs_volumes_request_type import ResolveMultipleUnresolvedVmfsVolumesRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    resolve_multiple_unresolved_vmfs_volumes_request_type = vmware_vi.ResolveMultipleUnresolvedVmfsVolumesRequestType() # ResolveMultipleUnresolvedVmfsVolumesRequestType | 

    try:
        # Resignature or 'Force Mount' list of unbound VMFS volumes. 
        api_response = api_instance.host_storage_system_resolve_multiple_unresolved_vmfs_volumes(mo_id, resolve_multiple_unresolved_vmfs_volumes_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_resolve_multiple_unresolved_vmfs_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_resolve_multiple_unresolved_vmfs_volumes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **resolve_multiple_unresolved_vmfs_volumes_request_type** | [**ResolveMultipleUnresolvedVmfsVolumesRequestType**](ResolveMultipleUnresolvedVmfsVolumesRequestType.md)|  | 

### Return type

[**List[HostUnresolvedVmfsResolutionResult]**](HostUnresolvedVmfsResolutionResult.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data object that represents the VMFS file system and return status value.  |  -  |
**500** | ***HostConfigFault***: if batch operation fails on the host. Because the returned array of ResolutionResult contains the new VMFS volume or fault for each operation, as of vSphere API 5.x, we won&#39;t throw fault when batch operation fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task**
> ManagedObjectReference host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task(mo_id, resolve_multiple_unresolved_vmfs_volumes_ex_request_type)

Resignature or 'Force Mount' list of unbound VMFS volumes. 

Resignature or 'Force Mount' list of unbound VMFS volumes.  To safely enable sharing of the volume across hosts, a VMFS volume is bound to its underlying block device storage. When a low level block copy is performed to copy or move the VMFS volume, the copied volume will be unbound. In order for the VMFS volume to be usable, a resolution operation is needed to determine whether the VMFS volume should be treated as a new volume or not and what extents compose that volume in the event there is more than one unbound volume.  Resignature results in a new VMFS volume on the host. Operations performed at the *HostStorageSystem* interface apply only to a specific host. Hence, callers of this method are responsible for issuing rescan operations to detect the new VMFS volume on other hosts. Alternatively, callers that want VirtualCenter to handle rescanning the necessary hosts should use the *HostDatastoreSystem* interface.  When user wants to keep the original VMFS UUID and mount it on the host, set the resolutionSpec.uuidResolution (*HostUnresolvedVmfsResolutionSpec.uuidResolution*) to *forceMount*. This is per-host operation.  It will return an array of *HostUnresolvedVmfsResolutionResult* describing success or failure associated with each specification.  This method behaves the same as *HostStorageSystem.ResolveMultipleUnresolvedVmfsVolumes* except that it returns a task to support monitoring the operation. This is important for operations with large number of unresolved volumes which may take potentially dozens of minutes to complete.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.resolve_multiple_unresolved_vmfs_volumes_ex_request_type import ResolveMultipleUnresolvedVmfsVolumesExRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    resolve_multiple_unresolved_vmfs_volumes_ex_request_type = vmware_vi.ResolveMultipleUnresolvedVmfsVolumesExRequestType() # ResolveMultipleUnresolvedVmfsVolumesExRequestType | 

    try:
        # Resignature or 'Force Mount' list of unbound VMFS volumes. 
        api_response = api_instance.host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task(mo_id, resolve_multiple_unresolved_vmfs_volumes_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_resolve_multiple_unresolved_vmfs_volumes_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **resolve_multiple_unresolved_vmfs_volumes_ex_request_type** | [**ResolveMultipleUnresolvedVmfsVolumesExRequestType**](ResolveMultipleUnresolvedVmfsVolumesExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains an array of *HostUnresolvedVmfsResolutionResult* describing success or failure associated with each specification.  Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: if batch operation fails on the host. Because the returned array of ResolutionResult contains the new VMFS volume or fault for each operation, as of vSphere API 5.x, we won&#39;t throw fault when batch operation fails.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_retrieve_disk_partition_info**
> List[HostDiskPartitionInfo] host_storage_system_retrieve_disk_partition_info(mo_id, retrieve_disk_partition_info_request_type)

Gets the partition information for the disks named by the device names. 

Gets the partition information for the disks named by the device names.  ***Required privileges:*** System.Read 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_disk_partition_info import HostDiskPartitionInfo
from vmware_vi.models.retrieve_disk_partition_info_request_type import RetrieveDiskPartitionInfoRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    retrieve_disk_partition_info_request_type = vmware_vi.RetrieveDiskPartitionInfoRequestType() # RetrieveDiskPartitionInfoRequestType | 

    try:
        # Gets the partition information for the disks named by the device names. 
        api_response = api_instance.host_storage_system_retrieve_disk_partition_info(mo_id, retrieve_disk_partition_info_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_retrieve_disk_partition_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_retrieve_disk_partition_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **retrieve_disk_partition_info_request_type** | [**RetrieveDiskPartitionInfoRequestType**](RetrieveDiskPartitionInfoRequestType.md)|  | 

### Return type

[**List[HostDiskPartitionInfo]**](HostDiskPartitionInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of information about the partitions.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_set_custom_value**
> host_storage_system_set_custom_value(mo_id, set_custom_value_request_type)

Assigns a value to a custom field. 

Assigns a value to a custom field.  The setCustomValue method requires whichever updatePrivilege is defined as one of the *CustomFieldDef.fieldInstancePrivileges* for the CustomFieldDef whose value is being changed.  ***Since:*** VI API 2.5 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_custom_value_request_type import SetCustomValueRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.host_storage_system_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_set_custom_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_custom_value_request_type** | [**SetCustomValueRequestType**](SetCustomValueRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_set_multipath_lun_policy**
> host_storage_system_set_multipath_lun_policy(mo_id, set_multipath_lun_policy_request_type)

Updates the path selection policy for a Logical Unit. 

Updates the path selection policy for a Logical Unit.  Use the LUN uuid from *HostMultipathInfoLogicalUnit*.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_multipath_lun_policy_request_type import SetMultipathLunPolicyRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_multipath_lun_policy_request_type = vmware_vi.SetMultipathLunPolicyRequestType() # SetMultipathLunPolicyRequestType | 

    try:
        # Updates the path selection policy for a Logical Unit. 
        api_instance.host_storage_system_set_multipath_lun_policy(mo_id, set_multipath_lun_policy_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_set_multipath_lun_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_multipath_lun_policy_request_type** | [**SetMultipathLunPolicyRequestType**](SetMultipathLunPolicyRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the LUN could not be found.  ***InvalidArgument***: if the policy is invalid.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_set_nfs_user**
> host_storage_system_set_nfs_user(mo_id, set_nfs_user_request_type)

Set NFS username and password on the host. 

Set NFS username and password on the host.  The specified password is stored encrypted at the host and overwrites any previous password configuration. This information is only needed when the host has mounted NFS volumes with security types that require user credentials for accessing data. The password is used to acquire credentials that the NFS client needs to use in order to secure NFS traffic using RPCSECGSS. The client will access files on all volumes mounted on this host (that are mounted with the relevant security type) on behalf of specified user.  At present, this API supports only file system NFSv4.1.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_nfs_user_request_type import SetNFSUserRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_nfs_user_request_type = vmware_vi.SetNFSUserRequestType() # SetNFSUserRequestType | 

    try:
        # Set NFS username and password on the host. 
        api_instance.host_storage_system_set_nfs_user(mo_id, set_nfs_user_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_set_nfs_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_nfs_user_request_type** | [**SetNFSUserRequestType**](SetNFSUserRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: Unable to set user/passwords due to host configuration problem.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_turn_disk_locator_led_off_task**
> ManagedObjectReference host_storage_system_turn_disk_locator_led_off_task(mo_id, turn_disk_locator_led_off_request_type)

Turn off one or more disk locator LEDs. 

Turn off one or more disk locator LEDs.  This is a batch operation to turn off one or more disk locator LEDs, which is the opposite operation of *HostStorageSystem.TurnDiskLocatorLedOn_Task*  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.turn_disk_locator_led_off_request_type import TurnDiskLocatorLedOffRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    turn_disk_locator_led_off_request_type = vmware_vi.TurnDiskLocatorLedOffRequestType() # TurnDiskLocatorLedOffRequestType | 

    try:
        # Turn off one or more disk locator LEDs. 
        api_response = api_instance.host_storage_system_turn_disk_locator_led_off_task(mo_id, turn_disk_locator_led_off_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_turn_disk_locator_led_off_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_turn_disk_locator_led_off_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **turn_disk_locator_led_off_request_type** | [**TurnDiskLocatorLedOffRequestType**](TurnDiskLocatorLedOffRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_turn_disk_locator_led_on_task**
> ManagedObjectReference host_storage_system_turn_disk_locator_led_on_task(mo_id, turn_disk_locator_led_on_request_type)

Turn on one or more disk locator LEDs, duration is the maximum that hardware can support. 

Turn on one or more disk locator LEDs, duration is the maximum that hardware can support.  This is a batch operation to turn on one or more disk locator LEDs, so that user can easily locate the ScsiDisk on physical infrastructure.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.turn_disk_locator_led_on_request_type import TurnDiskLocatorLedOnRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    turn_disk_locator_led_on_request_type = vmware_vi.TurnDiskLocatorLedOnRequestType() # TurnDiskLocatorLedOnRequestType | 

    try:
        # Turn on one or more disk locator LEDs, duration is the maximum that hardware can support. 
        api_response = api_instance.host_storage_system_turn_disk_locator_led_on_task(mo_id, turn_disk_locator_led_on_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_turn_disk_locator_led_on_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_turn_disk_locator_led_on_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **turn_disk_locator_led_on_request_type** | [**TurnDiskLocatorLedOnRequestType**](TurnDiskLocatorLedOnRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_unmap_vmfs_volume_ex_task**
> ManagedObjectReference host_storage_system_unmap_vmfs_volume_ex_task(mo_id, unmap_vmfs_volume_ex_request_type)

Unmap one or more VMFS volumes. 

Unmap one or more VMFS volumes.  This is an asynchronous, batch operation. The operation unmaps free blocks in each VMFS volume.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.unmap_vmfs_volume_ex_request_type import UnmapVmfsVolumeExRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmap_vmfs_volume_ex_request_type = vmware_vi.UnmapVmfsVolumeExRequestType() # UnmapVmfsVolumeExRequestType | 

    try:
        # Unmap one or more VMFS volumes. 
        api_response = api_instance.host_storage_system_unmap_vmfs_volume_ex_task(mo_id, unmap_vmfs_volume_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_unmap_vmfs_volume_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_unmap_vmfs_volume_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmap_vmfs_volume_ex_request_type** | [**UnmapVmfsVolumeExRequestType**](UnmapVmfsVolumeExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_unmount_force_mounted_vmfs_volume**
> host_storage_system_unmount_force_mounted_vmfs_volume(mo_id, unmount_force_mounted_vmfs_volume_request_type)

Unmount the 'forceMounted' Vmfs volume. 

Unmount the 'forceMounted' Vmfs volume.  When a low level block copy is performed to copy or move the VMFS volume, the copied volume is unresolved. For the VMFS volume to be usable, a resolution operation is applied. As part of resolution operation, user may decide to keep the original VMFS Uuid. Once the resolution is applied, the VMFS volume is mounted on the host for its use. User can unmount the VMFS volume if it is not being used by any registered VMs.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unmount_force_mounted_vmfs_volume_request_type import UnmountForceMountedVmfsVolumeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmount_force_mounted_vmfs_volume_request_type = vmware_vi.UnmountForceMountedVmfsVolumeRequestType() # UnmountForceMountedVmfsVolumeRequestType | 

    try:
        # Unmount the 'forceMounted' Vmfs volume. 
        api_instance.host_storage_system_unmount_force_mounted_vmfs_volume(mo_id, unmount_force_mounted_vmfs_volume_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_unmount_force_mounted_vmfs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmount_force_mounted_vmfs_volume_request_type** | [**UnmountForceMountedVmfsVolumeRequestType**](UnmountForceMountedVmfsVolumeRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if VMFS Uuid is not found on the host.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_unmount_vffs_volume**
> host_storage_system_unmount_vffs_volume(mo_id, unmount_vffs_volume_request_type)

Unmount the VFFS volume. 

Unmount the VFFS volume.  An unmounted volume cannot be used for any filesystem operation requiring I/O. In contrast to removal, this operation does not destroy or alter partitions on which VFFS volumes reside. The mountState will be persisted across filesystem rescans and host reboots. See *HostStorageSystem.MountVffsVolume*.  unmountVffsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed. See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unmount_vffs_volume_request_type import UnmountVffsVolumeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmount_vffs_volume_request_type = vmware_vi.UnmountVffsVolumeRequestType() # UnmountVffsVolumeRequestType | 

    try:
        # Unmount the VFFS volume. 
        api_instance.host_storage_system_unmount_vffs_volume(mo_id, unmount_vffs_volume_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_unmount_vffs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmount_vffs_volume_request_type** | [**UnmountVffsVolumeRequestType**](UnmountVffsVolumeRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if VFFS uuid is not found on the host.  ***InvalidState***: if - The volume is already unmounted. - The volume is inaccessible.    ***ResourceInUse***: if - 1 or more programs have I/O outstanding on this volume.    ***HostConfigFault***: for all other configuration failures.  ***ResourceInUse***: VFFS volume is being used.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_unmount_vmfs_volume**
> host_storage_system_unmount_vmfs_volume(mo_id, unmount_vmfs_volume_request_type)

Unmount the Vmfs volume. 

Unmount the Vmfs volume.  An unmounted volume cannot be used for any filesystem operation requiring I/O. In contrast to removal, this operation does not destroy or alter partitions on which vmfs volumes reside. The mountState will be persisted across filesystem rescans and host reboots. See *HostStorageSystem.MountVmfsVolume*.  unmountVmfsVolume is part of the Unmount / Detach workflow used when a device will be permanently removed.                           Mounted Vmfs Volume         unmountVmfsVolume  |  ^ mountVmfsVolume                            V  |                          Unmounted Vmfs Volume                   Attached Scsi Device (honors I/O)         detachScsiLun      |  ^ attachScsiLun                            V  |       Detached Scsi Device (does not honor I/O)  It is safe to unprovision a Lun from the Storage array \\*only\\* after a Scsi device is detached.  The best practice for decommisioning a Lun would be to find out the set of subsystems that a Lun is being used for. Many of the systems are listed as exceptions in the function documentation.  One typical workflow could be: - Find out if the device is used as a Vmfs Extent. (See VmfsVolume.Extent API) - Unmount the Vmfs Volume. - Find out if device is used by the Diagnostic system (See Diagnostic System API). - Deactivate the diagnostic system, if it is being used. - Find out if this device is used to back a VM's RDM (See VirtualMachine API). - Remove this device from the VM. - Detach the Scsi device. - On success, it is safe to decommision the Lun at this point.    See also *HostStorageSystem.DetachScsiLun*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.unmount_vmfs_volume_request_type import UnmountVmfsVolumeRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmount_vmfs_volume_request_type = vmware_vi.UnmountVmfsVolumeRequestType() # UnmountVmfsVolumeRequestType | 

    try:
        # Unmount the Vmfs volume. 
        api_instance.host_storage_system_unmount_vmfs_volume(mo_id, unmount_vmfs_volume_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_unmount_vmfs_volume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmount_vmfs_volume_request_type** | [**UnmountVmfsVolumeRequestType**](UnmountVmfsVolumeRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if VMFS Uuid is not found on the host.  ***InvalidState***: if - The volume is already unmounted. - The volume is inaccessible.    ***ResourceInUse***: if - There is any VM registered on this volume. - 1 or more programs have I/O outstanding on this volume.    ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_unmount_vmfs_volume_ex_task**
> ManagedObjectReference host_storage_system_unmount_vmfs_volume_ex_task(mo_id, unmount_vmfs_volume_ex_request_type)

Unmount one or more VMFS volumes. 

Unmount one or more VMFS volumes.  This is an asynchronous, batch operation of unmountVmfsVolume. Please see *HostStorageSystem.UnmountVmfsVolume* for operational details.  ***Since:*** vSphere API 6.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.unmount_vmfs_volume_ex_request_type import UnmountVmfsVolumeExRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    unmount_vmfs_volume_ex_request_type = vmware_vi.UnmountVmfsVolumeExRequestType() # UnmountVmfsVolumeExRequestType | 

    try:
        # Unmount one or more VMFS volumes. 
        api_response = api_instance.host_storage_system_unmount_vmfs_volume_ex_task(mo_id, unmount_vmfs_volume_ex_request_type)
        print("The response of HostStorageSystemApi->host_storage_system_unmount_vmfs_volume_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_unmount_vmfs_volume_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **unmount_vmfs_volume_ex_request_type** | [**UnmountVmfsVolumeExRequestType**](UnmountVmfsVolumeExRequestType.md)|  | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***HostConfigFault***: for host configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_disk_partitions**
> host_storage_system_update_disk_partitions(mo_id, update_disk_partitions_request_type)

Changes the partitions on the disk by supplying a partition specification and the device name. 

Changes the partitions on the disk by supplying a partition specification and the device name.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_disk_partitions_request_type import UpdateDiskPartitionsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_disk_partitions_request_type = vmware_vi.UpdateDiskPartitionsRequestType() # UpdateDiskPartitionsRequestType | 

    try:
        # Changes the partitions on the disk by supplying a partition specification and the device name. 
        api_instance.host_storage_system_update_disk_partitions(mo_id, update_disk_partitions_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_disk_partitions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_disk_partitions_request_type** | [**UpdateDiskPartitionsRequestType**](UpdateDiskPartitionsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidArgument***: if the spec is invalid.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_hpp_multipath_lun_policy**
> host_storage_system_update_hpp_multipath_lun_policy(mo_id, update_hpp_multipath_lun_policy_request_type)

Updates the path selection policy for a HPP claimed Logical Unit. 

Updates the path selection policy for a HPP claimed Logical Unit.  Use the LUN uuid from *HostMultipathInfoLogicalUnit*.  ***Since:*** vSphere API 7.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_hpp_multipath_lun_policy_request_type import UpdateHppMultipathLunPolicyRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_hpp_multipath_lun_policy_request_type = vmware_vi.UpdateHppMultipathLunPolicyRequestType() # UpdateHppMultipathLunPolicyRequestType | 

    try:
        # Updates the path selection policy for a HPP claimed Logical Unit. 
        api_instance.host_storage_system_update_hpp_multipath_lun_policy(mo_id, update_hpp_multipath_lun_policy_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_hpp_multipath_lun_policy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_hpp_multipath_lun_policy_request_type** | [**UpdateHppMultipathLunPolicyRequestType**](UpdateHppMultipathLunPolicyRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the LUN could not be found.  ***InvalidArgument***: if the policy is invalid.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_advanced_options**
> host_storage_system_update_internet_scsi_advanced_options(mo_id, update_internet_scsi_advanced_options_request_type)

Updates the advanced options the iSCSI host bus adapter or the discovery addresses and targets associated with it. 

Updates the advanced options the iSCSI host bus adapter or the discovery addresses and targets associated with it.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_advanced_options_request_type import UpdateInternetScsiAdvancedOptionsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_advanced_options_request_type = vmware_vi.UpdateInternetScsiAdvancedOptionsRequestType() # UpdateInternetScsiAdvancedOptionsRequestType | 

    try:
        # Updates the advanced options the iSCSI host bus adapter or the discovery addresses and targets associated with it. 
        api_instance.host_storage_system_update_internet_scsi_advanced_options(mo_id, update_internet_scsi_advanced_options_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_advanced_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_advanced_options_request_type** | [**UpdateInternetScsiAdvancedOptionsRequestType**](UpdateInternetScsiAdvancedOptionsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_alias**
> host_storage_system_update_internet_scsi_alias(mo_id, update_internet_scsi_alias_request_type)

Updates the alias of an iSCSI host bus adapter. 

Updates the alias of an iSCSI host bus adapter.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_alias_request_type import UpdateInternetScsiAliasRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_alias_request_type = vmware_vi.UpdateInternetScsiAliasRequestType() # UpdateInternetScsiAliasRequestType | 

    try:
        # Updates the alias of an iSCSI host bus adapter. 
        api_instance.host_storage_system_update_internet_scsi_alias(mo_id, update_internet_scsi_alias_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_alias: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_alias_request_type** | [**UpdateInternetScsiAliasRequestType**](UpdateInternetScsiAliasRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_authentication_properties**
> host_storage_system_update_internet_scsi_authentication_properties(mo_id, update_internet_scsi_authentication_properties_request_type)

Updates the authentication properties for one or more targets or discovery addresses associated with an iSCSI host bus adapter. 

Updates the authentication properties for one or more targets or discovery addresses associated with an iSCSI host bus adapter.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_authentication_properties_request_type import UpdateInternetScsiAuthenticationPropertiesRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_authentication_properties_request_type = vmware_vi.UpdateInternetScsiAuthenticationPropertiesRequestType() # UpdateInternetScsiAuthenticationPropertiesRequestType | 

    try:
        # Updates the authentication properties for one or more targets or discovery addresses associated with an iSCSI host bus adapter. 
        api_instance.host_storage_system_update_internet_scsi_authentication_properties(mo_id, update_internet_scsi_authentication_properties_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_authentication_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_authentication_properties_request_type** | [**UpdateInternetScsiAuthenticationPropertiesRequestType**](UpdateInternetScsiAuthenticationPropertiesRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_digest_properties**
> host_storage_system_update_internet_scsi_digest_properties(mo_id, update_internet_scsi_digest_properties_request_type)

Updates the digest properties for the iSCSI host bus adapter or the discovery addresses and targets associated with it. 

Updates the digest properties for the iSCSI host bus adapter or the discovery addresses and targets associated with it.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_digest_properties_request_type import UpdateInternetScsiDigestPropertiesRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_digest_properties_request_type = vmware_vi.UpdateInternetScsiDigestPropertiesRequestType() # UpdateInternetScsiDigestPropertiesRequestType | 

    try:
        # Updates the digest properties for the iSCSI host bus adapter or the discovery addresses and targets associated with it. 
        api_instance.host_storage_system_update_internet_scsi_digest_properties(mo_id, update_internet_scsi_digest_properties_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_digest_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_digest_properties_request_type** | [**UpdateInternetScsiDigestPropertiesRequestType**](UpdateInternetScsiDigestPropertiesRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_discovery_properties**
> host_storage_system_update_internet_scsi_discovery_properties(mo_id, update_internet_scsi_discovery_properties_request_type)

Updates the Discovery properties for an iSCSI host bus adapter. 

Updates the Discovery properties for an iSCSI host bus adapter.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_discovery_properties_request_type import UpdateInternetScsiDiscoveryPropertiesRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_discovery_properties_request_type = vmware_vi.UpdateInternetScsiDiscoveryPropertiesRequestType() # UpdateInternetScsiDiscoveryPropertiesRequestType | 

    try:
        # Updates the Discovery properties for an iSCSI host bus adapter. 
        api_instance.host_storage_system_update_internet_scsi_discovery_properties(mo_id, update_internet_scsi_discovery_properties_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_discovery_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_discovery_properties_request_type** | [**UpdateInternetScsiDiscoveryPropertiesRequestType**](UpdateInternetScsiDiscoveryPropertiesRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_ip_properties**
> host_storage_system_update_internet_scsi_ip_properties(mo_id, update_internet_scsi_ip_properties_request_type)

Updates the IP properties for an iSCSI host bus adapter. 

Updates the IP properties for an iSCSI host bus adapter.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_ip_properties_request_type import UpdateInternetScsiIPPropertiesRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_ip_properties_request_type = vmware_vi.UpdateInternetScsiIPPropertiesRequestType() # UpdateInternetScsiIPPropertiesRequestType | 

    try:
        # Updates the IP properties for an iSCSI host bus adapter. 
        api_instance.host_storage_system_update_internet_scsi_ip_properties(mo_id, update_internet_scsi_ip_properties_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_ip_properties: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_ip_properties_request_type** | [**UpdateInternetScsiIPPropertiesRequestType**](UpdateInternetScsiIPPropertiesRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_internet_scsi_name**
> host_storage_system_update_internet_scsi_name(mo_id, update_internet_scsi_name_request_type)

Updates the name of an iSCSI host bus adapter. 

Updates the name of an iSCSI host bus adapter.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_internet_scsi_name_request_type import UpdateInternetScsiNameRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_internet_scsi_name_request_type = vmware_vi.UpdateInternetScsiNameRequestType() # UpdateInternetScsiNameRequestType | 

    try:
        # Updates the name of an iSCSI host bus adapter. 
        api_instance.host_storage_system_update_internet_scsi_name(mo_id, update_internet_scsi_name_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_internet_scsi_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_internet_scsi_name_request_type** | [**UpdateInternetScsiNameRequestType**](UpdateInternetScsiNameRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the host bus adapter could not be found.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_scsi_lun_display_name**
> host_storage_system_update_scsi_lun_display_name(mo_id, update_scsi_lun_display_name_request_type)

Update the mutable display name associated with a ScsiLun. 

Update the mutable display name associated with a ScsiLun.  The ScsiLun to be updated is identified using the specified uuid.  ***Since:*** vSphere API 4.0  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_scsi_lun_display_name_request_type import UpdateScsiLunDisplayNameRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_scsi_lun_display_name_request_type = vmware_vi.UpdateScsiLunDisplayNameRequestType() # UpdateScsiLunDisplayNameRequestType | 

    try:
        # Update the mutable display name associated with a ScsiLun. 
        api_instance.host_storage_system_update_scsi_lun_display_name(mo_id, update_scsi_lun_display_name_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_scsi_lun_display_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_scsi_lun_display_name_request_type** | [**UpdateScsiLunDisplayNameRequestType**](UpdateScsiLunDisplayNameRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the device could not be found.  ***InvalidName***: if the name does not meet name restrictions such as an 80 character limit.  ***DuplicateName***: if the name does not name uniqueness restrictions. Name uniqueness restrictions will vary based on the context in which this method is invoked.  When this method is invoked on a host directly, no uniqueness checks will be performed on the name.  When this method is invoked on a VC server, uniqueness checks will be performed on the name. The uniqueness check will ensure that the name is unique with respect to the entire VC instance.  ***HostConfigFault***: for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_software_internet_scsi_enabled**
> host_storage_system_update_software_internet_scsi_enabled(mo_id, update_software_internet_scsi_enabled_request_type)

Enables or disables Software iSCSI. 

Enables or disables Software iSCSI.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_software_internet_scsi_enabled_request_type import UpdateSoftwareInternetScsiEnabledRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_software_internet_scsi_enabled_request_type = vmware_vi.UpdateSoftwareInternetScsiEnabledRequestType() # UpdateSoftwareInternetScsiEnabledRequestType | 

    try:
        # Enables or disables Software iSCSI. 
        api_instance.host_storage_system_update_software_internet_scsi_enabled(mo_id, update_software_internet_scsi_enabled_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_software_internet_scsi_enabled: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_software_internet_scsi_enabled_request_type** | [**UpdateSoftwareInternetScsiEnabledRequestType**](UpdateSoftwareInternetScsiEnabledRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: for any configuration failure.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_vmfs_unmap_bandwidth**
> host_storage_system_update_vmfs_unmap_bandwidth(mo_id, update_vmfs_unmap_bandwidth_request_type)

Update VMFS unmap bandwidth. 

Update VMFS unmap bandwidth.  This API updates the value of *VmfsUnmapBandwidthSpec.policy*, *VmfsUnmapBandwidthSpec.fixedValue*, *VmfsUnmapBandwidthSpec.dynamicMin*, *VmfsUnmapBandwidthSpec.dynamicMax*.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_vmfs_unmap_bandwidth_request_type import UpdateVmfsUnmapBandwidthRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_vmfs_unmap_bandwidth_request_type = vmware_vi.UpdateVmfsUnmapBandwidthRequestType() # UpdateVmfsUnmapBandwidthRequestType | 

    try:
        # Update VMFS unmap bandwidth. 
        api_instance.host_storage_system_update_vmfs_unmap_bandwidth(mo_id, update_vmfs_unmap_bandwidth_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_vmfs_unmap_bandwidth: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_vmfs_unmap_bandwidth_request_type** | [**UpdateVmfsUnmapBandwidthRequestType**](UpdateVmfsUnmapBandwidthRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_update_vmfs_unmap_priority**
> host_storage_system_update_vmfs_unmap_priority(mo_id, update_vmfs_unmap_priority_request_type)

Update VMFS unmap priority. 

Update VMFS unmap priority.  This API updates the value of *HostVmfsVolume.unmapPriority*.  ***Since:*** vSphere API 6.5  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.update_vmfs_unmap_priority_request_type import UpdateVmfsUnmapPriorityRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    update_vmfs_unmap_priority_request_type = vmware_vi.UpdateVmfsUnmapPriorityRequestType() # UpdateVmfsUnmapPriorityRequestType | 

    try:
        # Update VMFS unmap priority. 
        api_instance.host_storage_system_update_vmfs_unmap_priority(mo_id, update_vmfs_unmap_priority_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_update_vmfs_unmap_priority: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **update_vmfs_unmap_priority_request_type** | [**UpdateVmfsUnmapPriorityRequestType**](UpdateVmfsUnmapPriorityRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_upgrade_vm_layout**
> host_storage_system_upgrade_vm_layout(mo_id)

Iterates over all registered virtual machines. 

Iterates over all registered virtual machines.  For each VM which .vmx file is located on the service console and all disks are available on VMFS3 or NAS, it will relocate the disks into directories if stored in the ROOT, and relocate the VMX file into the directory too. Events are logged for each virtual machine that is relocated.  On ESXi systems, this operation has no effect.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Iterates over all registered virtual machines. 
        api_instance.host_storage_system_upgrade_vm_layout(mo_id)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_upgrade_vm_layout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_storage_system_upgrade_vmfs**
> host_storage_system_upgrade_vmfs(mo_id, upgrade_vmfs_request_type)

Upgrades the VMFS to the *latest supported VMFS version*. 

Upgrades the VMFS to the *latest supported VMFS version*.  Prerequisite:   All hosts that have mounted the volume must support the VMFS version to which the volume will be upgraded.  ***Required privileges:*** Host.Config.Storage 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.upgrade_vmfs_request_type import UpgradeVmfsRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostStorageSystemApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upgrade_vmfs_request_type = vmware_vi.UpgradeVmfsRequestType() # UpgradeVmfsRequestType | 

    try:
        # Upgrades the VMFS to the *latest supported VMFS version*. 
        api_instance.host_storage_system_upgrade_vmfs(mo_id, upgrade_vmfs_request_type)
    except Exception as e:
        print("Exception when calling HostStorageSystemApi->host_storage_system_upgrade_vmfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upgrade_vmfs_request_type** | [**UpgradeVmfsRequestType**](UpgradeVmfsRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***NotFound***: if the VMFS cannot be found or is unmounted.  ***HostConfigFault***: if the prerequisite is not satisfied or for all other configuration failures.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

