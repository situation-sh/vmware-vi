# VirtualMachineFlagInfo

The FlagInfo data object type encapsulates the flag settings for a virtual machine.  These properties are optional since the same structure is used to change the values during an edit or create operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_acceleration** | **bool** | Flag to turn off video acceleration for a virtual machine console window.  | [optional] 
**enable_logging** | **bool** | Flag to enable logging for a virtual machine.  | [optional] 
**use_toe** | **bool** | Flag to specify whether or not to use TOE (TCP/IP Offloading).  | [optional] 
**run_with_debug_info** | **bool** | Deprecated as of VI API 2.5, use *VirtualMachineFlagInfo.monitorType*.  Flag to specify whether or not to run in debug mode.  | [optional] 
**monitor_type** | **str** | vmx process type.  See *VirtualMachineFlagInfoMonitorType_enum* for possible values for this property.  ***Since:*** VI API 2.5  | [optional] 
**ht_sharing** | **str** | Deprecated as of vSphere API 6.7.  Specifies how the VCPUs of a virtual machine are allowed to share physical cores on a hyperthreaded system.  Two VCPUs are \&quot;sharing\&quot; a core if they are both running on logical CPUs of the core at the same time.  See also *VirtualMachineHtSharing_enum*.  | [optional] 
**snapshot_disabled** | **bool** | Deprecated as of vSphere API 4.0. The flag is ignored by the server.  Flag to specify whether snapshots are disabled for this virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**snapshot_locked** | **bool** | Flag to specify whether the snapshot tree is locked for this virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**disk_uuid_enabled** | **bool** | Indicates whether disk UUIDs are being used by this virtual machine.  If this flag is set to false, disk UUIDs are not exposed to the guest.  Since products before ESX 3.1 do not support disk UUIDs, moving virtual machines from a platform that supports UUID to a platform that does not support UUIDs could result in unspecified guest behavior. For virtual machines where the ability to move to older platforms is important, this flag should be set to false. If the value is unset, the behavior &#39;false&#39; will be used.  ***Since:*** VI API 2.5  | [optional] 
**virtual_mmu_usage** | **str** | Indicates whether or not the system will try to use nested page table hardware support, if available.  By default, VMware software will determine whether or not to use nested page table hardware support based on various factors such as the guest operating system type and the physical hardware. Certain workloads can benefit from explicitly turning nested page table hardware support on or off; this can be set using nptUsage flag. If the value is unset, the value will default to automatic.  *VirtualMachineFlagInfoVirtualMmuUsage_enum* represents the set of possible values.  ***Since:*** VI API 2.5  | [optional] 
**virtual_exec_usage** | **str** | Indicates whether or not the system will try to use Hardware Virtualization (HV) support for instruction virtualization, if available.  By default, VMware software will determine whether or not to use hardware virtualization support based on various factors such as the guest operating system type and the physical hardware. Certain workloads can benefit from explicitly turning hardware virtualization support on or off. If the value is unset, the value will default to hvAuto.  *VirtualMachineFlagInfoVirtualExecUsage_enum* represents the set of possible values.  New processors can enable two hardware acceleration technologies for virtualization, one for instruction virtualization and the other for MMU virtualization. Intel names its hardware-assisted instruction virtualization as VT, and its hardware-assisted MMU virtualization as EPT. AMD calls them as AMD-V and RVI, respectively. For details on these technologies, please refer to documents from the processor vendors.  *VirtualMachineFlagInfo.virtualExecUsage* controls instruction virtualization; while *VirtualMachineFlagInfo.virtualMmuUsage* controls MMU virtualization. \&quot;On\&quot; allows hardware acceleration, while \&quot;off\&quot; only allows software solution.  There are four meaningful combinations.  (hvAuto, automatic) - The host chooses which feature to use. (hvOn, on) - Use both VT/AMD-V and EPT/RVI. (hvOn, off) - Use VT/AMD-V but do not use EPT/RVI. (hvOff, off) - Do not use any of these hardware acceleration technologies.  ***Since:*** vSphere API 4.0  | [optional] 
**snapshot_power_off_behavior** | **str** | Specifies the power-off behavior for a virtual machine that has a snapshot.  If the value is unset, the behavior &#39;powerOff&#39; will be used.  See also *VirtualMachinePowerOffBehavior_enum*.  ***Since:*** VI API 2.5  | [optional] 
**record_replay_enabled** | **bool** | Deprecated as of vSphere API 6.0.  Flag to specify whether record and replay operations are allowed for this virtual machine.  If this flag is set to &#39;true&#39;, instruction virtualization will use hardware virtualization (HV) support. I.e., virtualExecUsage will be set to &#39;hvOn&#39;. If this flag is set to &#39;false&#39; for a virtual machine that already has a recording, replay will be disallowed, though the recording will be preserved. If the value is unset, the behavior &#39;false&#39; will be used.  ***Since:*** vSphere API 4.0  | [optional] 
**fault_tolerance_type** | **str** | Indicates the type of fault tolerance type the virtual machine is configured to use.  *VirtualMachineFaultToleranceType_enum* represents the set of possible values.  ***Since:*** vSphere API 6.0  | [optional] 
**cbrc_cache_enabled** | **bool** | Flag to specify whether common CBRC digest cache is enabled for this virtual machine.  The common CBRC cache is shared between the hot added disks in the VM. If this flag is set to &#39;true&#39; the VM will allocate a commont digest cache on power on.  ***Since:*** vSphere API 6.5  | [optional] 
**vvtd_enabled** | **bool** | Flag to specify if Intel Virtualization Technology for Directed I/O is enabled for this virtual machine.  When creating a new VM: \\- If vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt;, and this flag is set to &lt;code&gt;false&lt;/code&gt; error is returned. \\- If this flag is unset and vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt;, the value of this flag is set to &lt;code&gt;true&lt;/code&gt;.  ***Since:*** vSphere API 6.7  | [optional] 
**vbs_enabled** | **bool** | Flag to specify if Virtualization-based security is enabled for this virtual machine.  If set to &lt;code&gt;true&lt;/code&gt; when creating a new VM, the following VM properties might be modified automatically: \\- If vim.vm.FlagInfo.vvtdEnabled is not set to &lt;code&gt;false&lt;/code&gt;, it is set to &lt;code&gt;true&lt;/code&gt;. Else error is returned. \\- If vim.vm.ConfigSpec.nestedHVEnabled is not set to &lt;code&gt;false&lt;/code&gt;, it is set to &lt;code&gt;true&lt;/code&gt;. Else error is returned. \\- If vim.vm.BootOptions.efiSecureBootEnabled is not set to &lt;code&gt;false&lt;/code&gt;, it is set to &lt;code&gt;true&lt;/code&gt;. Else error is returned. \\- If vim.vm.firmware is not set to &lt;code&gt;bios&lt;/code&gt;, it is set to &lt;code&gt;efi&lt;/code&gt;. Else error is returned.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_flag_info import VirtualMachineFlagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFlagInfo from a JSON string
virtual_machine_flag_info_instance = VirtualMachineFlagInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFlagInfo.to_json()

# convert the object into a dict
virtual_machine_flag_info_dict = virtual_machine_flag_info_instance.to_dict()
# create an instance of VirtualMachineFlagInfo from a dict
virtual_machine_flag_info_form_dict = virtual_machine_flag_info.from_dict(virtual_machine_flag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


