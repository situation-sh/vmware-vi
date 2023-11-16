# ArrayOfVmMetadataManagerFault

A boxed array of *VmMetadataManagerFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMetadataManagerFault]**](VmMetadataManagerFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_metadata_manager_fault import ArrayOfVmMetadataManagerFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMetadataManagerFault from a JSON string
array_of_vm_metadata_manager_fault_instance = ArrayOfVmMetadataManagerFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMetadataManagerFault.to_json()

# convert the object into a dict
array_of_vm_metadata_manager_fault_dict = array_of_vm_metadata_manager_fault_instance.to_dict()
# create an instance of ArrayOfVmMetadataManagerFault from a dict
array_of_vm_metadata_manager_fault_form_dict = array_of_vm_metadata_manager_fault.from_dict(array_of_vm_metadata_manager_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


