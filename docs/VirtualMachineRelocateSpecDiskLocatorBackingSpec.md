# VirtualMachineRelocateSpecDiskLocatorBackingSpec

<code>*VirtualMachineRelocateSpecDiskLocatorBackingSpec*</code> is a data object type for crytographic information about the backing of a device.  The member *VirtualMachineRelocateSpecDiskLocatorBackingSpec.parent* refers the parent in the chain of *VirtualDeviceBackingInfo* objects.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**VirtualMachineRelocateSpecDiskLocatorBackingSpec**](VirtualMachineRelocateSpecDiskLocatorBackingSpec.md) |  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_relocate_spec_disk_locator_backing_spec import VirtualMachineRelocateSpecDiskLocatorBackingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRelocateSpecDiskLocatorBackingSpec from a JSON string
virtual_machine_relocate_spec_disk_locator_backing_spec_instance = VirtualMachineRelocateSpecDiskLocatorBackingSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRelocateSpecDiskLocatorBackingSpec.to_json()

# convert the object into a dict
virtual_machine_relocate_spec_disk_locator_backing_spec_dict = virtual_machine_relocate_spec_disk_locator_backing_spec_instance.to_dict()
# create an instance of VirtualMachineRelocateSpecDiskLocatorBackingSpec from a dict
virtual_machine_relocate_spec_disk_locator_backing_spec_form_dict = virtual_machine_relocate_spec_disk_locator_backing_spec.from_dict(virtual_machine_relocate_spec_disk_locator_backing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


