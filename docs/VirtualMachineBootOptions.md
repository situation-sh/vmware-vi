# VirtualMachineBootOptions

The *VirtualMachineBootOptions* data object defines the boot-time behavior of a virtual machine.  You can use the delay options to specify a time interval during which you can enter the virtual machine BIOS setup. These options provide a solution for the situation that occurs when the console attaches to the virtual machine after the boot sequence has passed the BIOS setup entry point.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_delay** | **int** | Delay in milliseconds before starting the boot sequence.  The boot delay specifies a time interval between virtual machine power on or restart and the beginning of the boot sequence.  ***Since:*** VI API 2.5  | [optional] 
**enter_bios_setup** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the virtual machine automatically enters BIOS setup the next time it boots.  The virtual machine resets this flag to &lt;code&gt;false&lt;/code&gt; so that subsequent boots proceed normally.  ***Since:*** VI API 2.5  | [optional] 
**efi_secure_boot_enabled** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the virtual machine&#39;s firmware will perform signature checks of any EFI images loaded during startup, and will refuse to start any images which do not pass those signature checks.  When creating a new VM: \\- If vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt;, and this flag is set to &lt;code&gt;false&lt;/code&gt; error is returned. \\- If this flag is unset and vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt;, the value of this flag is set to &lt;code&gt;true&lt;/code&gt;.  ***Since:*** vSphere API 6.5  | [optional] 
**boot_retry_enabled** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, a virtual machine that fails to boot will try again after the *VirtualMachineBootOptions.bootRetryDelay* time period has expired.  When &lt;code&gt;false&lt;/code&gt;, the virtual machine waits indefinitely for you to initiate boot retry.  ***Since:*** vSphere API 4.1  | [optional] 
**boot_retry_delay** | **int** | Delay in milliseconds before a boot retry.  The boot retry delay specifies a time interval between virtual machine boot failure and the subsequent attempt to boot again. The virtual machine uses this value only if *VirtualMachineBootOptions.bootRetryEnabled* is true.  ***Since:*** vSphere API 4.1  | [optional] 
**boot_order** | [**List[VirtualMachineBootOptionsBootableDevice]**](VirtualMachineBootOptionsBootableDevice.md) | Boot order.  Listed devices are used for booting. After list is exhausted, default BIOS boot device algorithm is used for booting. Note that order of the entries in the list is important: device listed first is used for boot first, if that one fails second entry is used, and so on. Platform may have some internal limit on the number of devices it supports. If bootable device is not reached before platform&#39;s limit is hit, boot will fail. At least single entry is supported by all products supporting boot order settings.  ***Since:*** vSphere API 5.0  | [optional] 
**network_boot_protocol** | **str** | Protocol to attempt during PXE network boot or NetBoot.  See also *VirtualMachineBootOptionsNetworkBootProtocolType_enum*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_boot_options import VirtualMachineBootOptions

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineBootOptions from a JSON string
virtual_machine_boot_options_instance = VirtualMachineBootOptions.from_json(json)
# print the JSON string representation of the object
print VirtualMachineBootOptions.to_json()

# convert the object into a dict
virtual_machine_boot_options_dict = virtual_machine_boot_options_instance.to_dict()
# create an instance of VirtualMachineBootOptions from a dict
virtual_machine_boot_options_form_dict = virtual_machine_boot_options.from_dict(virtual_machine_boot_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


