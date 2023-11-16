# GuestInfo

Information about the guest operating system.  Most of this information is collected by VMware Tools. In general, be sure you have VMware Tools installed and that the virtual machine is running when you access this information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools_status** | [**VirtualMachineToolsStatusEnum**](VirtualMachineToolsStatusEnum.md) |  | [optional] 
**tools_version_status** | **str** | Deprecated as of vSphere API 5.1 use *GuestInfo.toolsVersionStatus2*.  Current version status of VMware Tools in the guest operating system, if known.  The set of possible values is described in *VirtualMachineToolsVersionStatus_enum* for vSphere API 5.0.  ***Since:*** vSphere API 4.0  | [optional] 
**tools_version_status2** | **str** | Current version status of VMware Tools in the guest operating system, if known.  The set of possible values is described in *VirtualMachineToolsVersionStatus_enum*  ***Since:*** vSphere API 5.0  | [optional] 
**tools_running_status** | **str** | Current running status of VMware Tools in the guest operating system, if known.  The set of possible values is described in *VirtualMachineToolsRunningStatus_enum*  ***Since:*** vSphere API 4.0  | [optional] 
**tools_version** | **str** | Current version of VMware Tools, if known.  | [optional] 
**tools_install_type** | **str** | Current installation type of VMware Tools in the guest operating system.  The set of possible values is described in *VirtualMachineToolsInstallType_enum*  ***Since:*** vSphere API 6.5  | [optional] 
**guest_id** | **str** | Guest operating system identifier (short name), if known.  | [optional] 
**guest_family** | **str** | Guest operating system family, if known.  | [optional] 
**guest_full_name** | **str** | Guest operating system full name, if known.  | [optional] 
**host_name** | **str** | Hostname of the guest operating system, if known.  | [optional] 
**ip_address** | **str** | Primary IP address assigned to the guest operating system, if known.  | [optional] 
**net** | [**List[GuestNicInfo]**](GuestNicInfo.md) | Guest information about network adapters, if known.  | [optional] 
**ip_stack** | [**List[GuestStackInfo]**](GuestStackInfo.md) | Guest information about IP networking stack, if known.  ***Since:*** vSphere API 4.1  | [optional] 
**disk** | [**List[GuestDiskInfo]**](GuestDiskInfo.md) | Guest information about disks.  You can obtain Linux guest disk information for the following file system types: Ext2, Ext3, Ext4, ReiserFS, XFS, Btrfs, NTFS, VFAT, UFS, PCFS, HFS, and MS-DOS.  NOTE: Installing a more recent version of VMware Tools in the guest may help obtain disk information for more file system types. Please refer the VMware Tools User Guide for up-to-date supported file system types.  | [optional] 
**screen** | [**GuestScreenInfo**](GuestScreenInfo.md) |  | [optional] 
**guest_state** | **str** | Operation mode of guest operating system.  One of: - \&quot;running\&quot; - Guest is running normally. - \&quot;shuttingdown\&quot; - Guest has a pending shutdown command. - \&quot;resetting\&quot; - Guest has a pending reset command. - \&quot;standby\&quot; - Guest has a pending standby command. - \&quot;notrunning\&quot; - Guest is not running. - \&quot;unknown\&quot; - Guest information is not available.  | 
**app_heartbeat_status** | **str** | Application heartbeat status.  Please see *VirtualMachineAppHeartbeatStatusType_enum*  ***Since:*** vSphere API 4.1  | [optional] 
**guest_kernel_crashed** | **bool** | Guest operating system&#39;s kernel crash state.  If true, the guest operating system&#39;s kernel has crashed.  ***Since:*** vSphere API 6.0  | [optional] 
**app_state** | **str** | Application state.  If vSphere HA is enabled and the vm is configured for Application Monitoring and this field&#39;s value is \&quot;appStateNeedReset\&quot; then HA will attempt immediately reset the vm. There are some system conditions which may delay the immediate reset. The immediate reset will be performed as soon as allowed by vSphere HA and ESX. If during these conditions the value is changed to appStateOk the reset will be cancelled.  See also *GuestInfoAppStateType_enum*.  ***Since:*** vSphere API 5.5  | [optional] 
**guest_operations_ready** | **bool** | Guest Operations availability.  If true, the virtual machine is ready to process guest operations.  ***Since:*** vSphere API 5.0  | [optional] 
**interactive_guest_operations_ready** | **bool** | Interactive Guest Operations availability.  If true, the virtual machine is ready to process guest operations as the user interacting with the guest desktop.  ***Since:*** vSphere API 5.0  | [optional] 
**guest_state_change_supported** | **bool** | State change support.  If true, the virtual machine is ready to process soft power operations.  ***Since:*** vSphere API 6.0  | [optional] 
**generation_info** | [**List[GuestInfoNamespaceGenerationInfo]**](GuestInfoNamespaceGenerationInfo.md) | A list of namespaces and their corresponding generation numbers.  Only namespaces with non-zero *VirtualMachineNamespaceManagerCreateSpec.maxSizeEventsFromGuest* are guaranteed to be present here. Use *VirtualMachineNamespaceManager.ListNamespaces* to retrieve list of namespaces.  ***Since:*** vSphere API 5.1  | [optional] 
**hw_version** | **str** | The hardware version string for this virtual machine.  ***Since:*** vSphere API 6.9.1  | [optional] 
**customization_info** | [**GuestInfoCustomizationInfo**](GuestInfoCustomizationInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.guest_info import GuestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestInfo from a JSON string
guest_info_instance = GuestInfo.from_json(json)
# print the JSON string representation of the object
print GuestInfo.to_json()

# convert the object into a dict
guest_info_dict = guest_info_instance.to_dict()
# create an instance of GuestInfo from a dict
guest_info_form_dict = guest_info.from_dict(guest_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


