# vmware_vi.VirtualMachineApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_acquire_mks_ticket**](VirtualMachineApi.md#virtual_machine_acquire_mks_ticket) | **POST** /VirtualMachine/{moId}/AcquireMksTicket | Creates and returns a one-time credential used in establishing a remote mouse-keyboard-screen connection to this virtual machine. 
[**virtual_machine_acquire_ticket**](VirtualMachineApi.md#virtual_machine_acquire_ticket) | **POST** /VirtualMachine/{moId}/AcquireTicket | Creates and returns a one-time credential used in establishing a specific connection to this virtual machine, for example, a ticket type of mks can be used to establish a remote mouse-keyboard-screen connection. 
[**virtual_machine_answer_vm**](VirtualMachineApi.md#virtual_machine_answer_vm) | **POST** /VirtualMachine/{moId}/AnswerVM | Responds to a question that is blocking this virtual machine. 
[**virtual_machine_apply_evc_mode_vm_task**](VirtualMachineApi.md#virtual_machine_apply_evc_mode_vm_task) | **POST** /VirtualMachine/{moId}/ApplyEvcModeVM_Task | Applies the EVC mode masks to the virtual machine. 
[**virtual_machine_attach_disk_task**](VirtualMachineApi.md#virtual_machine_attach_disk_task) | **POST** /VirtualMachine/{moId}/AttachDisk_Task | Attach an existing disk to this virtual machine. 
[**virtual_machine_check_customization_spec**](VirtualMachineApi.md#virtual_machine_check_customization_spec) | **POST** /VirtualMachine/{moId}/CheckCustomizationSpec | Checks the customization specification against the virtual machine configuration. 
[**virtual_machine_clone_vm_task**](VirtualMachineApi.md#virtual_machine_clone_vm_task) | **POST** /VirtualMachine/{moId}/CloneVM_Task | Creates a clone of this virtual machine. 
[**virtual_machine_consolidate_vm_disks_task**](VirtualMachineApi.md#virtual_machine_consolidate_vm_disks_task) | **POST** /VirtualMachine/{moId}/ConsolidateVMDisks_Task | Consolidate the virtual disk files of the virtual machine by finding hierarchies of redo logs that can be combined without violating data dependency. 
[**virtual_machine_create_screenshot_task**](VirtualMachineApi.md#virtual_machine_create_screenshot_task) | **POST** /VirtualMachine/{moId}/CreateScreenshot_Task | Create a screen shot of a virtual machine. 
[**virtual_machine_create_secondary_vm_task**](VirtualMachineApi.md#virtual_machine_create_secondary_vm_task) | **POST** /VirtualMachine/{moId}/CreateSecondaryVM_Task | Creates a secondary virtual machine to be part of this fault tolerant group. 
[**virtual_machine_create_secondary_vmex_task**](VirtualMachineApi.md#virtual_machine_create_secondary_vmex_task) | **POST** /VirtualMachine/{moId}/CreateSecondaryVMEx_Task | Creates a secondary virtual machine to be part of this fault tolerant group. 
[**virtual_machine_create_snapshot_ex_task**](VirtualMachineApi.md#virtual_machine_create_snapshot_ex_task) | **POST** /VirtualMachine/{moId}/CreateSnapshotEx_Task | Creates a new snapshot of this virtual machine. 
[**virtual_machine_create_snapshot_task**](VirtualMachineApi.md#virtual_machine_create_snapshot_task) | **POST** /VirtualMachine/{moId}/CreateSnapshot_Task | Creates a new snapshot of this virtual machine. 
[**virtual_machine_crypto_unlock_task**](VirtualMachineApi.md#virtual_machine_crypto_unlock_task) | **POST** /VirtualMachine/{moId}/CryptoUnlock_Task | Unlocks an encrypted virtual machine by sending the encryption keys for the Virtual Machine Home and all the Virtual Disks to the ESX Server. 
[**virtual_machine_customize_vm_task**](VirtualMachineApi.md#virtual_machine_customize_vm_task) | **POST** /VirtualMachine/{moId}/CustomizeVM_Task | Customizes a virtual machine&#39;s guest operating system. 
[**virtual_machine_defragment_all_disks**](VirtualMachineApi.md#virtual_machine_defragment_all_disks) | **POST** /VirtualMachine/{moId}/DefragmentAllDisks | Defragment all virtual disks attached to this virtual machine. 
[**virtual_machine_destroy_task**](VirtualMachineApi.md#virtual_machine_destroy_task) | **POST** /VirtualMachine/{moId}/Destroy_Task | Destroys this object, deleting its contents and removing it from its parent folder (if any). 
[**virtual_machine_detach_disk_task**](VirtualMachineApi.md#virtual_machine_detach_disk_task) | **POST** /VirtualMachine/{moId}/DetachDisk_Task | Detach a disk from this virtual machine. 
[**virtual_machine_disable_secondary_vm_task**](VirtualMachineApi.md#virtual_machine_disable_secondary_vm_task) | **POST** /VirtualMachine/{moId}/DisableSecondaryVM_Task | Disables the specified secondary virtual machine in this fault tolerant group. 
[**virtual_machine_drop_connections**](VirtualMachineApi.md#virtual_machine_drop_connections) | **POST** /VirtualMachine/{moId}/DropConnections | Force the virtual machine to drop the specified connections. 
[**virtual_machine_enable_secondary_vm_task**](VirtualMachineApi.md#virtual_machine_enable_secondary_vm_task) | **POST** /VirtualMachine/{moId}/EnableSecondaryVM_Task | Enables the specified secondary virtual machine in this fault tolerant group. 
[**virtual_machine_estimate_storage_for_consolidate_snapshots_task**](VirtualMachineApi.md#virtual_machine_estimate_storage_for_consolidate_snapshots_task) | **POST** /VirtualMachine/{moId}/EstimateStorageForConsolidateSnapshots_Task | Estimate the temporary space required to consolidation disk files. 
[**virtual_machine_export_vm**](VirtualMachineApi.md#virtual_machine_export_vm) | **POST** /VirtualMachine/{moId}/ExportVm | Obtains an export lease on this virtual machine. 
[**virtual_machine_extract_ovf_environment**](VirtualMachineApi.md#virtual_machine_extract_ovf_environment) | **POST** /VirtualMachine/{moId}/ExtractOvfEnvironment | Returns the OVF environment for a virtual machine. 
[**virtual_machine_get_alarm_actions_enabled**](VirtualMachineApi.md#virtual_machine_get_alarm_actions_enabled) | **GET** /VirtualMachine/{moId}/alarmActionsEnabled | Whether alarm actions are enabled for this entity. 
[**virtual_machine_get_available_field**](VirtualMachineApi.md#virtual_machine_get_available_field) | **GET** /VirtualMachine/{moId}/availableField | List of custom field definitions that are valid for the object&#39;s type. 
[**virtual_machine_get_capability**](VirtualMachineApi.md#virtual_machine_get_capability) | **GET** /VirtualMachine/{moId}/capability | Information about the runtime capabilities of this virtual machine. 
[**virtual_machine_get_config**](VirtualMachineApi.md#virtual_machine_get_config) | **GET** /VirtualMachine/{moId}/config | Configuration of this virtual machine, including the name and UUID. 
[**virtual_machine_get_config_issue**](VirtualMachineApi.md#virtual_machine_get_config_issue) | **GET** /VirtualMachine/{moId}/configIssue | Current configuration issues that have been detected for this entity. 
[**virtual_machine_get_config_status**](VirtualMachineApi.md#virtual_machine_get_config_status) | **GET** /VirtualMachine/{moId}/configStatus | The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
[**virtual_machine_get_custom_value**](VirtualMachineApi.md#virtual_machine_get_custom_value) | **GET** /VirtualMachine/{moId}/customValue | Custom field values. 
[**virtual_machine_get_datastore**](VirtualMachineApi.md#virtual_machine_get_datastore) | **GET** /VirtualMachine/{moId}/datastore | A collection of references to the subset of datastore objects in the datacenter that is used by this virtual machine. 
[**virtual_machine_get_declared_alarm_state**](VirtualMachineApi.md#virtual_machine_get_declared_alarm_state) | **GET** /VirtualMachine/{moId}/declaredAlarmState | A set of alarm states for alarms that apply to this managed entity. 
[**virtual_machine_get_disabled_method**](VirtualMachineApi.md#virtual_machine_get_disabled_method) | **GET** /VirtualMachine/{moId}/disabledMethod | List of operations that are disabled, given the current runtime state of the entity. 
[**virtual_machine_get_effective_role**](VirtualMachineApi.md#virtual_machine_get_effective_role) | **GET** /VirtualMachine/{moId}/effectiveRole | Access rights the current session has to this entity. 
[**virtual_machine_get_environment_browser**](VirtualMachineApi.md#virtual_machine_get_environment_browser) | **GET** /VirtualMachine/{moId}/environmentBrowser | The current virtual machine&#39;s environment browser object. 
[**virtual_machine_get_guest**](VirtualMachineApi.md#virtual_machine_get_guest) | **GET** /VirtualMachine/{moId}/guest | Information about VMware Tools and about the virtual machine from the perspective of VMware Tools. 
[**virtual_machine_get_guest_heartbeat_status**](VirtualMachineApi.md#virtual_machine_get_guest_heartbeat_status) | **GET** /VirtualMachine/{moId}/guestHeartbeatStatus | The guest heartbeat. 
[**virtual_machine_get_layout**](VirtualMachineApi.md#virtual_machine_get_layout) | **GET** /VirtualMachine/{moId}/layout | Detailed information about the files that comprise this virtual machine. 
[**virtual_machine_get_layout_ex**](VirtualMachineApi.md#virtual_machine_get_layout_ex) | **GET** /VirtualMachine/{moId}/layoutEx | Detailed information about the files that comprise this virtual machine. 
[**virtual_machine_get_name**](VirtualMachineApi.md#virtual_machine_get_name) | **GET** /VirtualMachine/{moId}/name | Name of this entity, unique relative to its parent. 
[**virtual_machine_get_network**](VirtualMachineApi.md#virtual_machine_get_network) | **GET** /VirtualMachine/{moId}/network | A collection of references to the subset of network objects in the datacenter that is used by this virtual machine. 
[**virtual_machine_get_overall_status**](VirtualMachineApi.md#virtual_machine_get_overall_status) | **GET** /VirtualMachine/{moId}/overallStatus | General health of this managed entity. 
[**virtual_machine_get_parent**](VirtualMachineApi.md#virtual_machine_get_parent) | **GET** /VirtualMachine/{moId}/parent | Parent of this entity. 
[**virtual_machine_get_parent_v_app**](VirtualMachineApi.md#virtual_machine_get_parent_v_app) | **GET** /VirtualMachine/{moId}/parentVApp | Reference to the parent vApp. 
[**virtual_machine_get_permission**](VirtualMachineApi.md#virtual_machine_get_permission) | **GET** /VirtualMachine/{moId}/permission | List of permissions defined for this entity. 
[**virtual_machine_get_recent_task**](VirtualMachineApi.md#virtual_machine_get_recent_task) | **GET** /VirtualMachine/{moId}/recentTask | The set of recent tasks operating on this managed entity. 
[**virtual_machine_get_resource_config**](VirtualMachineApi.md#virtual_machine_get_resource_config) | **GET** /VirtualMachine/{moId}/resourceConfig | The resource configuration for a virtual machine. 
[**virtual_machine_get_resource_pool**](VirtualMachineApi.md#virtual_machine_get_resource_pool) | **GET** /VirtualMachine/{moId}/resourcePool | The current resource pool that specifies resource allocation for this virtual machine. 
[**virtual_machine_get_root_snapshot**](VirtualMachineApi.md#virtual_machine_get_root_snapshot) | **GET** /VirtualMachine/{moId}/rootSnapshot | The roots of all snapshot trees for the virtual machine. 
[**virtual_machine_get_runtime**](VirtualMachineApi.md#virtual_machine_get_runtime) | **GET** /VirtualMachine/{moId}/runtime | Execution state and history for this virtual machine. 
[**virtual_machine_get_snapshot**](VirtualMachineApi.md#virtual_machine_get_snapshot) | **GET** /VirtualMachine/{moId}/snapshot | Current snapshot and tree. 
[**virtual_machine_get_storage**](VirtualMachineApi.md#virtual_machine_get_storage) | **GET** /VirtualMachine/{moId}/storage | Storage space used by the virtual machine, split by datastore. 
[**virtual_machine_get_summary**](VirtualMachineApi.md#virtual_machine_get_summary) | **GET** /VirtualMachine/{moId}/summary | Basic information about this virtual machine. 
[**virtual_machine_get_tag**](VirtualMachineApi.md#virtual_machine_get_tag) | **GET** /VirtualMachine/{moId}/tag | The set of tags associated with this managed entity. 
[**virtual_machine_get_triggered_alarm_state**](VirtualMachineApi.md#virtual_machine_get_triggered_alarm_state) | **GET** /VirtualMachine/{moId}/triggeredAlarmState | A set of alarm states for alarms triggered by this entity or by its descendants. 
[**virtual_machine_get_value**](VirtualMachineApi.md#virtual_machine_get_value) | **GET** /VirtualMachine/{moId}/value | List of custom field values. 
[**virtual_machine_instant_clone_task**](VirtualMachineApi.md#virtual_machine_instant_clone_task) | **POST** /VirtualMachine/{moId}/InstantClone_Task | Creates a powered-on Instant Clone of a virtual machine. 
[**virtual_machine_make_primary_vm_task**](VirtualMachineApi.md#virtual_machine_make_primary_vm_task) | **POST** /VirtualMachine/{moId}/MakePrimaryVM_Task | Makes the specified secondary virtual machine from this fault tolerant group as the primary virtual machine. 
[**virtual_machine_mark_as_template**](VirtualMachineApi.md#virtual_machine_mark_as_template) | **POST** /VirtualMachine/{moId}/MarkAsTemplate | Marks a VirtualMachine object as being used as a template. 
[**virtual_machine_mark_as_virtual_machine**](VirtualMachineApi.md#virtual_machine_mark_as_virtual_machine) | **POST** /VirtualMachine/{moId}/MarkAsVirtualMachine | Clears the &#39;isTemplate&#39; flag and reassociates the virtual machine with a resource pool and host. 
[**virtual_machine_migrate_vm_task**](VirtualMachineApi.md#virtual_machine_migrate_vm_task) | **POST** /VirtualMachine/{moId}/MigrateVM_Task | Migrates a virtual machine&#39;s execution to a specific resource pool or host. 
[**virtual_machine_mount_tools_installer**](VirtualMachineApi.md#virtual_machine_mount_tools_installer) | **POST** /VirtualMachine/{moId}/MountToolsInstaller | Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system. 
[**virtual_machine_power_off_vm_task**](VirtualMachineApi.md#virtual_machine_power_off_vm_task) | **POST** /VirtualMachine/{moId}/PowerOffVM_Task | Powers off this virtual machine. 
[**virtual_machine_power_on_vm_task**](VirtualMachineApi.md#virtual_machine_power_on_vm_task) | **POST** /VirtualMachine/{moId}/PowerOnVM_Task | Powers on this virtual machine. 
[**virtual_machine_promote_disks_task**](VirtualMachineApi.md#virtual_machine_promote_disks_task) | **POST** /VirtualMachine/{moId}/PromoteDisks_Task | Promotes disks on this virtual machine that have delta disk backings. 
[**virtual_machine_put_usb_scan_codes**](VirtualMachineApi.md#virtual_machine_put_usb_scan_codes) | **POST** /VirtualMachine/{moId}/PutUsbScanCodes | Inject a sequence of USB HID scan codes into the keyboard. 
[**virtual_machine_query_changed_disk_areas**](VirtualMachineApi.md#virtual_machine_query_changed_disk_areas) | **POST** /VirtualMachine/{moId}/QueryChangedDiskAreas | Get a list of areas of a virtual disk belonging to this VM that have been modified since a well-defined point in the past. 
[**virtual_machine_query_connections**](VirtualMachineApi.md#virtual_machine_query_connections) | **POST** /VirtualMachine/{moId}/QueryConnections | Ask the virtual machine for a list of connections. 
[**virtual_machine_query_fault_tolerance_compatibility**](VirtualMachineApi.md#virtual_machine_query_fault_tolerance_compatibility) | **POST** /VirtualMachine/{moId}/QueryFaultToleranceCompatibility | This API can be invoked to determine whether a virtual machine is compatible for legacy Fault Tolerance. 
[**virtual_machine_query_fault_tolerance_compatibility_ex**](VirtualMachineApi.md#virtual_machine_query_fault_tolerance_compatibility_ex) | **POST** /VirtualMachine/{moId}/QueryFaultToleranceCompatibilityEx | This API can be invoked to determine whether a virtual machine is compatible for Fault Tolerance. 
[**virtual_machine_query_unowned_files**](VirtualMachineApi.md#virtual_machine_query_unowned_files) | **POST** /VirtualMachine/{moId}/QueryUnownedFiles | For all files that belong to the vm, check that the file owner is set to the current datastore principal user, as set by *HostDatastoreSystem.ConfigureDatastorePrincipal* 
[**virtual_machine_reboot_guest**](VirtualMachineApi.md#virtual_machine_reboot_guest) | **POST** /VirtualMachine/{moId}/RebootGuest | Issues a command to the guest operating system asking it to perform a reboot. 
[**virtual_machine_reconfig_vm_task**](VirtualMachineApi.md#virtual_machine_reconfig_vm_task) | **POST** /VirtualMachine/{moId}/ReconfigVM_Task | Reconfigures this virtual machine. 
[**virtual_machine_refresh_storage_info**](VirtualMachineApi.md#virtual_machine_refresh_storage_info) | **POST** /VirtualMachine/{moId}/RefreshStorageInfo | Explicitly refreshes the storage information of this virtual machine, updating properties *VirtualMachine.storage*, *VirtualMachine.layoutEx* and *VirtualMachineSummary.storage*. 
[**virtual_machine_reload**](VirtualMachineApi.md#virtual_machine_reload) | **POST** /VirtualMachine/{moId}/Reload | Reload the entity state. 
[**virtual_machine_reload_virtual_machine_from_path_task**](VirtualMachineApi.md#virtual_machine_reload_virtual_machine_from_path_task) | **POST** /VirtualMachine/{moId}/reloadVirtualMachineFromPath_Task | Reloads the configuration for this virtual machine from a given datastore path. 
[**virtual_machine_relocate_vm_task**](VirtualMachineApi.md#virtual_machine_relocate_vm_task) | **POST** /VirtualMachine/{moId}/RelocateVM_Task | Relocates a virtual machine to the location specified by *VirtualMachineRelocateSpec*. 
[**virtual_machine_remove_all_snapshots_task**](VirtualMachineApi.md#virtual_machine_remove_all_snapshots_task) | **POST** /VirtualMachine/{moId}/RemoveAllSnapshots_Task | Remove all the snapshots associated with this virtual machine. 
[**virtual_machine_rename_task**](VirtualMachineApi.md#virtual_machine_rename_task) | **POST** /VirtualMachine/{moId}/Rename_Task | Renames this managed entity. 
[**virtual_machine_reset_guest_information**](VirtualMachineApi.md#virtual_machine_reset_guest_information) | **POST** /VirtualMachine/{moId}/ResetGuestInformation | Clears cached guest information. 
[**virtual_machine_reset_vm_task**](VirtualMachineApi.md#virtual_machine_reset_vm_task) | **POST** /VirtualMachine/{moId}/ResetVM_Task | Resets power on this virtual machine. 
[**virtual_machine_revert_to_current_snapshot_task**](VirtualMachineApi.md#virtual_machine_revert_to_current_snapshot_task) | **POST** /VirtualMachine/{moId}/RevertToCurrentSnapshot_Task | Reverts the virtual machine to the current snapshot. 
[**virtual_machine_send_nmi**](VirtualMachineApi.md#virtual_machine_send_nmi) | **POST** /VirtualMachine/{moId}/SendNMI | Send a non-maskable interrupt (NMI). 
[**virtual_machine_set_custom_value**](VirtualMachineApi.md#virtual_machine_set_custom_value) | **POST** /VirtualMachine/{moId}/setCustomValue | Assigns a value to a custom field. 
[**virtual_machine_set_display_topology**](VirtualMachineApi.md#virtual_machine_set_display_topology) | **POST** /VirtualMachine/{moId}/SetDisplayTopology | Sets the console window&#39;s display topology as specified. 
[**virtual_machine_set_screen_resolution**](VirtualMachineApi.md#virtual_machine_set_screen_resolution) | **POST** /VirtualMachine/{moId}/SetScreenResolution | Sets the console window&#39;s resolution as specified. 
[**virtual_machine_shutdown_guest**](VirtualMachineApi.md#virtual_machine_shutdown_guest) | **POST** /VirtualMachine/{moId}/ShutdownGuest | Issues a command to the guest operating system asking it to perform a clean shutdown of all services. 
[**virtual_machine_standby_guest**](VirtualMachineApi.md#virtual_machine_standby_guest) | **POST** /VirtualMachine/{moId}/StandbyGuest | Issues a command to the guest operating system asking it to prepare for a suspend operation. 
[**virtual_machine_start_recording_task**](VirtualMachineApi.md#virtual_machine_start_recording_task) | **POST** /VirtualMachine/{moId}/StartRecording_Task | Initiates a recording session on this virtual machine. 
[**virtual_machine_start_replaying_task**](VirtualMachineApi.md#virtual_machine_start_replaying_task) | **POST** /VirtualMachine/{moId}/StartReplaying_Task | Starts a replay session on this virtual machine. 
[**virtual_machine_stop_recording_task**](VirtualMachineApi.md#virtual_machine_stop_recording_task) | **POST** /VirtualMachine/{moId}/StopRecording_Task | Stops a currently active recording session on this virtual machine. 
[**virtual_machine_stop_replaying_task**](VirtualMachineApi.md#virtual_machine_stop_replaying_task) | **POST** /VirtualMachine/{moId}/StopReplaying_Task | Stops a replay session on this virtual machine. 
[**virtual_machine_suspend_vm_task**](VirtualMachineApi.md#virtual_machine_suspend_vm_task) | **POST** /VirtualMachine/{moId}/SuspendVM_Task | Suspends execution in this virtual machine. 
[**virtual_machine_terminate_fault_tolerant_vm_task**](VirtualMachineApi.md#virtual_machine_terminate_fault_tolerant_vm_task) | **POST** /VirtualMachine/{moId}/TerminateFaultTolerantVM_Task | Terminates the specified secondary virtual machine in a fault tolerant group. 
[**virtual_machine_terminate_vm**](VirtualMachineApi.md#virtual_machine_terminate_vm) | **POST** /VirtualMachine/{moId}/TerminateVM | Do an immediate power off of a VM. 
[**virtual_machine_turn_off_fault_tolerance_for_vm_task**](VirtualMachineApi.md#virtual_machine_turn_off_fault_tolerance_for_vm_task) | **POST** /VirtualMachine/{moId}/TurnOffFaultToleranceForVM_Task | Removes all secondary virtual machines associated with the fault tolerant group and turns off protection for this virtual machine. 
[**virtual_machine_unmount_tools_installer**](VirtualMachineApi.md#virtual_machine_unmount_tools_installer) | **POST** /VirtualMachine/{moId}/UnmountToolsInstaller | Unmounts VMware Tools installer CD. 
[**virtual_machine_unregister_vm**](VirtualMachineApi.md#virtual_machine_unregister_vm) | **POST** /VirtualMachine/{moId}/UnregisterVM | Removes this virtual machine from the inventory without removing any of the virtual machine&#39;s files on disk. 
[**virtual_machine_upgrade_tools_task**](VirtualMachineApi.md#virtual_machine_upgrade_tools_task) | **POST** /VirtualMachine/{moId}/UpgradeTools_Task | Begins the tools upgrade process. 
[**virtual_machine_upgrade_vm_task**](VirtualMachineApi.md#virtual_machine_upgrade_vm_task) | **POST** /VirtualMachine/{moId}/UpgradeVM_Task | Upgrades this virtual machine&#39;s virtual hardware to the latest revision that is supported by the virtual machine&#39;s current host. 


# **virtual_machine_acquire_mks_ticket**
> VirtualMachineMksTicket virtual_machine_acquire_mks_ticket(mo_id)

Creates and returns a one-time credential used in establishing a remote mouse-keyboard-screen connection to this virtual machine. 

Deprecated as of vSphere API 4.1, use *VirtualMachine.AcquireTicket* instead.  Creates and returns a one-time credential used in establishing a remote mouse-keyboard-screen connection to this virtual machine.  The correct function of this method depends on being able to retrieve TCP binding information about the server end of the client connection that is requesting the ticket. If such information is not available, the NotSupported fault is thrown. This method is appropriate for SOAP and authenticated connections, which are both TCP-based connections.  ***Required privileges:*** VirtualMachine.Interact.ConsoleInteract 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_mks_ticket import VirtualMachineMksTicket
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Creates and returns a one-time credential used in establishing a remote mouse-keyboard-screen connection to this virtual machine. 
        api_response = api_instance.virtual_machine_acquire_mks_ticket(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_acquire_mks_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_acquire_mks_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineMksTicket**](VirtualMachineMksTicket.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A one-time credential used in establishing a remote mouse-keyboard-screen connection.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_acquire_ticket**
> VirtualMachineTicket virtual_machine_acquire_ticket(mo_id, acquire_ticket_request_type)

Creates and returns a one-time credential used in establishing a specific connection to this virtual machine, for example, a ticket type of mks can be used to establish a remote mouse-keyboard-screen connection. 

Creates and returns a one-time credential used in establishing a specific connection to this virtual machine, for example, a ticket type of mks can be used to establish a remote mouse-keyboard-screen connection.  A client using this ticketing mechanism must have network connectivity to the ESX server where the virtual machine is running, and the ESX server must be reachable to the management client from the address made available to the client via the ticket.  Acquiring a virtual machine ticket requires different privileges depending on the types of ticket: - VirtualMachine.Interact.DeviceConnection if requesting a device   ticket. - VirtualMachine.Interact.GuestControl if requesting a guestControl   or guestIntegrity ticket. - VirtualMachine.Interact.ConsoleInteract if requesting an mks   or webmks ticket. - VirtualMachine.Interact.DnD if requesting a drag and drop   ticket.    ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.acquire_ticket_request_type import AcquireTicketRequestType
from vmware_vi.models.virtual_machine_ticket import VirtualMachineTicket
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    acquire_ticket_request_type = vmware_vi.AcquireTicketRequestType() # AcquireTicketRequestType | 

    try:
        # Creates and returns a one-time credential used in establishing a specific connection to this virtual machine, for example, a ticket type of mks can be used to establish a remote mouse-keyboard-screen connection. 
        api_response = api_instance.virtual_machine_acquire_ticket(mo_id, acquire_ticket_request_type)
        print("The response of VirtualMachineApi->virtual_machine_acquire_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_acquire_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **acquire_ticket_request_type** | [**AcquireTicketRequestType**](AcquireTicketRequestType.md)|  | 

### Return type

[**VirtualMachineTicket**](VirtualMachineTicket.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A one-time credential used in establishing a remote connection to this virtual machine.  |  -  |
**500** | ***InvalidState***: if the virtual machine is not connected.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_answer_vm**
> virtual_machine_answer_vm(mo_id, answer_vm_request_type)

Responds to a question that is blocking this virtual machine. 

Responds to a question that is blocking this virtual machine.  ***Required privileges:*** VirtualMachine.Interact.AnswerQuestion 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.answer_vm_request_type import AnswerVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    answer_vm_request_type = vmware_vi.AnswerVMRequestType() # AnswerVMRequestType | 

    try:
        # Responds to a question that is blocking this virtual machine. 
        api_instance.virtual_machine_answer_vm(mo_id, answer_vm_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_answer_vm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **answer_vm_request_type** | [**AnswerVMRequestType**](AnswerVMRequestType.md)|  | 

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
**500** | ***InvalidArgument***: if the questionId does not apply to this virtual machine. For example, this can happen if another client already answered the message.  ***ConcurrentAccess***: if the question has been or is being answered by another thread or user.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_apply_evc_mode_vm_task**
> ManagedObjectReference virtual_machine_apply_evc_mode_vm_task(mo_id, apply_evc_mode_vm_request_type)

Applies the EVC mode masks to the virtual machine. 

Applies the EVC mode masks to the virtual machine.  Existing masks will be replaced by the input masks. If the mask parameter is not set, then the masks on the virtual machine are removed. See *EVCMode.featureMask* for the list of masks to provide. These can be retrieved from *Capability.supportedEVCMode*, which is accessible in *ServiceInstance.capability*.  This operation is only supported if *VirtualMachineCapability.perVmEvcSupported* is true.  ***Since:*** vSphere API 6.7  ***Required privileges:*** VirtualMachine.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.apply_evc_mode_vm_request_type import ApplyEvcModeVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    apply_evc_mode_vm_request_type = vmware_vi.ApplyEvcModeVMRequestType() # ApplyEvcModeVMRequestType | 

    try:
        # Applies the EVC mode masks to the virtual machine. 
        api_response = api_instance.virtual_machine_apply_evc_mode_vm_task(mo_id, apply_evc_mode_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_apply_evc_mode_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_apply_evc_mode_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **apply_evc_mode_vm_request_type** | [**ApplyEvcModeVMRequestType**](ApplyEvcModeVMRequestType.md)|  | 

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
**500** | ***InvalidPowerState***: if the power state is not poweredOff.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_attach_disk_task**
> ManagedObjectReference virtual_machine_attach_disk_task(mo_id, attach_disk_request_type)

Attach an existing disk to this virtual machine. 

Attach an existing disk to this virtual machine.  A minimum virtual machine version of 'vmx-13' is required for this operation to succeed. If a compatible VM version is not satisfied, a *DeviceUnsupportedForVmVersion* fault will be thrown.  ***Since:*** vSphere API 6.5  ***Required privileges:*** VirtualMachine.Config.AddExistingDisk 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.attach_disk_request_type import AttachDiskRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    attach_disk_request_type = vmware_vi.AttachDiskRequestType() # AttachDiskRequestType | 

    try:
        # Attach an existing disk to this virtual machine. 
        api_response = api_instance.virtual_machine_attach_disk_task(mo_id, attach_disk_request_type)
        print("The response of VirtualMachineApi->virtual_machine_attach_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_attach_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **attach_disk_request_type** | [**AttachDiskRequestType**](AttachDiskRequestType.md)|  | 

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
**500** | ***NotFound***: if the disk object cannot be found.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid.  ***FileFault***: if there is a problem creating or accessing the virtual machine&#39;s files for this operation.  ***InvalidState***: if the operation cannot be performed in the current state of the virtual machine. For example, because the virtual machine&#39;s configuration is not available.  ***InvalidDatastore***: If the datastore cannot be found or inaccessible.  ***InvalidController***: If the specified controller cannot be found or the specified unitNumber is already taken, or the controller has no free slots.  ***MissingController***: If the virtual machine has no or more than one available controllers when controllerKey is unset.  ***DeviceUnsupportedForVmVersion***: If the virtual machine&#39;s version is incompatible for the given device.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_check_customization_spec**
> virtual_machine_check_customization_spec(mo_id, check_customization_spec_request_type)

Checks the customization specification against the virtual machine configuration. 

Checks the customization specification against the virtual machine configuration.  For example, this is used on a source virtual machine before a clone operation to catch customization failure before the disk copy. This checks the specification's internal consistency as well as for compatibility with this virtual machine's configuration.  ***Required privileges:*** VirtualMachine.Provisioning.Customize 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.check_customization_spec_request_type import CheckCustomizationSpecRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    check_customization_spec_request_type = vmware_vi.CheckCustomizationSpecRequestType() # CheckCustomizationSpecRequestType | 

    try:
        # Checks the customization specification against the virtual machine configuration. 
        api_instance.virtual_machine_check_customization_spec(mo_id, check_customization_spec_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_check_customization_spec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **check_customization_spec_request_type** | [**CheckCustomizationSpecRequestType**](CheckCustomizationSpecRequestType.md)|  | 

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
**500** | ***CustomizationFault***: A subclass of CustomizationFault is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_clone_vm_task**
> ManagedObjectReference virtual_machine_clone_vm_task(mo_id, clone_vm_request_type)

Creates a clone of this virtual machine. 

Creates a clone of this virtual machine.  If the virtual machine is used as a template, this method corresponds to the deploy command.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  The privilege required on the source virtual machine depends on the source and destination types: - source is virtual machine, destination is virtual machine -   VirtualMachine.Provisioning.Clone - source is virtual machine, destination is template -   VirtualMachine.Provisioning.CreateTemplateFromVM - source is template, destination is virtual machine -   VirtualMachine.Provisioning.DeployTemplate - source is template, destination is template -   VirtualMachine.Provisioning.CloneTemplate - source is encrypted virtual machine - Cryptographer.Clone    If customization is requested in the CloneSpec, then the VirtualMachine.Provisioning.Customize privilege must also be held on the source virtual machine.  The Resource.AssignVMToPool privilege is also required for the resource pool specified in the CloneSpec, if the destination is not a template. The Datastore.AllocateSpace privilege is required on all datastores where the clone is created. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.clone_vm_request_type import CloneVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    clone_vm_request_type = vmware_vi.CloneVMRequestType() # CloneVMRequestType | 

    try:
        # Creates a clone of this virtual machine. 
        api_response = api_instance.virtual_machine_clone_vm_task(mo_id, clone_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_clone_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_clone_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **clone_vm_request_type** | [**CloneVMRequestType**](CloneVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly added *VirtualMachine* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if the host cannot run this virtual machine.  ***CustomizationFault***: if a customization error happens. Typically, a specific subclass of this exception is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the operation is not supported by the current agent.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***FileFault***: if there is an error accessing the virtual machine files.  ***VmConfigFault***: if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.  ***MigrationFault***: if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***NoPermission***: if the virtual machine is encrypted, but encryption is not enabled on the destination and the user does not have Cryptographer.RegisterHost permission on the host.  ***NoPermission***: if source virtual machine is encrypted, but the the user does not have Cryptographer.Clone permission on it.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_consolidate_vm_disks_task**
> ManagedObjectReference virtual_machine_consolidate_vm_disks_task(mo_id)

Consolidate the virtual disk files of the virtual machine by finding hierarchies of redo logs that can be combined without violating data dependency. 

Consolidate the virtual disk files of the virtual machine by finding hierarchies of redo logs that can be combined without violating data dependency.  The redundant redo logs after merging are then deleted. Consolidation improves I/O performance since less number of virtual disk files need to be traversed; it also reduces the storage usage. However additional space is temporarily required to perform the operation. Use *VirtualMachine.EstimateStorageForConsolidateSnapshots_Task* to estimate the temporary space required. Consolidation can be I/O intensive, it is advisable to invoke this operation when guest is not under heavy I/O usage.  ***Since:*** vSphere API 5.0  ***Required privileges:*** VirtualMachine.State.RemoveSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Consolidate the virtual disk files of the virtual machine by finding hierarchies of redo logs that can be combined without violating data dependency. 
        api_response = api_instance.virtual_machine_consolidate_vm_disks_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_consolidate_vm_disks_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_consolidate_vm_disks_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***FileFault***: if if there is a problem creating or accessing the virtual machine&#39;s files for this operation. Typically a more specific fault for example *NoDiskSpace* is thrown.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***VmConfigFault***: if a virtual machine configuration issue prevents consolidation. Typically, a more specific fault is thrown such as *InvalidDiskFormat* if a disk cannot be read, or *InvalidSnapshotFormat* if the snapshot configuration is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_create_screenshot_task**
> ManagedObjectReference virtual_machine_create_screenshot_task(mo_id)

Create a screen shot of a virtual machine. 

Create a screen shot of a virtual machine.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.CreateScreenshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Create a screen shot of a virtual machine. 
        api_response = api_instance.virtual_machine_create_screenshot_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_create_screenshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_create_screenshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***InvalidPowerState***: if the virtual machine is not powered on.  ***InvalidState***: if the virtual machine is not ready to respond to such requests.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_create_secondary_vm_task**
> ManagedObjectReference virtual_machine_create_secondary_vm_task(mo_id, create_secondary_vm_request_type)

Creates a secondary virtual machine to be part of this fault tolerant group. 

Deprecated as of vSphere API 6.0, use *VirtualMachine.CreateSecondaryVMEx_Task* instead.  Creates a secondary virtual machine to be part of this fault tolerant group.  If a host is specified, the secondary virtual machine will be created on it. Otherwise, a host will be selected by the system.  If the primary virtual machine (i.e., this virtual machine) is powered on when the secondary is created, an attempt will be made to power on the secondary on a system selected host. If the cluster is a DRS cluster, DRS will be invoked to obtain a placement for the new secondary virtual machine. If the DRS recommendation (see *ClusterRecommendation*) is automatic, it will be automatically executed. Otherwise, the recommendation will be returned to the caller of this method and the secondary will remain powered off until the recommendation is approved using *ClusterComputeResource.ApplyRecommendation*. Failure to power on the secondary virtual machine will not fail the creation of the secondary.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.CreateSecondary 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_secondary_vm_request_type import CreateSecondaryVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_secondary_vm_request_type = vmware_vi.CreateSecondaryVMRequestType() # CreateSecondaryVMRequestType | 

    try:
        # Creates a secondary virtual machine to be part of this fault tolerant group. 
        api_response = api_instance.virtual_machine_create_secondary_vm_task(mo_id, create_secondary_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_create_secondary_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_create_secondary_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_secondary_vm_request_type** | [**CreateSecondaryVMRequestType**](CreateSecondaryVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* returns an instance of the *FaultToleranceSecondaryOpResult* data object, which contains a reference to the created *VirtualMachine* and the status of powering it on, if attempted.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the virtual machine is marked as a template, or it is not in a vSphere HA enabled cluster.  ***InvalidState***: if the virtual machine&#39;s configuration information is not available.  ***ManagedObjectNotFound***: if a host is specified and it does not exist.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like FaultToleranceNotLicensed is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  ***VmConfigFault***: if a configuration issue prevents creating the secondary. Typically, a more specific fault such as VmConfigIncompatibleForFaultTolerance is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_create_secondary_vmex_task**
> ManagedObjectReference virtual_machine_create_secondary_vmex_task(mo_id, create_secondary_vmex_request_type)

Creates a secondary virtual machine to be part of this fault tolerant group. 

Creates a secondary virtual machine to be part of this fault tolerant group.  If a host is specified, the secondary virtual machine will be created on it. Otherwise, a host will be selected by the system.  If a FaultToleranceConfigSpec is specified, the virtual machine's configuration files and disks will be created in the specified datastores.  If the primary virtual machine (i.e., this virtual machine) is powered on when the secondary is created, an attempt will be made to power on the secondary on a system selected host. If the cluster is a DRS cluster, DRS will be invoked to obtain a placement for the new secondary virtual machine. If the DRS recommendation (see *ClusterRecommendation*) is automatic, it will be automatically executed. Otherwise, the recommendation will be returned to the caller of this method and the secondary will remain powered off until the recommendation is approved using *ClusterComputeResource.ApplyRecommendation*. Failure to power on the secondary virtual machine will not fail the creation of the secondary.  ***Since:*** vSphere API 6.0  ***Required privileges:*** VirtualMachine.Interact.CreateSecondary 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_secondary_vmex_request_type import CreateSecondaryVMExRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_secondary_vmex_request_type = vmware_vi.CreateSecondaryVMExRequestType() # CreateSecondaryVMExRequestType | 

    try:
        # Creates a secondary virtual machine to be part of this fault tolerant group. 
        api_response = api_instance.virtual_machine_create_secondary_vmex_task(mo_id, create_secondary_vmex_request_type)
        print("The response of VirtualMachineApi->virtual_machine_create_secondary_vmex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_create_secondary_vmex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_secondary_vmex_request_type** | [**CreateSecondaryVMExRequestType**](CreateSecondaryVMExRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* returns an instance of the *FaultToleranceSecondaryOpResult* data object, which contains a reference to the created *VirtualMachine* and the status of powering it on, if attempted.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the virtual machine is marked as a template, or it is not in a vSphere HA enabled cluster.  ***InvalidState***: if the virtual machine&#39;s configuration information is not available.  ***ManagedObjectNotFound***: if a host is specified and it does not exist.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like FaultToleranceNotLicensed is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  ***VmConfigFault***: if a configuration issue prevents creating the secondary. Typically, a more specific fault such as VmConfigIncompatibleForFaultTolerance is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_create_snapshot_ex_task**
> ManagedObjectReference virtual_machine_create_snapshot_ex_task(mo_id, create_snapshot_ex_request_type)

Creates a new snapshot of this virtual machine. 

Creates a new snapshot of this virtual machine.  As a side effect, this updates the current snapshot.  Snapshots are not supported for Fault Tolerance primary and secondary virtual machines.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Since:*** vSphere API 6.5  ***Required privileges:*** VirtualMachine.State.CreateSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_snapshot_ex_request_type import CreateSnapshotExRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_snapshot_ex_request_type = vmware_vi.CreateSnapshotExRequestType() # CreateSnapshotExRequestType | 

    try:
        # Creates a new snapshot of this virtual machine. 
        api_response = api_instance.virtual_machine_create_snapshot_ex_task(mo_id, create_snapshot_ex_request_type)
        print("The response of VirtualMachineApi->virtual_machine_create_snapshot_ex_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_create_snapshot_ex_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_snapshot_ex_request_type** | [**CreateSnapshotExRequestType**](CreateSnapshotExRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly created *VirtualMachineSnapshot* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: if quiesceSpec is invalid.  ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support snapshots or if the host does not support quiesced snapshots and the quiesce spec is set; or if the virtual machine is a Fault Tolerance primary or secondary; or if an unsupported quiesce spec is set.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically a more specific fault like MultipleSnapshotsNotSupported is thrown.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid. Typically, a more specific fault like InvalidSnapshotState is thrown.  ***InvalidName***: if the specified snapshot name is invalid.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_create_snapshot_task**
> ManagedObjectReference virtual_machine_create_snapshot_task(mo_id, create_snapshot_request_type)

Creates a new snapshot of this virtual machine. 

Deprecated as of vSphere 8.0GA, this method is deprecated. Please use *VirtualMachine.CreateSnapshotEx_Task* instead.  Creates a new snapshot of this virtual machine.  As a side effect, this updates the current snapshot.  Snapshots are not supported for Fault Tolerance primary and secondary virtual machines.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  ***Required privileges:*** VirtualMachine.State.CreateSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.create_snapshot_request_type import CreateSnapshotRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    create_snapshot_request_type = vmware_vi.CreateSnapshotRequestType() # CreateSnapshotRequestType | 

    try:
        # Creates a new snapshot of this virtual machine. 
        api_response = api_instance.virtual_machine_create_snapshot_task(mo_id, create_snapshot_request_type)
        print("The response of VirtualMachineApi->virtual_machine_create_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_create_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **create_snapshot_request_type** | [**CreateSnapshotRequestType**](CreateSnapshotRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly created *VirtualMachineSnapshot* upon success.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support snapshots or if the host does not support quiesced snapshots and the quiesce parameter is set to true; or if the virtual machine is a Fault Tolerance primary or secondary  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically a more specific fault like MultipleSnapshotsNotSupported is thrown.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid. Typically, a more specific fault like InvalidSnapshotState is thrown.  ***InvalidName***: if the specified snapshot name is invalid.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_crypto_unlock_task**
> ManagedObjectReference virtual_machine_crypto_unlock_task(mo_id)

Unlocks an encrypted virtual machine by sending the encryption keys for the Virtual Machine Home and all the Virtual Disks to the ESX Server. 

Unlocks an encrypted virtual machine by sending the encryption keys for the Virtual Machine Home and all the Virtual Disks to the ESX Server.  ***Since:*** vSphere API 6.7  ***Required privileges:*** Cryptographer.RegisterVM 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Unlocks an encrypted virtual machine by sending the encryption keys for the Virtual Machine Home and all the Virtual Disks to the ESX Server. 
        api_response = api_instance.virtual_machine_crypto_unlock_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_crypto_unlock_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_crypto_unlock_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: when the required Key Management Server is not configured.  ***InvalidVmState***: when the virtual machine failed to unlock.  ***NotSupported***: if the ESX server doesn&#39;t support encryption.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_customize_vm_task**
> ManagedObjectReference virtual_machine_customize_vm_task(mo_id, customize_vm_request_type)

Customizes a virtual machine's guest operating system. 

Customizes a virtual machine's guest operating system.  ***Required privileges:*** VirtualMachine.Provisioning.Customize 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.customize_vm_request_type import CustomizeVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    customize_vm_request_type = vmware_vi.CustomizeVMRequestType() # CustomizeVMRequestType | 

    try:
        # Customizes a virtual machine's guest operating system. 
        api_response = api_instance.virtual_machine_customize_vm_task(mo_id, customize_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_customize_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_customize_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **customize_vm_request_type** | [**CustomizeVMRequestType**](CustomizeVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***CustomizationFault***: A subclass of CustomizationFault is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_defragment_all_disks**
> virtual_machine_defragment_all_disks(mo_id)

Defragment all virtual disks attached to this virtual machine. 

Defragment all virtual disks attached to this virtual machine.  ***Since:*** VI API 2.5  ***Required privileges:*** VirtualMachine.Interact.DefragmentAllDisks 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Defragment all virtual disks attached to this virtual machine. 
        api_instance.virtual_machine_defragment_all_disks(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_defragment_all_disks: %s\n" % e)
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
**500** | ***InvalidState***: if the virtual machine is not connected.  ***InvalidPowerState***: if the virtual machine is poweredOn.  ***TaskInProgress***: if the virtual machine is busy.  ***FileFault***: if there is an error accessing the disk files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_destroy_task**
> ManagedObjectReference virtual_machine_destroy_task(mo_id)

Destroys this object, deleting its contents and removing it from its parent folder (if any). 

Destroys this object, deleting its contents and removing it from its parent folder (if any).  NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself. This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.  ***Required privileges:*** VirtualMachine.Inventory.Delete 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Destroys this object, deleting its contents and removing it from its parent folder (if any). 
        api_response = api_instance.virtual_machine_destroy_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_destroy_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_destroy_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | Failure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_detach_disk_task**
> ManagedObjectReference virtual_machine_detach_disk_task(mo_id, detach_disk_request_type)

Detach a disk from this virtual machine. 

Detach a disk from this virtual machine.  ***Since:*** vSphere API 6.5  ***Required privileges:*** VirtualMachine.Config.RemoveDisk 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.detach_disk_request_type import DetachDiskRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    detach_disk_request_type = vmware_vi.DetachDiskRequestType() # DetachDiskRequestType | 

    try:
        # Detach a disk from this virtual machine. 
        api_response = api_instance.virtual_machine_detach_disk_task(mo_id, detach_disk_request_type)
        print("The response of VirtualMachineApi->virtual_machine_detach_disk_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_detach_disk_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **detach_disk_request_type** | [**DetachDiskRequestType**](DetachDiskRequestType.md)|  | 

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
**500** | ***NotFound***: if the disk object cannot be found.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid.  ***FileFault***: if there is a problem creating or accessing the virtual machine&#39;s files for this operation.  ***InvalidState***: if the operation cannot be performed in the current state of the virtual machine. For example, because the virtual machine&#39;s configuration is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_disable_secondary_vm_task**
> ManagedObjectReference virtual_machine_disable_secondary_vm_task(mo_id, disable_secondary_vm_request_type)

Disables the specified secondary virtual machine in this fault tolerant group. 

Disables the specified secondary virtual machine in this fault tolerant group.  The specified secondary will not be automatically started on a subsequent power-on of the primary virtual machine. This operation could leave the primary virtual machine in a non-fault tolerant state.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.DisableSecondary 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disable_secondary_vm_request_type import DisableSecondaryVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    disable_secondary_vm_request_type = vmware_vi.DisableSecondaryVMRequestType() # DisableSecondaryVMRequestType | 

    try:
        # Disables the specified secondary virtual machine in this fault tolerant group. 
        api_response = api_instance.virtual_machine_disable_secondary_vm_task(mo_id, disable_secondary_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_disable_secondary_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_disable_secondary_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **disable_secondary_vm_request_type** | [**DisableSecondaryVMRequestType**](DisableSecondaryVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_drop_connections**
> bool virtual_machine_drop_connections(mo_id, drop_connections_request_type)

Force the virtual machine to drop the specified connections. 

Force the virtual machine to drop the specified connections.  Attempt to drop the specified virtual machine connections. An attempt will be made to drop all of the specified connections before returning.  ***Since:*** vSphere API 7.0.1.0  ***Required privileges:*** VirtualMachine.Interact.ConsoleInteract 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.drop_connections_request_type import DropConnectionsRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    drop_connections_request_type = vmware_vi.DropConnectionsRequestType() # DropConnectionsRequestType | 

    try:
        # Force the virtual machine to drop the specified connections. 
        api_response = api_instance.virtual_machine_drop_connections(mo_id, drop_connections_request_type)
        print("The response of VirtualMachineApi->virtual_machine_drop_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_drop_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **drop_connections_request_type** | [**DropConnectionsRequestType**](DropConnectionsRequestType.md)|  | 

### Return type

**bool**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | true All of the specified connections have been dropped.  |  -  |
**500** | ***InvalidPowerState***: If the virtual machine is not powered on. No connection drop actions will have been attempted if this is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_enable_secondary_vm_task**
> ManagedObjectReference virtual_machine_enable_secondary_vm_task(mo_id, enable_secondary_vm_request_type)

Enables the specified secondary virtual machine in this fault tolerant group. 

Enables the specified secondary virtual machine in this fault tolerant group.  This operation is used to enable a secondary virtual machine that was previously disabled by the *VirtualMachine.DisableSecondaryVM_Task* call. The specified secondary will be automatically started whenever the primary is powered on.  If the primary virtual machine (i.e., this virtual machine) is powered on when the secondary is enabled, an attempt will be made to power on the secondary. If a host was specified in the method call, this host will be used. If a host is not specified, one will be selected by the system. In the latter case, if the cluster is a DRS cluster, DRS will be invoked to obtain a placement for the new secondary virtual machine. If the DRS recommendation (see *ClusterRecommendation*) is automatic, it will be executed. Otherwise, the recommendation will be returned to the caller of this method and the secondary will remain powered off until the recommendation is approved using *ClusterComputeResource.ApplyRecommendation*.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.EnableSecondary 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.enable_secondary_vm_request_type import EnableSecondaryVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    enable_secondary_vm_request_type = vmware_vi.EnableSecondaryVMRequestType() # EnableSecondaryVMRequestType | 

    try:
        # Enables the specified secondary virtual machine in this fault tolerant group. 
        api_response = api_instance.virtual_machine_enable_secondary_vm_task(mo_id, enable_secondary_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_enable_secondary_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_enable_secondary_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **enable_secondary_vm_request_type** | [**EnableSecondaryVMRequestType**](EnableSecondaryVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* returns an instance of the *FaultToleranceSecondaryOpResult* data object, which contains a reference to the *VirtualMachine* and the status of powering it on, if attempted.  Refers instance of *Task*.  |  -  |
**500** | ***VmConfigFault***: if a configuration issue prevents enabling the secondary. Typically, a more specific fault such as VmConfigIncompatibleForFaultTolerance is thrown.  ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***ManagedObjectNotFound***: if a host is specified and it does not exist.  ***InvalidState***: if the virtual machine&#39;s configuration information is not available, if the secondary virtual machine is not disabled, or if a power-on is attempted and one is already in progress.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_estimate_storage_for_consolidate_snapshots_task**
> ManagedObjectReference virtual_machine_estimate_storage_for_consolidate_snapshots_task(mo_id)

Estimate the temporary space required to consolidation disk files. 

Estimate the temporary space required to consolidation disk files.  The estimation is a lower bound if the childmost writable disk file will be consolidated for an online virtual machine, it is accurate for all other situations. This is because the space requirement depending on the size of the childmost disk file and how write intensive the guest is.  This method can be used prior to invoke consolidation via *VirtualMachine.ConsolidateVMDisks_Task*.  ***Since:*** vSphere API 5.0  ***Required privileges:*** VirtualMachine.State.RemoveSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Estimate the temporary space required to consolidation disk files. 
        api_response = api_instance.virtual_machine_estimate_storage_for_consolidate_snapshots_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_estimate_storage_for_consolidate_snapshots_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_estimate_storage_for_consolidate_snapshots_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***FileFault***: if if there is a problem accessing the virtual machine&#39;s files for this operation. Typically a more specific fault *FileLocked* is thrown.  ***VmConfigFault***: if a virtual machine configuration issue prevents the estimation. Typically, a more specific fault is thrown.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_export_vm**
> ManagedObjectReference virtual_machine_export_vm(mo_id)

Obtains an export lease on this virtual machine. 

Obtains an export lease on this virtual machine.  The export lease contains a list of URLs for the virtual disks for this virtual machine, as well as a ticket giving access to the URLs.  See *HttpNfcLease* for information on how to use the lease.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.Export 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Obtains an export lease on this virtual machine. 
        api_response = api_instance.virtual_machine_export_vm(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_export_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_export_vm: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export lease on this *VirtualMachine*. The export task continues running until the lease is completed by the caller.  Refers instance of *HttpNfcLease*.  |  -  |
**500** | ***InvalidPowerState***: if the virtual machine is powered on.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***FileFault***: if there is an error accessing the virtual machine files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_extract_ovf_environment**
> str virtual_machine_extract_ovf_environment(mo_id)

Returns the OVF environment for a virtual machine. 

Returns the OVF environment for a virtual machine.  If the virtual machine has no vApp configuration, an empty string is returned. Also, sensitive information is omitted, so this method is not guaranteed to return the complete OVF environment.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VApp.ExtractOvfEnvironment 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Returns the OVF environment for a virtual machine. 
        api_response = api_instance.virtual_machine_extract_ovf_environment(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_extract_ovf_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_extract_ovf_environment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidState***: if the virtual machine is not running  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_alarm_actions_enabled**
> bool virtual_machine_get_alarm_actions_enabled(mo_id)

Whether alarm actions are enabled for this entity. 

Whether alarm actions are enabled for this entity.  True if enabled; false otherwise.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Whether alarm actions are enabled for this entity. 
        api_response = api_instance.virtual_machine_get_alarm_actions_enabled(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_alarm_actions_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_alarm_actions_enabled: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**bool**

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

# **virtual_machine_get_available_field**
> List[CustomFieldDef] virtual_machine_get_available_field(mo_id)

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field definitions that are valid for the object's type. 
        api_response = api_instance.virtual_machine_get_available_field(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_available_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_available_field: %s\n" % e)
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

# **virtual_machine_get_capability**
> VirtualMachineCapability virtual_machine_get_capability(mo_id)

Information about the runtime capabilities of this virtual machine. 

Information about the runtime capabilities of this virtual machine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_capability import VirtualMachineCapability
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about the runtime capabilities of this virtual machine. 
        api_response = api_instance.virtual_machine_get_capability(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_capability: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineCapability**](VirtualMachineCapability.md)

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

# **virtual_machine_get_config**
> VirtualMachineConfigInfo virtual_machine_get_config(mo_id)

Configuration of this virtual machine, including the name and UUID. 

Configuration of this virtual machine, including the name and UUID.  This property is set when a virtual machine is created or when the *reconfigVM* method is called.  The virtual machine configuration is not guaranteed to be available. For example, the configuration information would be unavailable if the server is unable to access the virtual machine files on disk, and is often also unavailable during the initial phases of virtual machine creation. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_config_info import VirtualMachineConfigInfo
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of this virtual machine, including the name and UUID. 
        api_response = api_instance.virtual_machine_get_config(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineConfigInfo**](VirtualMachineConfigInfo.md)

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

# **virtual_machine_get_config_issue**
> List[Event] virtual_machine_get_config_issue(mo_id)

Current configuration issues that have been detected for this entity. 

Current configuration issues that have been detected for this entity.  Typically, these issues have already been logged as events. The entity stores these events as long as they are still current. The *configStatus* property provides an overall status based on these events. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.event import Event
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current configuration issues that have been detected for this entity. 
        api_response = api_instance.virtual_machine_get_config_issue(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_config_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_config_issue: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Event]**](Event.md)

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

# **virtual_machine_get_config_status**
> ManagedEntityStatusEnum virtual_machine_get_config_status(mo_id)

The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 

The configStatus indicates whether or not the system has detected a configuration issue involving this entity.  For example, it might have detected a duplicate IP address or MAC address, or a host in a cluster might be out of compliance. The meanings of the configStatus values are: - red: A problem has been detected involving the entity. - yellow: A problem is about to occur or a transient condition   has occurred (For example, reconfigure fail-over policy). - green: No configuration issues have been detected. - gray: The configuration status of the entity is not being monitored.    A green status indicates only that a problem has not been detected; it is not a guarantee that the entity is problem-free.  The *configIssue* property contains a list of the problems that have been detected. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The configStatus indicates whether or not the system has detected a configuration issue involving this entity. 
        api_response = api_instance.virtual_machine_get_config_status(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_config_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_config_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md)

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

# **virtual_machine_get_custom_value**
> List[CustomFieldValue] virtual_machine_get_custom_value(mo_id)

Custom field values. 

Custom field values.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Custom field values. 
        api_response = api_instance.virtual_machine_get_custom_value(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_custom_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_custom_value: %s\n" % e)
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

# **virtual_machine_get_datastore**
> List[ManagedObjectReference] virtual_machine_get_datastore(mo_id)

A collection of references to the subset of datastore objects in the datacenter that is used by this virtual machine. 

A collection of references to the subset of datastore objects in the datacenter that is used by this virtual machine.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A collection of references to the subset of datastore objects in the datacenter that is used by this virtual machine. 
        api_response = api_instance.virtual_machine_get_datastore(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_datastore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_datastore: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *Datastore*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_declared_alarm_state**
> List[AlarmState] virtual_machine_get_declared_alarm_state(mo_id)

A set of alarm states for alarms that apply to this managed entity. 

A set of alarm states for alarms that apply to this managed entity.  The set includes alarms defined on this entity and alarms inherited from the parent entity, or from any ancestors in the inventory hierarchy.  Alarms are inherited if they can be triggered by this entity or its descendants. This set does not include alarms that are defined on descendants of this entity.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_state import AlarmState
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms that apply to this managed entity. 
        api_response = api_instance.virtual_machine_get_declared_alarm_state(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_declared_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_declared_alarm_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AlarmState]**](AlarmState.md)

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

# **virtual_machine_get_disabled_method**
> List[str] virtual_machine_get_disabled_method(mo_id)

List of operations that are disabled, given the current runtime state of the entity. 

List of operations that are disabled, given the current runtime state of the entity.  For example, a power-on operation always fails if a virtual machine is already powered on. This list can be used by clients to enable or disable operations in a graphical user interface.  Note: This list is determined by the current runtime state of an entity, not by its permissions.  This list may include the following operations for a HostSystem: - *HostSystem.EnterMaintenanceMode_Task* - *HostSystem.ExitMaintenanceMode_Task* - *HostSystem.RebootHost_Task* - *HostSystem.ShutdownHost_Task* - *HostSystem.ReconnectHost_Task* - *HostSystem.DisconnectHost_Task*    This list may include the following operations for a VirtualMachine: - *VirtualMachine.AnswerVM* - *ManagedEntity.Rename_Task* - *VirtualMachine.CloneVM_Task* - *VirtualMachine.PowerOffVM_Task* - *VirtualMachine.PowerOnVM_Task* - *VirtualMachine.SuspendVM_Task* - *VirtualMachine.ResetVM_Task* - *VirtualMachine.ReconfigVM_Task* - *VirtualMachine.RelocateVM_Task* - *VirtualMachine.MigrateVM_Task* - *VirtualMachine.CustomizeVM_Task* - *VirtualMachine.ShutdownGuest* - *VirtualMachine.StandbyGuest* - *VirtualMachine.RebootGuest* - *VirtualMachine.CreateSnapshot_Task* - *VirtualMachine.RemoveAllSnapshots_Task* - *VirtualMachine.RevertToCurrentSnapshot_Task* - *VirtualMachine.MarkAsTemplate* - *VirtualMachine.MarkAsVirtualMachine* - *VirtualMachine.ResetGuestInformation* - *VirtualMachine.MountToolsInstaller* - *VirtualMachine.UnmountToolsInstaller* - *ManagedEntity.Destroy_Task* - *VirtualMachine.UpgradeVM_Task* - *VirtualMachine.ExportVm*    This list may include the following operations for a ResourcePool: - *ResourcePool.ImportVApp* - *ResourcePool.CreateChildVM_Task* - *ResourcePool.UpdateConfig* - *Folder.CreateVM_Task* - *ManagedEntity.Destroy_Task* - *ManagedEntity.Rename_Task*    This list may include the following operations for a VirtualApp: - *ManagedEntity.Destroy_Task* - *VirtualApp.CloneVApp_Task* - *VirtualApp.unregisterVApp_Task* - *VirtualApp.ExportVApp* - *VirtualApp.PowerOnVApp_Task* - *VirtualApp.PowerOffVApp_Task* - *VirtualApp.UpdateVAppConfig*    In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of operations that are disabled, given the current runtime state of the entity. 
        api_response = api_instance.virtual_machine_get_disabled_method(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_disabled_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_disabled_method: %s\n" % e)
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

# **virtual_machine_get_effective_role**
> List[int] virtual_machine_get_effective_role(mo_id)

Access rights the current session has to this entity. 

Access rights the current session has to this entity.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Access rights the current session has to this entity. 
        api_response = api_instance.virtual_machine_get_effective_role(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_effective_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_effective_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**List[int]**

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

# **virtual_machine_get_environment_browser**
> ManagedObjectReference virtual_machine_get_environment_browser(mo_id)

The current virtual machine's environment browser object. 

The current virtual machine's environment browser object.  This contains information on all the configurations that can be used on the virtual machine. This is identical to the environment browser on the *ComputeResource* to which this virtual machine belongs. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The current virtual machine's environment browser object. 
        api_response = api_instance.virtual_machine_get_environment_browser(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_environment_browser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_environment_browser: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *EnvironmentBrowser*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_guest**
> GuestInfo virtual_machine_get_guest(mo_id)

Information about VMware Tools and about the virtual machine from the perspective of VMware Tools. 

Information about VMware Tools and about the virtual machine from the perspective of VMware Tools.  Information about the guest operating system is available in VirtualCenter. Guest operating system information reflects the last known state of the virtual machine. For powered on machines, this is current information. For powered off machines, this is the last recorded state before the virtual machine was powered off. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.guest_info import GuestInfo
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Information about VMware Tools and about the virtual machine from the perspective of VMware Tools. 
        api_response = api_instance.virtual_machine_get_guest(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_guest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_guest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**GuestInfo**](GuestInfo.md)

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

# **virtual_machine_get_guest_heartbeat_status**
> ManagedEntityStatusEnum virtual_machine_get_guest_heartbeat_status(mo_id)

The guest heartbeat. 

The guest heartbeat.  The heartbeat status is classified as: - gray - VMware Tools are not installed or not running. - red - No heartbeat. Guest operating system may have stopped responding. - yellow - Intermittent heartbeat. May be due to guest load. - green - Guest operating system is responding normally.    The guest heartbeat is a statistics metric. Alarms can be configured on this metric to trigger emails or other actions. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The guest heartbeat. 
        api_response = api_instance.virtual_machine_get_guest_heartbeat_status(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_guest_heartbeat_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_guest_heartbeat_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md)

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

# **virtual_machine_get_layout**
> VirtualMachineFileLayout virtual_machine_get_layout(mo_id)

Detailed information about the files that comprise this virtual machine. 

Deprecated as of vSphere API 4.0, use *VirtualMachine.layoutEx* instead. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  Detailed information about the files that comprise this virtual machine. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_file_layout import VirtualMachineFileLayout
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Detailed information about the files that comprise this virtual machine. 
        api_response = api_instance.virtual_machine_get_layout(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_layout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_layout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineFileLayout**](VirtualMachineFileLayout.md)

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

# **virtual_machine_get_layout_ex**
> VirtualMachineFileLayoutEx virtual_machine_get_layout_ex(mo_id)

Detailed information about the files that comprise this virtual machine. 

Detailed information about the files that comprise this virtual machine.  Can be explicitly refreshed by the *VirtualMachine.RefreshStorageInfo* operation. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_file_layout_ex import VirtualMachineFileLayoutEx
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Detailed information about the files that comprise this virtual machine. 
        api_response = api_instance.virtual_machine_get_layout_ex(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_layout_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_layout_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineFileLayoutEx**](VirtualMachineFileLayoutEx.md)

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

# **virtual_machine_get_name**
> str virtual_machine_get_name(mo_id)

Name of this entity, unique relative to its parent. 

Name of this entity, unique relative to its parent.  Any / (slash), \\\\ (backslash), character used in this name element will be escaped. Similarly, any % (percent) character used in this name element will be escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.  ***Required privileges:*** System.View 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Name of this entity, unique relative to its parent. 
        api_response = api_instance.virtual_machine_get_name(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

**str**

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

# **virtual_machine_get_network**
> List[ManagedObjectReference] virtual_machine_get_network(mo_id)

A collection of references to the subset of network objects in the datacenter that is used by this virtual machine. 

A collection of references to the subset of network objects in the datacenter that is used by this virtual machine.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A collection of references to the subset of network objects in the datacenter that is used by this virtual machine. 
        api_response = api_instance.virtual_machine_get_network(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_network: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *Network*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_overall_status**
> ManagedEntityStatusEnum virtual_machine_get_overall_status(mo_id)

General health of this managed entity. 

General health of this managed entity.  The overall status of the managed entity is computed as the worst status among its alarms and the configuration issues detected on the entity. The status is reported as one of the following values: - red: The entity has alarms or configuration issues with a red status. - yellow: The entity does not have alarms or configuration issues with a   red status, and has at least one with a yellow status. - green: The entity does not have alarms or configuration issues with a   red or yellow status, and has at least one with a green status. - gray: All of the entity's alarms have a gray status and the   configuration status of the entity is not being monitored.    In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # General health of this managed entity. 
        api_response = api_instance.virtual_machine_get_overall_status(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_overall_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_overall_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md)

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

# **virtual_machine_get_parent**
> ManagedObjectReference virtual_machine_get_parent(mo_id)

Parent of this entity. 

Parent of this entity.  This value is null for the root object and for *VirtualMachine* objects that are part of a *VirtualApp*.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Parent of this entity. 
        api_response = api_instance.virtual_machine_get_parent(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_parent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_parent: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_parent_v_app**
> ManagedObjectReference virtual_machine_get_parent_v_app(mo_id)

Reference to the parent vApp. 

Reference to the parent vApp.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reference to the parent vApp. 
        api_response = api_instance.virtual_machine_get_parent_v_app(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_parent_v_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_parent_v_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *ManagedEntity*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_permission**
> List[Permission] virtual_machine_get_permission(mo_id)

List of permissions defined for this entity. 

List of permissions defined for this entity. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.permission import Permission
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of permissions defined for this entity. 
        api_response = api_instance.virtual_machine_get_permission(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_permission: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Permission]**](Permission.md)

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

# **virtual_machine_get_recent_task**
> List[ManagedObjectReference] virtual_machine_get_recent_task(mo_id)

The set of recent tasks operating on this managed entity. 

The set of recent tasks operating on this managed entity.  This is a subset of *TaskManager.recentTask* belong to this entity. A task in this list could be in one of the four states: pending, running, success or error.  This property can be used to deduce intermediate power states for a virtual machine entity. For example, if the current powerState is \"poweredOn\" and there is a running task performing the \"suspend\" operation, then the virtual machine's intermediate state might be described as \"suspending.\"  Most tasks (such as power operations) obtain exclusive access to the virtual machine, so it is unusual for this list to contain more than one running task. One exception, however, is the task of cloning a virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of recent tasks operating on this managed entity. 
        api_response = api_instance.virtual_machine_get_recent_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_recent_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_recent_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *Task*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_resource_config**
> ResourceConfigSpec virtual_machine_get_resource_config(mo_id)

The resource configuration for a virtual machine. 

The resource configuration for a virtual machine.  The shares in this specification are evaluated relative to the resource pool to which it is assigned. This will return null if the product the virtual machine is registered on does not support resource configuration.  To retrieve the configuration, you typically use *childConfiguration*.  To change the configuration, use *ResourcePool.UpdateChildResourceConfiguration*. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.resource_config_spec import ResourceConfigSpec
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The resource configuration for a virtual machine. 
        api_response = api_instance.virtual_machine_get_resource_config(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_resource_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_resource_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ResourceConfigSpec**](ResourceConfigSpec.md)

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

# **virtual_machine_get_resource_pool**
> ManagedObjectReference virtual_machine_get_resource_pool(mo_id)

The current resource pool that specifies resource allocation for this virtual machine. 

The current resource pool that specifies resource allocation for this virtual machine.  This property is set when a virtual machine is created or associated with a different resource pool.  Returns null if the virtual machine is a template or the session has no access to the resource pool. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The current resource pool that specifies resource allocation for this virtual machine. 
        api_response = api_instance.virtual_machine_get_resource_pool(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_resource_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_resource_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instance of *ResourcePool*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_root_snapshot**
> List[ManagedObjectReference] virtual_machine_get_root_snapshot(mo_id)

The roots of all snapshot trees for the virtual machine. 

The roots of all snapshot trees for the virtual machine.  ***Since:*** vSphere API 4.1 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The roots of all snapshot trees for the virtual machine. 
        api_response = api_instance.virtual_machine_get_root_snapshot(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_root_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_root_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[ManagedObjectReference]**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refers instances of *VirtualMachineSnapshot*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_get_runtime**
> VirtualMachineRuntimeInfo virtual_machine_get_runtime(mo_id)

Execution state and history for this virtual machine. 

Execution state and history for this virtual machine.  The contents of this property change when: - the virtual machine's power state changes. - an execution message is pending. - an event occurs. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_runtime_info import VirtualMachineRuntimeInfo
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Execution state and history for this virtual machine. 
        api_response = api_instance.virtual_machine_get_runtime(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_runtime: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineRuntimeInfo**](VirtualMachineRuntimeInfo.md)

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

# **virtual_machine_get_snapshot**
> VirtualMachineSnapshotInfo virtual_machine_get_snapshot(mo_id)

Current snapshot and tree. 

Current snapshot and tree.  The property is valid if snapshots have been created for this virtual machine.  The contents of this property change in response to the methods: - *createSnapshot* - *revertToCurrentSnapshot* - *remove* - *revert* - *removeAllSnapshots* 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_snapshot_info import VirtualMachineSnapshotInfo
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Current snapshot and tree. 
        api_response = api_instance.virtual_machine_get_snapshot(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineSnapshotInfo**](VirtualMachineSnapshotInfo.md)

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

# **virtual_machine_get_storage**
> VirtualMachineStorageInfo virtual_machine_get_storage(mo_id)

Storage space used by the virtual machine, split by datastore. 

Storage space used by the virtual machine, split by datastore.  Can be explicitly refreshed by the *VirtualMachine.RefreshStorageInfo* operation. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Since:*** vSphere API 4.0 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_storage_info import VirtualMachineStorageInfo
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Storage space used by the virtual machine, split by datastore. 
        api_response = api_instance.virtual_machine_get_storage(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_storage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineStorageInfo**](VirtualMachineStorageInfo.md)

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

# **virtual_machine_get_summary**
> VirtualMachineSummary virtual_machine_get_summary(mo_id)

Basic information about this virtual machine. 

Basic information about this virtual machine.  This includes: - runtimeInfo - guest - basic configuration - alarms - performance information 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_summary import VirtualMachineSummary
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Basic information about this virtual machine. 
        api_response = api_instance.virtual_machine_get_summary(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**VirtualMachineSummary**](VirtualMachineSummary.md)

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

# **virtual_machine_get_tag**
> List[Tag] virtual_machine_get_tag(mo_id)

The set of tags associated with this managed entity. 

The set of tags associated with this managed entity.  Experimental. Subject to change.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.tag import Tag
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # The set of tags associated with this managed entity. 
        api_response = api_instance.virtual_machine_get_tag(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[Tag]**](Tag.md)

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

# **virtual_machine_get_triggered_alarm_state**
> List[AlarmState] virtual_machine_get_triggered_alarm_state(mo_id)

A set of alarm states for alarms triggered by this entity or by its descendants. 

A set of alarm states for alarms triggered by this entity or by its descendants.  Triggered alarms are propagated up the inventory hierarchy so that a user can readily tell when a descendant has triggered an alarm. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.  ***Required privileges:*** System.View 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.alarm_state import AlarmState
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # A set of alarm states for alarms triggered by this entity or by its descendants. 
        api_response = api_instance.virtual_machine_get_triggered_alarm_state(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_triggered_alarm_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_triggered_alarm_state: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[AlarmState]**](AlarmState.md)

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

# **virtual_machine_get_value**
> List[CustomFieldValue] virtual_machine_get_value(mo_id)

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # List of custom field values. 
        api_response = api_instance.virtual_machine_get_value(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_get_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_get_value: %s\n" % e)
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

# **virtual_machine_instant_clone_task**
> ManagedObjectReference virtual_machine_instant_clone_task(mo_id, instant_clone_request_type)

Creates a powered-on Instant Clone of a virtual machine. 

Creates a powered-on Instant Clone of a virtual machine.  The new virtual machine will be created on the same host and start with the identical running point as the original virtual machine, sharing memory state when possible and sharing disk state. The original virtual machine must be in a powered-on state. The privilege required for Instant Clone operation are: - VirtualMachine.Provisioning.Clone - VirtualMachine.Interact.PowerOn - VirtualMachine.Inventory.CreateFromExisting - Datastore.AllocateSpace - Resource.AssignVMToPool    ***Since:*** vSphere API 6.7  ***Required privileges:*** VirtualMachine.Provisioning.Clone 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.instant_clone_request_type import InstantCloneRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    instant_clone_request_type = vmware_vi.InstantCloneRequestType() # InstantCloneRequestType | 

    try:
        # Creates a powered-on Instant Clone of a virtual machine. 
        api_response = api_instance.virtual_machine_instant_clone_task(mo_id, instant_clone_request_type)
        print("The response of VirtualMachineApi->virtual_machine_instant_clone_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_instant_clone_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **instant_clone_request_type** | [**InstantCloneRequestType**](InstantCloneRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: in the following cases: - Source virtual machine is not powered on - Source virtual machine configuration is not supported for   Instant Clone operation - Relocation specification has unsupported settings     ***InvalidState***: if the operation cannot be performed because of the host or virtual machine&#39;s current state. For example, if the host is in maintenance mode or if the source virtual machine is not powered on.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***FileFault***: if there is an error accessing the virtual machine files.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***DisallowedMigrationDeviceAttached***: if any of the devices attached to the source virtual machine are not supported for the Instant Clone operation or if device change specification contains changes that are not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_make_primary_vm_task**
> ManagedObjectReference virtual_machine_make_primary_vm_task(mo_id, make_primary_vm_request_type)

Makes the specified secondary virtual machine from this fault tolerant group as the primary virtual machine. 

Makes the specified secondary virtual machine from this fault tolerant group as the primary virtual machine.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.MakePrimary 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.make_primary_vm_request_type import MakePrimaryVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    make_primary_vm_request_type = vmware_vi.MakePrimaryVMRequestType() # MakePrimaryVMRequestType | 

    try:
        # Makes the specified secondary virtual machine from this fault tolerant group as the primary virtual machine. 
        api_response = api_instance.virtual_machine_make_primary_vm_task(mo_id, make_primary_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_make_primary_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_make_primary_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **make_primary_vm_request_type** | [**MakePrimaryVMRequestType**](MakePrimaryVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_mark_as_template**
> virtual_machine_mark_as_template(mo_id)

Marks a VirtualMachine object as being used as a template. 

Marks a VirtualMachine object as being used as a template.  Note: A VirtualMachine marked as a template cannot be powered on.  ***Required privileges:*** VirtualMachine.Provisioning.MarkAsTemplate 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Marks a VirtualMachine object as being used as a template. 
        api_instance.virtual_machine_mark_as_template(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_mark_as_template: %s\n" % e)
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
**500** | ***NotSupported***: if marking a virtual machine as a template is not supported.  ***InvalidPowerState***: if the virtual machine is not powered off.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  ***VmConfigFault***: if the template is incompatible with the host, such as the files are not accessible.  ***FileFault***: if there is an error accessing the virtual machine files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_mark_as_virtual_machine**
> virtual_machine_mark_as_virtual_machine(mo_id, mark_as_virtual_machine_request_type)

Clears the 'isTemplate' flag and reassociates the virtual machine with a resource pool and host. 

Clears the 'isTemplate' flag and reassociates the virtual machine with a resource pool and host.  ***Required privileges:*** VirtualMachine.Provisioning.MarkAsVM 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.mark_as_virtual_machine_request_type import MarkAsVirtualMachineRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    mark_as_virtual_machine_request_type = vmware_vi.MarkAsVirtualMachineRequestType() # MarkAsVirtualMachineRequestType | 

    try:
        # Clears the 'isTemplate' flag and reassociates the virtual machine with a resource pool and host. 
        api_instance.virtual_machine_mark_as_virtual_machine(mo_id, mark_as_virtual_machine_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_mark_as_virtual_machine: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **mark_as_virtual_machine_request_type** | [**MarkAsVirtualMachineRequestType**](MarkAsVirtualMachineRequestType.md)|  | 

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
**500** | ***NotSupported***: if marking a template as a virtual machine is not supported.  ***InvalidState***: if the virtual machine is not marked as a template.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***VmConfigFault***: if the virtual machine is not compatible with the host. For example, a DisksNotSupported fault if the destination host does not support the disk backings of the template.  ***FileFault***: if there is an error accessing the virtual machine files.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_migrate_vm_task**
> ManagedObjectReference virtual_machine_migrate_vm_task(mo_id, migrate_vm_request_type)

Migrates a virtual machine's execution to a specific resource pool or host. 

Deprecated as of vSphere 6.5, use *VirtualMachine.RelocateVM_Task* instead.  Migrates a virtual machine's execution to a specific resource pool or host.  Requires Resource.HotMigrate privilege if the virtual machine is powered on or Resource.ColdMigrate privilege if the virtual machine is powered off or suspended. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.migrate_vm_request_type import MigrateVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    migrate_vm_request_type = vmware_vi.MigrateVMRequestType() # MigrateVMRequestType | 

    try:
        # Migrates a virtual machine's execution to a specific resource pool or host. 
        api_response = api_instance.virtual_machine_migrate_vm_task(mo_id, migrate_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_migrate_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_migrate_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **migrate_vm_request_type** | [**MigrateVMRequestType**](MigrateVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidArgument***: in the following cases: - the target host and target pool are not associated with the   same compute resource - the host parameter is left unset when the target pool is   associated with a non-DRS cluster    ***InvalidPowerState***: if the state argument is set and the virtual machine does not have that power state.  ***FileFault***: if, in a case where the virtual machine configuration file must be copied, the destination location for that file does not have the necessary file access permissions.  ***VmConfigFault***: if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.  ***MigrationFault***: if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.  ***Timedout***: if one of the phases of the migration process times out.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state or the target host&#39;s current state. For example, if the virtual machine configuration information is not available or if the target host is disconnected or in maintenance mode.  ***NoActiveHostInCluster***: if a target host is not specified and the cluster associated with the target pool does not contain at least one potential target host. A host must be connected and not in maintenance mode in order to be considered as a potential target host.  ***NoPermission***: if the virtual machine is encrypted, but encryption is not enabled on the destination host and the user does not have Cryptographer.RegisterHost permission on it.  ***NoPermission***: if the virtual machine is encrypted, but the the user does not have Cryptographer.Migrate permission on the VM.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_mount_tools_installer**
> virtual_machine_mount_tools_installer(mo_id)

Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system. 

Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system.  To monitor the status of the tools install, clients should check the tools status, *GuestInfo.toolsVersionStatus* and *GuestInfo.toolsRunningStatus*  ***Required privileges:*** VirtualMachine.Interact.ToolsInstall 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system. 
        api_instance.virtual_machine_mount_tools_installer(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_mount_tools_installer: %s\n" % e)
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
**500** | ***InvalidState***: if the virtual machine is not running, or the VMware Tools CD is already mounted.  ***VmToolsUpgradeFault***: if the VMware Tools CD failed to mount.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_power_off_vm_task**
> ManagedObjectReference virtual_machine_power_off_vm_task(mo_id)

Powers off this virtual machine. 

Powers off this virtual machine.  If this virtual machine is a fault tolerant primary virtual machine, this will result in the secondary virtual machine(s) getting powered off as well.  ***Required privileges:*** VirtualMachine.Interact.PowerOff 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Powers off this virtual machine. 
        api_response = api_instance.virtual_machine_power_off_vm_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_power_off_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_power_off_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is not poweredOn.  ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_power_on_vm_task**
> ManagedObjectReference virtual_machine_power_on_vm_task(mo_id, power_on_vm_request_type)

Powers on this virtual machine. 

Powers on this virtual machine.  If the virtual machine is suspended, this method resumes execution from the suspend point.  When powering on a virtual machine in a cluster, the system might implicitly or due to the host argument, do an implicit relocation of the virtual machine to another host. Hence, errors related to this relocation can be thrown. If the cluster is a DRS cluster, DRS will be invoked if the virtual machine can be automatically placed by DRS (see *DrsBehavior_enum*). Because this method does not return a DRS *ClusterRecommendation*, no vmotion nor host power operations will be done as part of a DRS-facilitated power on. To have DRS consider such operations use *Datacenter.PowerOnMultiVM_Task*. As of vSphere API 5.1, use of this method with vCenter Server is deprecated; use *Datacenter.PowerOnMultiVM_Task* instead.  If this virtual machine is a fault tolerant primary virtual machine, its secondary virtual machines will be started on system-selected hosts. If the virtual machines are in a VMware DRS enabled cluster, then DRS will be invoked to obtain placements for the secondaries but no vmotion nor host power operations will be considered for these power ons.  ***Required privileges:*** VirtualMachine.Interact.PowerOn 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.power_on_vm_request_type import PowerOnVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    power_on_vm_request_type = vmware_vi.PowerOnVMRequestType() # PowerOnVMRequestType | 

    try:
        # Powers on this virtual machine. 
        api_response = api_instance.virtual_machine_power_on_vm_task(mo_id, power_on_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_power_on_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_power_on_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **power_on_vm_request_type** | [**PowerOnVMRequestType**](PowerOnVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is poweredOn.  ***TaskInProgress***: if the virtual machine is busy.  ***NotEnoughLicenses***: if there are not enough licenses to power on this virtual machine.  ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidState***: if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available or if the virtual machine is already powering on  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***VmConfigFault***: if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  ***DisallowedOperationOnFailoverHost***: if the host specified is a failover host. See *ClusterFailoverHostAdmissionControlPolicy*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_promote_disks_task**
> ManagedObjectReference virtual_machine_promote_disks_task(mo_id, promote_disks_request_type)

Promotes disks on this virtual machine that have delta disk backings. 

Promotes disks on this virtual machine that have delta disk backings.  A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.  Promoting does two things 1. If the unlink parameter is true, any disk backing which is shared    shared by multiple virtual machines is copied so that this virtual machine    has its own unshared version. Copied files always end up in the virtual    machine's home directory. To promote the disks of a powered on VM,    the VM cannot have snapshots. 2. Any disk backing which is not shared between multiple virtual    machines and is not associated with a snapshot is consolidated    with its child backing.     If the unlink parameter is true, the net effect of this operation is improved read performance, at the cost of disk space. If the unlink parameter is false the net effect is improved read performance at the cost of inhibiting future sharing.  This operation is only supported if *HostCapability.deltaDiskBackingsSupported* is true.  This operation is only supported on VirtualCenter. If no work is required, an invocation completes successfully.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Provisioning.PromoteDisks 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.promote_disks_request_type import PromoteDisksRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    promote_disks_request_type = vmware_vi.PromoteDisksRequestType() # PromoteDisksRequestType | 

    try:
        # Promotes disks on this virtual machine that have delta disk backings. 
        api_response = api_instance.virtual_machine_promote_disks_task(mo_id, promote_disks_request_type)
        print("The response of VirtualMachineApi->virtual_machine_promote_disks_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_promote_disks_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **promote_disks_request_type** | [**PromoteDisksRequestType**](PromoteDisksRequestType.md)|  | 

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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host doesn&#39;t support disk promotion APIs.  ***InvalidState***: if the virtual machine&#39;s power state changes during the execution of this method.  ***InvalidState***: if the virtual machine is not ready to respond to such requests.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_put_usb_scan_codes**
> int virtual_machine_put_usb_scan_codes(mo_id, put_usb_scan_codes_request_type)

Inject a sequence of USB HID scan codes into the keyboard. 

Inject a sequence of USB HID scan codes into the keyboard.  ***Since:*** vSphere API 6.5  ***Required privileges:*** VirtualMachine.Interact.PutUsbScanCodes 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.put_usb_scan_codes_request_type import PutUsbScanCodesRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    put_usb_scan_codes_request_type = vmware_vi.PutUsbScanCodesRequestType() # PutUsbScanCodesRequestType | 

    try:
        # Inject a sequence of USB HID scan codes into the keyboard. 
        api_response = api_instance.virtual_machine_put_usb_scan_codes(mo_id, put_usb_scan_codes_request_type)
        print("The response of VirtualMachineApi->virtual_machine_put_usb_scan_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_put_usb_scan_codes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **put_usb_scan_codes_request_type** | [**PutUsbScanCodesRequestType**](PutUsbScanCodesRequestType.md)|  | 

### Return type

**int**

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of keys injected.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_query_changed_disk_areas**
> DiskChangeInfo virtual_machine_query_changed_disk_areas(mo_id, query_changed_disk_areas_request_type)

Get a list of areas of a virtual disk belonging to this VM that have been modified since a well-defined point in the past. 

Get a list of areas of a virtual disk belonging to this VM that have been modified since a well-defined point in the past.  The beginning of the change interval is identified by \"changeId\", while the end of the change interval is implied by the snapshot ID passed in.  Note that the result of this function may contain \"false positives\" (i.e: flag areas of the disk as modified that are not). However, it is guaranteed that no changes will be missed.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Provisioning.DiskRandomRead 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.disk_change_info import DiskChangeInfo
from vmware_vi.models.query_changed_disk_areas_request_type import QueryChangedDiskAreasRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_changed_disk_areas_request_type = vmware_vi.QueryChangedDiskAreasRequestType() # QueryChangedDiskAreasRequestType | 

    try:
        # Get a list of areas of a virtual disk belonging to this VM that have been modified since a well-defined point in the past. 
        api_response = api_instance.virtual_machine_query_changed_disk_areas(mo_id, query_changed_disk_areas_request_type)
        print("The response of VirtualMachineApi->virtual_machine_query_changed_disk_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_query_changed_disk_areas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_changed_disk_areas_request_type** | [**QueryChangedDiskAreasRequestType**](QueryChangedDiskAreasRequestType.md)|  | 

### Return type

[**DiskChangeInfo**](DiskChangeInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a data structure specifying extents of the virtual disk that have changed since the thime the changeId string was obtained.  |  -  |
**500** | ***NotFound***: if the snapshot specified does not exist.  ***InvalidArgument***: if deviceKey does not specify a virtual disk, startOffset is beyond the end of the virtual disk or changeId is invalid or change tracking is not supported for this particular disk.  ***FileFault***: if the virtual disk files cannot be accessed/queried.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_query_connections**
> List[VirtualMachineConnection] virtual_machine_query_connections(mo_id)

Ask the virtual machine for a list of connections. 

Ask the virtual machine for a list of connections.  The virtual machine returns a list of connections. It is possible for the array returned to be empty - a virtual machine may have no connections.  ***Since:*** vSphere API 7.0.1.0  ***Required privileges:*** VirtualMachine.Interact.ConsoleInteract 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.virtual_machine_connection import VirtualMachineConnection
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Ask the virtual machine for a list of connections. 
        api_response = api_instance.virtual_machine_query_connections(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_query_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_query_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[VirtualMachineConnection]**](VirtualMachineConnection.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidPowerState***: If the virtual machine is not powered on.  ***Timedout***: If the the virtual machine did not respond to the request in a timely manner.  ***VmConfigFault***: If an error occurred.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_query_fault_tolerance_compatibility**
> List[MethodFault] virtual_machine_query_fault_tolerance_compatibility(mo_id)

This API can be invoked to determine whether a virtual machine is compatible for legacy Fault Tolerance. 

Deprecated as of vSphere API 6.0.  This API can be invoked to determine whether a virtual machine is compatible for legacy Fault Tolerance.  The API only checks for VM-specific factors that impact compatibility for RecordReplay based Fault Tolerance. Other requirements for Fault Tolerance such as host processor compatibility, logging nic configuration and licensing are not covered by this API. The query returns a list of faults, each fault corresponding to a specific incompatibility. If a given virtual machine is compatible for Fault Tolerance, then the fault list returned will be empty.  ***Since:*** vSphere API 4.1  ***Required privileges:*** VirtualMachine.Config.QueryFTCompatibility 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.method_fault import MethodFault
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # This API can be invoked to determine whether a virtual machine is compatible for legacy Fault Tolerance. 
        api_response = api_instance.virtual_machine_query_fault_tolerance_compatibility(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_query_fault_tolerance_compatibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_query_fault_tolerance_compatibility: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**List[MethodFault]**](MethodFault.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid.  ***NotSupported***: if the virtual machine is a template or this operation is not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_query_fault_tolerance_compatibility_ex**
> List[MethodFault] virtual_machine_query_fault_tolerance_compatibility_ex(mo_id, query_fault_tolerance_compatibility_ex_request_type)

This API can be invoked to determine whether a virtual machine is compatible for Fault Tolerance. 

This API can be invoked to determine whether a virtual machine is compatible for Fault Tolerance.  The API only checks for VM-specific factors that impact compatibility for Fault Tolerance. Other requirements for Fault Tolerance such as host processor compatibility, logging nic configuration and licensing are not covered by this API. The query returns a list of faults, each fault corresponding to a specific incompatibility. If a given virtual machine is compatible for Fault Tolerance, then the fault list returned will be empty.  ***Since:*** vSphere API 6.0  ***Required privileges:*** VirtualMachine.Config.QueryFTCompatibility 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.method_fault import MethodFault
from vmware_vi.models.query_fault_tolerance_compatibility_ex_request_type import QueryFaultToleranceCompatibilityExRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    query_fault_tolerance_compatibility_ex_request_type = vmware_vi.QueryFaultToleranceCompatibilityExRequestType() # QueryFaultToleranceCompatibilityExRequestType | 

    try:
        # This API can be invoked to determine whether a virtual machine is compatible for Fault Tolerance. 
        api_response = api_instance.virtual_machine_query_fault_tolerance_compatibility_ex(mo_id, query_fault_tolerance_compatibility_ex_request_type)
        print("The response of VirtualMachineApi->virtual_machine_query_fault_tolerance_compatibility_ex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_query_fault_tolerance_compatibility_ex: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **query_fault_tolerance_compatibility_ex_request_type** | [**QueryFaultToleranceCompatibilityExRequestType**](QueryFaultToleranceCompatibilityExRequestType.md)|  | 

### Return type

[**List[MethodFault]**](MethodFault.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |
**500** | ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state.  ***VmConfigFault***: if the virtual machine&#39;s configuration is invalid.  ***NotSupported***: if the virtual machine is a template or this operation is not supported.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_query_unowned_files**
> List[str] virtual_machine_query_unowned_files(mo_id)

For all files that belong to the vm, check that the file owner is set to the current datastore principal user, as set by *HostDatastoreSystem.ConfigureDatastorePrincipal* 

For all files that belong to the vm, check that the file owner is set to the current datastore principal user, as set by *HostDatastoreSystem.ConfigureDatastorePrincipal*  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Config.QueryUnownedFiles 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # For all files that belong to the vm, check that the file owner is set to the current datastore principal user, as set by *HostDatastoreSystem.ConfigureDatastorePrincipal* 
        api_response = api_instance.virtual_machine_query_unowned_files(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_query_unowned_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_query_unowned_files: %s\n" % e)
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
**200** | The list of file paths for vm files whose ownership is not correct. Use *FileManager.ChangeOwner* to set the file ownership.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_reboot_guest**
> virtual_machine_reboot_guest(mo_id)

Issues a command to the guest operating system asking it to perform a reboot. 

Issues a command to the guest operating system asking it to perform a reboot.  Returns immediately and does not wait for the guest operating system to complete the operation.  ***Required privileges:*** VirtualMachine.Interact.Reset 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Issues a command to the guest operating system asking it to perform a reboot. 
        api_instance.virtual_machine_reboot_guest(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reboot_guest: %s\n" % e)
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
**500** | ***InvalidPowerState***: if the power state is not powered on.  ***ToolsUnavailable***: if VMware Tools is not running.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_reconfig_vm_task**
> ManagedObjectReference virtual_machine_reconfig_vm_task(mo_id, reconfig_vm_request_type)

Reconfigures this virtual machine. 

Reconfigures this virtual machine.  All the changes in the given configuration are applied to the virtual machine as an atomic operation.  Reconfiguring the virtual machine may require any of the following privileges depending on what is being changed: - VirtualMachine.Interact.DeviceConnection if changing the runtime connection   state of a device as embodied by the Connectable property. - VirtualMachine.Interact.SetCDMedia if changing the backing of a CD-ROM   device - VirtualMachine.Interact.SetFloppyMedia if changing the backing of a   floppy device - VirtualMachine.Config.Rename if renaming the virtual machine - VirtualMachine.Config.Annotation if setting annotation a value - VirtualMachine.Config.AddExistingDisk if adding a virtual disk device   that is backed by an existing virtual disk file - VirtualMachine.Config.AddNewDisk if adding a virtual disk device for which   the backing virtual disk file is to be created - VirtualMachine.Config.RemoveDisk if removing a virtual disk device that   refers to a virtual disk file - VirtualMachine.Config.CPUCount if changing the number of CPUs - VirtualMachine.Config.Memory if changing the amount of memory - VirtualMachine.Config.RawDevice if adding, removing or editing a raw   device mapping (RDM) or SCSI passthrough device - VirtualMachine.Config.AddRemoveDevice if adding or removing any   device other than disk, raw, or USB device - VirtualMachine.Config.EditDevice if changing the settings of any   device - VirtualMachine.Config.Settings if changing any basic settings such as   those in ToolsConfigInfo, FlagInfo, or DefaultPowerOpInfo - VirtualMachine.Config.Resource if changing resource allocations,   affinities, or setting network traffic shaping or virtual disk shares - VirtualMachine.Config.AdvancedConfig if changing values in   extraConfig - VirtualMachine.Config.SwapPlacement if changing swapPlacement - VirtualMachine.Config.HostUSBDevice if adding, removing or editing a   VirtualUSB device backed by the host USB device. - VirtualMachine.Config.DiskExtend if extending an existing VirtualDisk   device. - VirtualMachine.Config.ChangeTracking if enabling/disabling changed   block tracking for the virtual machine's disks. - VirtualMachine.Config.MksControl if toggling display connection   limits or the guest auto-lock feature. - DVSwitch.CanUse if connecting a VirtualEthernetAdapter to a port   in a DistributedVirtualSwitch. - DVPortgroup.CanUse if connecting a VirtualEthernetAdapter to a   DistributedVirtualPortgroup. - Cryptographer.Encrypt if vm home folder is encrypted or existing   disk is encryted. - Cryptographer.Decrypt if vm home folder is decrypted or existing   disk is decryted. - Cryptographer.Recrypt if vm home folder is recrypted or existing   disk is recryted. - Cryptographer.AddDisk if encrypted disk is attached to the vm. - Cryptographer.RegisterHost on the host if the virtual machine is   encrypted, but encryption is not enabled on the host.    Creating a virtual machine may require the following privileges: - VirtualMachine.Config.RawDevice if adding a raw device - VirtualMachine.Config.AddExistingDisk if adding a VirtualDisk and   the fileOperation is unset - VirtualMachine.Config.AddNewDisk if adding a VirtualDisk and   the fileOperation is set - VirtualMachine.Config.HostUSBDevice if adding a VirtualUSB device   backed by the host USB device.    In addition, this operation may require the following privileges: - Datastore.AllocateSpace on any datastore where virtual disks will   be created or extended. - Network.Assign on any network the virtual machine will be   connected to.    To create a VirtualDisk on a persistent memory storage, the storage must be specified via *profile* while the datastore property of corresponding VirtualDisk backing must be unset.  To create a VirtualNVDIMM device, the storage *profile* must be set to the default persistent memory storage profile while the datastore property of *the device backing* must be unset. 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reconfig_vm_request_type import ReconfigVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reconfig_vm_request_type = vmware_vi.ReconfigVMRequestType() # ReconfigVMRequestType | 

    try:
        # Reconfigures this virtual machine. 
        api_response = api_instance.virtual_machine_reconfig_vm_task(mo_id, reconfig_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_reconfig_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reconfig_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reconfig_vm_request_type** | [**ReconfigVMRequestType**](ReconfigVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is poweredOn and the virtual hardware cannot support the configuration changes.  ***TaskInProgress***: if the virtual machine is busy.  ***TooManyDevices***: if the device specifications exceed the allowed limits.  ***ConcurrentAccess***: if the changeVersion does not match the server&#39;s changeVersion for the configuration.  ***FileFault***: if there is a problem creating or accessing the virtual machine&#39;s files for this operation. Typically a more specific fault like NoDiskSpace or FileAlreadyExists is thrown.  ***InvalidName***: if the specified name is invalid.  ***DuplicateName***: if the specified name already exists in the parent folder.  ***InvalidState***: if the operation cannot be performed in the current state of the virtual machine. For example, because the virtual machine&#39;s configuration is not available.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***VmConfigFault***: if the spec is invalid. Typically, a more specific subclass is thrown.  ***CpuHotPlugNotSupported***: if the current configuration of the VM does not support hot-plugging of CPUs.  ***MemoryHotPlugNotSupported***: if the current configuration of the VM does not support hot-plugging of memory.  ***VmWwnConflict***: if the WWN of the virtual machine has been used by other virtual machines.  ***NoPermission***: if crypto operation is requested on the vm home folder, but the user does not have the corresponding crypto privilege on the virtual machine: Encrypt - Cryptographer.Encrypt Decrypt - Cryptographer.Decrypt Recrypt - Cryptographer.Recrypt  ***NoPermission***: if crypto operation is requested on the vms disks, but the user does not have the corresponding crypto privilege on the virtual machine: Encrypt - Cryptographer.Encrypt Decrypt - Cryptographer.Decrypt Recrypt - Cryptographer.Recrypt AddDisk - Cryptographer.AddDisk  ***NoPermission***: if the virtual machine is encrypted and the encryption is not enabled on the host, but the user does not have Cryptographer.RegisterHost privilege on the host.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_refresh_storage_info**
> virtual_machine_refresh_storage_info(mo_id)

Explicitly refreshes the storage information of this virtual machine, updating properties *VirtualMachine.storage*, *VirtualMachine.layoutEx* and *VirtualMachineSummary.storage*. 

Explicitly refreshes the storage information of this virtual machine, updating properties *VirtualMachine.storage*, *VirtualMachine.layoutEx* and *VirtualMachineSummary.storage*.  This is an asynchronous operation which will return immediately; changes may not be reflected in vCenter for some time.  ***Since:*** vSphere API 4.0  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Explicitly refreshes the storage information of this virtual machine, updating properties *VirtualMachine.storage*, *VirtualMachine.layoutEx* and *VirtualMachineSummary.storage*. 
        api_instance.virtual_machine_refresh_storage_info(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_refresh_storage_info: %s\n" % e)
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

# **virtual_machine_reload**
> virtual_machine_reload(mo_id)

Reload the entity state. 

Reload the entity state.  Clients only need to call this method if they changed some external state that affects the service without using the Web service interface to perform the change. For example, hand-editing a virtual machine configuration file affects the configuration of the associated virtual machine but the service managing the virtual machine might not monitor the file for changes. In this case, after such an edit, a client would call \"reload\" on the associated virtual machine to ensure the service and its clients have current data for the virtual machine.  ***Required privileges:*** System.Read 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Reload the entity state. 
        api_instance.virtual_machine_reload(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reload: %s\n" % e)
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

# **virtual_machine_reload_virtual_machine_from_path_task**
> ManagedObjectReference virtual_machine_reload_virtual_machine_from_path_task(mo_id, reload_virtual_machine_from_path_request_type)

Reloads the configuration for this virtual machine from a given datastore path. 

Reloads the configuration for this virtual machine from a given datastore path.  This is equivalent to unregistering and registering the virtual machine from a different path. The virtual machine's hardware configuration, snapshots, guestinfo variables etc. will be replaced based on the new configuration file. Other information associated with the virtual machine object, such as events and permissions, will be preserved.  This method is only supported on vCenter Server. It can be invoked on inaccessible or orphaned virtual machines, but it cannot be invoked on powered on, connected virtual machines. Both the source virtual machine object and the destination path should be of the same type i.e. virtual machine or template. Reloading a virtual machine with a template or vice-versa is not supported.  _Note:_ Since the API replaces the source configuration with that of the destination, if the destination configuration does not refer to a valid virtual machine, it will create an invalid virtual machine object. This API should not be invoked on fault tolerant virtual machines since doing so will leave the original virtual machine's configuration in an invalid state. It is recommended that you turn off fault tolerance before invoking this API.  ***Since:*** vSphere API 4.1  ***Required privileges:*** VirtualMachine.Config.ReloadFromPath 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.reload_virtual_machine_from_path_request_type import ReloadVirtualMachineFromPathRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    reload_virtual_machine_from_path_request_type = vmware_vi.ReloadVirtualMachineFromPathRequestType() # ReloadVirtualMachineFromPathRequestType | 

    try:
        # Reloads the configuration for this virtual machine from a given datastore path. 
        api_response = api_instance.virtual_machine_reload_virtual_machine_from_path_task(mo_id, reload_virtual_machine_from_path_request_type)
        print("The response of VirtualMachineApi->virtual_machine_reload_virtual_machine_from_path_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reload_virtual_machine_from_path_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **reload_virtual_machine_from_path_request_type** | [**ReloadVirtualMachineFromPathRequestType**](ReloadVirtualMachineFromPathRequestType.md)|  | 

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
**500** | ***NotSupported***: if invoked on ESX server or if invoked on a virtual machine with the destination path for a template and vice-versa.  ***InvalidPowerState***: if the virtual machine is powered on.  ***TaskInProgress***: if the virtual machine is busy.  ***FileFault***: if there is a problem creating or accessing the files needed for this operation.  ***InvalidState***: if the virtual machine is busy or not ready to respond to such requests.  ***VmConfigFault***: if the format / configuration of the virtual machine is invalid. Typically, a more specific fault is thrown such as InvalidFormat if the configuration file cannot be read, or InvalidDiskFormat if the disks cannot be read.  ***AlreadyExists***: if the virtual machine is already registered.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_relocate_vm_task**
> ManagedObjectReference virtual_machine_relocate_vm_task(mo_id, relocate_vm_request_type)

Relocates a virtual machine to the location specified by *VirtualMachineRelocateSpec*. 

Relocates a virtual machine to the location specified by *VirtualMachineRelocateSpec*.  Starting from VCenter 5.1, this API also supports relocating a template to a new host should the current host become inactive. Starting from vCenter 6.0 this API also supports relocating a VM to a new vCenter service.  Requires the following additional permissions: - Resource.HotMigrate if the virtual machine is powered on. - Datastore.AllocateSpec if the virtual machine or its disks are   being relocated to a new datastore. - Resource.AssignVMToPool if the resource pool is changing. - VirtualMachine.Inventory.Register against the destination folder if   the virtual machine is moving to a new vCenter service. - VirtualMachine.Inventory.Move against the virtual machine, source   folder, and destination folder if the virtual machine is changing   folders within the same vCenter service. - Network.Assign against the new network if the virtual machine is   changing networks.    If this virtual machine is configured with a VirtualNVDIMM device, and if the virtual machine will be moved to a different host, the VirtualNVDIMM will be automatically relocated to the destination host's Non-Volatile Memory storage. If this Virtual machine is configured with virtual disks via persistent memory storage profile: - If spec specifies only compute location change, these virtual disks   will be automatically moved to a persistent memory storage in   destination host that supports the profile. - If spec specifies primary datastore change via   *datastore*, unlike regular   virtual disks, these disks will not be automatically moved to the   specified datastore, instead they will stay on a persistent   memory storage in destination host that supports the profile. - To explicityly move these disks to a location other than   persistent memory storage, use disk locator to specify the   new destination datastore along with a storage profile that removes   the persistent memory storage requirement. Note that this   downgrades the disk I/O performance. - On the other hand, to move a virtual disk from a regular storage to   persistent memory, use   *deviceChange*   to specify a storage profile of persistent memory storage. Note   that this upgrades the disk I/O performance.    ***Required privileges:*** Resource.ColdMigrate 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.relocate_vm_request_type import RelocateVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    relocate_vm_request_type = vmware_vi.RelocateVMRequestType() # RelocateVMRequestType | 

    try:
        # Relocates a virtual machine to the location specified by *VirtualMachineRelocateSpec*. 
        api_response = api_instance.virtual_machine_relocate_vm_task(mo_id, relocate_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_relocate_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_relocate_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **relocate_vm_request_type** | [**RelocateVMRequestType**](RelocateVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidArgument***: in the following cases: - the target host and target pool are not associated with the   same compute resource - the target pool represents a cluster without DRS enabled,   and the host is not specified - the virtual machine is powered on, its home or any of its disks   will change storage location, and the host is not specified - Datastore is not accessible in a cross-datacenter move - Datastore in a diskLocator entry is not specified - the specified device ID cannot be found in the virtual machine&#39;s current   configuration    ***NotSupported***: if the virtual machine is marked as template and the datastore is changing or if it is a cross vCenter vMotion operation.  ***Timedout***: if one of the phases of the relocate process times out.  ***InvalidState***: if the operation cannot be performed because of the host or virtual machine&#39;s current state. For example, if the host is in maintenance mode, or if the virtual machine&#39;s configuration information is not available.  ***InvalidDatastore***: if the operation cannot be performed on the target datastores.  ***FileFault***: if there is an error accessing the virtual machine files.  ***VmConfigFault***: if the virtual machine is not compatible with the destination host. Typically, a specific subclass of this exception is thrown, such as IDEDiskNotSupported.  ***MigrationFault***: if it is not possible to migrate the virtual machine to the destination host. This is typically due to hosts being incompatible, such as mismatch in network polices or access to networks and datastores. Typically, a more specific subclass is thrown.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***DisallowedOperationOnFailoverHost***: if the virtual machine is powered on and is being migrated to a failover host. See *ClusterFailoverHostAdmissionControlPolicy*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_remove_all_snapshots_task**
> ManagedObjectReference virtual_machine_remove_all_snapshots_task(mo_id, remove_all_snapshots_request_type)

Remove all the snapshots associated with this virtual machine. 

Remove all the snapshots associated with this virtual machine.  If the virtual machine does not have any snapshots, then this operation simply returns successfully.  ***Required privileges:*** VirtualMachine.State.RemoveSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.remove_all_snapshots_request_type import RemoveAllSnapshotsRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    remove_all_snapshots_request_type = vmware_vi.RemoveAllSnapshotsRequestType() # RemoveAllSnapshotsRequestType | 

    try:
        # Remove all the snapshots associated with this virtual machine. 
        api_response = api_instance.virtual_machine_remove_all_snapshots_task(mo_id, remove_all_snapshots_request_type)
        print("The response of VirtualMachineApi->virtual_machine_remove_all_snapshots_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_remove_all_snapshots_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **remove_all_snapshots_request_type** | [**RemoveAllSnapshotsRequestType**](RemoveAllSnapshotsRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support snapshots.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_rename_task**
> ManagedObjectReference virtual_machine_rename_task(mo_id, rename_request_type)

Renames this managed entity. 

Renames this managed entity.  Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.  See also *ManagedEntity.name*.  ***Required privileges:*** VirtualMachine.Config.Rename 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.rename_request_type import RenameRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    rename_request_type = vmware_vi.RenameRequestType() # RenameRequestType | 

    try:
        # Renames this managed entity. 
        api_response = api_instance.virtual_machine_rename_task(mo_id, rename_request_type)
        print("The response of VirtualMachineApi->virtual_machine_rename_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_rename_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **rename_request_type** | [**RenameRequestType**](RenameRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***DuplicateName***: If another object in the same folder has the target name.  ***InvalidName***: If the new name is not a valid entity name.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_reset_guest_information**
> virtual_machine_reset_guest_information(mo_id)

Clears cached guest information. 

Clears cached guest information.  Guest information can be cleared only if the virtual machine is powered off.  This method can be useful if stale information is cached, preventing an IP address or MAC address from being reused.  ***Required privileges:*** VirtualMachine.Config.ResetGuestInfo 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Clears cached guest information. 
        api_instance.virtual_machine_reset_guest_information(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reset_guest_information: %s\n" % e)
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
**500** | ***InvalidState***: if the virtual machine is not powered off.  ***NotSupported***: if the virtual machine is marked as a template.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_reset_vm_task**
> ManagedObjectReference virtual_machine_reset_vm_task(mo_id)

Resets power on this virtual machine. 

Resets power on this virtual machine.  If the current state is poweredOn, then this method first performs powerOff(hard). Once the power state is poweredOff, then this method performs powerOn(option).  Although this method functions as a powerOff followed by a powerOn, the two operations are atomic with respect to other clients, meaning that other power operations cannot be performed until the reset method completes.  ***Required privileges:*** VirtualMachine.Interact.Reset 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Resets power on this virtual machine. 
        api_response = api_instance.virtual_machine_reset_vm_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_reset_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_reset_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is suspended or poweredOff.  ***TaskInProgress***: if the virtual machine is busy.  ***NotEnoughLicenses***: if there are not enough licenses to reset this virtual machine.  ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidState***: if the host is in maintenance mode.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_revert_to_current_snapshot_task**
> ManagedObjectReference virtual_machine_revert_to_current_snapshot_task(mo_id, revert_to_current_snapshot_request_type)

Reverts the virtual machine to the current snapshot. 

Reverts the virtual machine to the current snapshot.  This is equivalent to doing snapshot.currentSnapshot.revert.  If no snapshot exists, then the operation does nothing, and the virtual machine state remains unchanged.  ***Required privileges:*** VirtualMachine.State.RevertToSnapshot 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.revert_to_current_snapshot_request_type import RevertToCurrentSnapshotRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    revert_to_current_snapshot_request_type = vmware_vi.RevertToCurrentSnapshotRequestType() # RevertToCurrentSnapshotRequestType | 

    try:
        # Reverts the virtual machine to the current snapshot. 
        api_response = api_instance.virtual_machine_revert_to_current_snapshot_task(mo_id, revert_to_current_snapshot_request_type)
        print("The response of VirtualMachineApi->virtual_machine_revert_to_current_snapshot_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_revert_to_current_snapshot_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **revert_to_current_snapshot_request_type** | [**RevertToCurrentSnapshotRequestType**](RevertToCurrentSnapshotRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support snapshots.  ***InsufficientResourcesFault***: if this operation would violate a resource usage policy.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available or if an OVF consumer is blocking the operation.  ***VmConfigFault***: if a configuration issue prevents the power-on. Typically, a more specific fault, such as UnsupportedVmxLocation, is thrown.  ***FileFault***: if there is a problem accessing the virtual machine on the filesystem.  ***NotFound***: if the virtual machine does not have a current snapshot.  ***DisallowedOperationOnFailoverHost***: if the virtual machine is being reverted to a powered on state and the host specified is a failover host. See *ClusterFailoverHostAdmissionControlPolicy*.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_send_nmi**
> virtual_machine_send_nmi(mo_id)

Send a non-maskable interrupt (NMI). 

Send a non-maskable interrupt (NMI).  Currently, there is no way to verify if the NMI was actually received by the guest OS.  ***Since:*** vSphere API 6.0  ***Required privileges:*** VirtualMachine.Interact.GuestControl 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Send a non-maskable interrupt (NMI). 
        api_instance.virtual_machine_send_nmi(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_send_nmi: %s\n" % e)
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
**500** | ***InvalidState***: if the virtual machine is not powered on.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_set_custom_value**
> virtual_machine_set_custom_value(mo_id, set_custom_value_request_type)

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_custom_value_request_type = vmware_vi.SetCustomValueRequestType() # SetCustomValueRequestType | 

    try:
        # Assigns a value to a custom field. 
        api_instance.virtual_machine_set_custom_value(mo_id, set_custom_value_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_set_custom_value: %s\n" % e)
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

# **virtual_machine_set_display_topology**
> virtual_machine_set_display_topology(mo_id, set_display_topology_request_type)

Sets the console window's display topology as specified. 

Sets the console window's display topology as specified.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.ConsoleInteract 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_display_topology_request_type import SetDisplayTopologyRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_display_topology_request_type = vmware_vi.SetDisplayTopologyRequestType() # SetDisplayTopologyRequestType | 

    try:
        # Sets the console window's display topology as specified. 
        api_instance.virtual_machine_set_display_topology(mo_id, set_display_topology_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_set_display_topology: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_display_topology_request_type** | [**SetDisplayTopologyRequestType**](SetDisplayTopologyRequestType.md)|  | 

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
**500** | ***NotSupported***: if the Guest Operating system does not support setting the display topology  ***InvalidPowerState***: if the power state is not poweredOn.  ***InvalidState***: if the virtual machine is not connected.  ***ToolsUnavailable***: if VMware Tools is not running.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_set_screen_resolution**
> virtual_machine_set_screen_resolution(mo_id, set_screen_resolution_request_type)

Sets the console window's resolution as specified. 

Sets the console window's resolution as specified.  ***Required privileges:*** VirtualMachine.Interact.ConsoleInteract 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.set_screen_resolution_request_type import SetScreenResolutionRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    set_screen_resolution_request_type = vmware_vi.SetScreenResolutionRequestType() # SetScreenResolutionRequestType | 

    try:
        # Sets the console window's resolution as specified. 
        api_instance.virtual_machine_set_screen_resolution(mo_id, set_screen_resolution_request_type)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_set_screen_resolution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **set_screen_resolution_request_type** | [**SetScreenResolutionRequestType**](SetScreenResolutionRequestType.md)|  | 

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
**500** | ***NotSupported***: if the Guest Operating system does not support setting the screen resolution.  ***InvalidPowerState***: if the power state is not poweredOn.  ***InvalidState***: if the virtual machine is not connected.  ***ToolsUnavailable***: if VMware Tools is not running.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_shutdown_guest**
> virtual_machine_shutdown_guest(mo_id)

Issues a command to the guest operating system asking it to perform a clean shutdown of all services. 

Issues a command to the guest operating system asking it to perform a clean shutdown of all services.  Returns immediately and does not wait for the guest operating system to complete the operation.  ***Required privileges:*** VirtualMachine.Interact.PowerOff 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Issues a command to the guest operating system asking it to perform a clean shutdown of all services. 
        api_instance.virtual_machine_shutdown_guest(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_shutdown_guest: %s\n" % e)
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
**500** | ***InvalidPowerState***: if the power state is not powered on.  ***ToolsUnavailable***: if VMware Tools is not running.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_standby_guest**
> virtual_machine_standby_guest(mo_id)

Issues a command to the guest operating system asking it to prepare for a suspend operation. 

Issues a command to the guest operating system asking it to prepare for a suspend operation.  Returns immediately and does not wait for the guest operating system to complete the operation.  ***Required privileges:*** VirtualMachine.Interact.Suspend 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Issues a command to the guest operating system asking it to prepare for a suspend operation. 
        api_instance.virtual_machine_standby_guest(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_standby_guest: %s\n" % e)
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
**500** | ***InvalidPowerState***: if the power state is not powered on.  ***ToolsUnavailable***: if VMware Tools is not running.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_start_recording_task**
> ManagedObjectReference virtual_machine_start_recording_task(mo_id, start_recording_request_type)

Initiates a recording session on this virtual machine. 

Deprecated as of vsphere API 5.1.  Initiates a recording session on this virtual machine.  As a side effect, this operation creates a snapshot on the virtual machine, which in turn becomes the current snapshot.  This is an experimental interface that is not intended for use in production code.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.Record 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.start_recording_request_type import StartRecordingRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    start_recording_request_type = vmware_vi.StartRecordingRequestType() # StartRecordingRequestType | 

    try:
        # Initiates a recording session on this virtual machine. 
        api_response = api_instance.virtual_machine_start_recording_task(mo_id, start_recording_request_type)
        print("The response of VirtualMachineApi->virtual_machine_start_recording_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_start_recording_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **start_recording_request_type** | [**StartRecordingRequestType**](StartRecordingRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation. The *info.result* property in the *Task* contains the newly created *VirtualMachineSnapshot* associated with the recording on success.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support record functionality or if the virtual machine does not support this  ***VmConfigIncompatibleForRecordReplay***: if the virtual machine configuration is incompatible for recording.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like MultipleSnapshotsNotSupported is thrown.  ***InvalidName***: if the specified snapshot name is invalid.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine configuration information is not available.  ***RecordReplayDisabled***: if the record/replay config flag has not been enabled for this virtual machine.  ***HostIncompatibleForRecordReplay***: if the virtual machine is located on a host that does not support record/replay.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_start_replaying_task**
> ManagedObjectReference virtual_machine_start_replaying_task(mo_id, start_replaying_request_type)

Starts a replay session on this virtual machine. 

Deprecated as of vsphere API 5.1.  Starts a replay session on this virtual machine.  As a side effect, this operation updates the current snapshot of the virtual machine.  This is an experimental interface that is not intended for use in production code.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.Replay 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.start_replaying_request_type import StartReplayingRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    start_replaying_request_type = vmware_vi.StartReplayingRequestType() # StartReplayingRequestType | 

    try:
        # Starts a replay session on this virtual machine. 
        api_response = api_instance.virtual_machine_start_replaying_task(mo_id, start_replaying_request_type)
        print("The response of VirtualMachineApi->virtual_machine_start_replaying_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_start_replaying_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **start_replaying_request_type** | [**StartReplayingRequestType**](StartReplayingRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support record/replay functionality or if the virtual machine does not support this capability.  ***InvalidArgument***: if replaySnapshot is not a valid snapshot associated with a recorded session on this virtual machine.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***VmConfigIncompatibleForRecordReplay***: if the virtual machine configuration is incompatible for replaying.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine configuration information is not available.  ***NotFound***: if replaySnapshot is no longer present.  ***RecordReplayDisabled***: if the record/replay config flag has not been enabled for this virtual machine.  ***HostIncompatibleForRecordReplay***: if the virtual machine is located on a host that does not support record/replay.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_stop_recording_task**
> ManagedObjectReference virtual_machine_stop_recording_task(mo_id)

Stops a currently active recording session on this virtual machine. 

Deprecated as of vsphere API 5.1.  Stops a currently active recording session on this virtual machine.  This is an experimental interface that is not intended for use in production code.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.Record 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Stops a currently active recording session on this virtual machine. 
        api_response = api_instance.virtual_machine_stop_recording_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_stop_recording_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_stop_recording_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support record/replay functionality or if the virtual machine does not support this capability.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine does not have an active recording session.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_stop_replaying_task**
> ManagedObjectReference virtual_machine_stop_replaying_task(mo_id)

Stops a replay session on this virtual machine. 

Deprecated as of vsphere API 5.1.  Stops a replay session on this virtual machine.  This is an experimental interface that is not intended for use in production code.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.Replay 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Stops a replay session on this virtual machine. 
        api_response = api_instance.virtual_machine_stop_replaying_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_stop_replaying_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_stop_replaying_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the host product does not support record/replay functionality or if the virtual machine does not support this capability.  ***SnapshotFault***: if an error occurs during the snapshot operation. Typically, a more specific fault like InvalidSnapshotFormat is thrown.  ***FileFault***: if there is a problem with creating or accessing one or more files needed for this operation.  ***InvalidPowerState***: if the operation cannot be performed in the current power state of the virtual machine.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, the virtual machine does not have an active recording session.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_suspend_vm_task**
> ManagedObjectReference virtual_machine_suspend_vm_task(mo_id)

Suspends execution in this virtual machine. 

Suspends execution in this virtual machine.  ***Required privileges:*** VirtualMachine.Interact.Suspend 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Suspends execution in this virtual machine. 
        api_response = api_instance.virtual_machine_suspend_vm_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_suspend_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_suspend_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is not poweredOn.  ***TaskInProgress***: if the virtual machine is busy.  ***NotSupported***: if the virtual machine is marked as a template.  ***InvalidState***: if the operation cannot be performed because of the virtual machine&#39;s current state. For example, if the virtual machine configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_terminate_fault_tolerant_vm_task**
> ManagedObjectReference virtual_machine_terminate_fault_tolerant_vm_task(mo_id, terminate_fault_tolerant_vm_request_type)

Terminates the specified secondary virtual machine in a fault tolerant group. 

Terminates the specified secondary virtual machine in a fault tolerant group.  This can be used to test fault tolerance on a given virtual machine, and should be used with care.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.TerminateFaultTolerantVM 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.terminate_fault_tolerant_vm_request_type import TerminateFaultTolerantVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    terminate_fault_tolerant_vm_request_type = vmware_vi.TerminateFaultTolerantVMRequestType() # TerminateFaultTolerantVMRequestType | 

    try:
        # Terminates the specified secondary virtual machine in a fault tolerant group. 
        api_response = api_instance.virtual_machine_terminate_fault_tolerant_vm_task(mo_id, terminate_fault_tolerant_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_terminate_fault_tolerant_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_terminate_fault_tolerant_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **terminate_fault_tolerant_vm_request_type** | [**TerminateFaultTolerantVMRequestType**](TerminateFaultTolerantVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_terminate_vm**
> virtual_machine_terminate_vm(mo_id)

Do an immediate power off of a VM. 

Do an immediate power off of a VM.  This API issues a SIGKILL to the vmx process of the VM. Pending synchronous I/Os may not be written out before the vmx process dies depending on accessibility of the datastore.  ***Since:*** vSphere API 5.0  ***Required privileges:*** VirtualMachine.Interact.PowerOff 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Do an immediate power off of a VM. 
        api_instance.virtual_machine_terminate_vm(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_terminate_vm: %s\n" % e)
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
**500** | ***NotSupported***: if this operation is not supported.  ***InvalidState***: if the VM is not powered on or another issue prevents the operation from being performed.  ***TaskInProgress***: if the virtual machine is busy.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_turn_off_fault_tolerance_for_vm_task**
> ManagedObjectReference virtual_machine_turn_off_fault_tolerance_for_vm_task(mo_id)

Removes all secondary virtual machines associated with the fault tolerant group and turns off protection for this virtual machine. 

Removes all secondary virtual machines associated with the fault tolerant group and turns off protection for this virtual machine.  This operation can only be invoked from the primary virtual machine in the group.  ***Since:*** vSphere API 4.0  ***Required privileges:*** VirtualMachine.Interact.TurnOffFaultTolerance 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes all secondary virtual machines associated with the fault tolerant group and turns off protection for this virtual machine. 
        api_response = api_instance.virtual_machine_turn_off_fault_tolerance_for_vm_task(mo_id)
        print("The response of VirtualMachineApi->virtual_machine_turn_off_fault_tolerance_for_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_turn_off_fault_tolerance_for_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**ManagedObjectReference**](ManagedObjectReference.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***VmFaultToleranceIssue***: if any error is encountered with the fault tolerance configuration of the virtual machine. Typically, a more specific fault like InvalidOperationOnSecondaryVm is thrown.  ***TaskInProgress***: if the virtual machine is busy.  ***InvalidState***: if the host is in maintenance mode or if the virtual machine&#39;s configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_unmount_tools_installer**
> virtual_machine_unmount_tools_installer(mo_id)

Unmounts VMware Tools installer CD. 

Unmounts VMware Tools installer CD.  ***Required privileges:*** VirtualMachine.Interact.ToolsInstall 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Unmounts VMware Tools installer CD. 
        api_instance.virtual_machine_unmount_tools_installer(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_unmount_tools_installer: %s\n" % e)
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
**500** | ***InvalidState***: if the virtual machine is not running, VMware Tools is not running or the VMware Tools CD is already mounted.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_unregister_vm**
> virtual_machine_unregister_vm(mo_id)

Removes this virtual machine from the inventory without removing any of the virtual machine's files on disk. 

Removes this virtual machine from the inventory without removing any of the virtual machine's files on disk.  All high-level information stored with the management server (ESX Server or VirtualCenter) is removed, including information such as statistics, resource pool association, permissions, and alarms.  Use the Folder.RegisterVM method to recreate a VirtualMachine object from the set of virtual machine files by passing in the path to the configuration file. However, the VirtualMachine managed object that results typically has different objects ID and may inherit a different set of permissions.  ***Required privileges:*** VirtualMachine.Inventory.Unregister 

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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Removes this virtual machine from the inventory without removing any of the virtual machine's files on disk. 
        api_instance.virtual_machine_unregister_vm(mo_id)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_unregister_vm: %s\n" % e)
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
**500** | ***TaskInProgress***: if the virtual machine is busy.  ***InvalidPowerState***: if the virtual machine is powered on.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_upgrade_tools_task**
> ManagedObjectReference virtual_machine_upgrade_tools_task(mo_id, upgrade_tools_request_type)

Begins the tools upgrade process. 

Begins the tools upgrade process.  To monitor the status of the tools install, clients should check the tools status, *GuestInfo.toolsVersionStatus* and *GuestInfo.toolsRunningStatus*.  ***Required privileges:*** VirtualMachine.Interact.ToolsInstall 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.upgrade_tools_request_type import UpgradeToolsRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upgrade_tools_request_type = vmware_vi.UpgradeToolsRequestType() # UpgradeToolsRequestType | 

    try:
        # Begins the tools upgrade process. 
        api_response = api_instance.virtual_machine_upgrade_tools_task(mo_id, upgrade_tools_request_type)
        print("The response of VirtualMachineApi->virtual_machine_upgrade_tools_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_upgrade_tools_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upgrade_tools_request_type** | [**UpgradeToolsRequestType**](UpgradeToolsRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidState***: if the virtual machine is not running or is suspended.  ***NotSupported***: if upgrading tools is not supported.  ***TaskInProgress***: if an upgrade is already taking place.  ***VmToolsUpgradeFault***: if the upgrade failed.  ***ToolsUnavailable***: if VMware Tools is not running.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_upgrade_vm_task**
> ManagedObjectReference virtual_machine_upgrade_vm_task(mo_id, upgrade_vm_request_type)

Upgrades this virtual machine's virtual hardware to the latest revision that is supported by the virtual machine's current host. 

Upgrades this virtual machine's virtual hardware to the latest revision that is supported by the virtual machine's current host.  ***Required privileges:*** VirtualMachine.Config.UpgradeVirtualHardware 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.upgrade_vm_request_type import UpgradeVMRequestType
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
    api_instance = vmware_vi.VirtualMachineApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    upgrade_vm_request_type = vmware_vi.UpgradeVMRequestType() # UpgradeVMRequestType | 

    try:
        # Upgrades this virtual machine's virtual hardware to the latest revision that is supported by the virtual machine's current host. 
        api_response = api_instance.virtual_machine_upgrade_vm_task(mo_id, upgrade_vm_request_type)
        print("The response of VirtualMachineApi->virtual_machine_upgrade_vm_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualMachineApi->virtual_machine_upgrade_vm_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **upgrade_vm_request_type** | [**UpgradeVMRequestType**](UpgradeVMRequestType.md)|  | 

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
**200** | This method returns a *Task* object with which to monitor the operation.  Refers instance of *Task*.  |  -  |
**500** | ***InvalidPowerState***: if the power state is not poweredOff.  ***TaskInProgress***: if the virtual machine is busy.  ***AlreadyUpgraded***: if the virtual machine&#39;s hardware is already up-to-date.  ***NoDiskFound***: if no virtual disks are attached to this virtual machine.  ***InvalidState***: if the host is in maintenance mode, if an invalid version string is specified, or if the virtual machine is in a state in which the operation cannot be performed. For example, if the configuration information is not available.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

