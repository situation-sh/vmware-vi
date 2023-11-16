# VirtualMachineInstantCloneSpec

Specification for creating an Instant Clone of a powered-on virtual machine.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the cloned virtual machine.  ***Since:*** vSphere API 6.7  | 
**location** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | 
**config** | [**List[OptionValue]**](OptionValue.md) | A list of key value pairs that will be passed to the destination VM.  These pairs should be used to provide user-defined customization to differentiate the destination VM from the source VM. Values will be queryable via destination VM&#39;s *VirtualMachineConfigInfo.extraConfig*.  ***Since:*** vSphere API 6.7  | [optional] 
**bios_uuid** | **str** | 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in \&quot;12345678-abcd-1234-cdef-123456789abc\&quot; format.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_instant_clone_spec import VirtualMachineInstantCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineInstantCloneSpec from a JSON string
virtual_machine_instant_clone_spec_instance = VirtualMachineInstantCloneSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineInstantCloneSpec.to_json()

# convert the object into a dict
virtual_machine_instant_clone_spec_dict = virtual_machine_instant_clone_spec_instance.to_dict()
# create an instance of VirtualMachineInstantCloneSpec from a dict
virtual_machine_instant_clone_spec_form_dict = virtual_machine_instant_clone_spec.from_dict(virtual_machine_instant_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


