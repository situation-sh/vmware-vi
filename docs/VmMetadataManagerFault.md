# VmMetadataManagerFault

This fault indicates that some error has occurred during the processing of of a MetadataManager operation.  This may be subclassed by a more specific fault.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_metadata_manager_fault import VmMetadataManagerFault

# TODO update the JSON string below
json = "{}"
# create an instance of VmMetadataManagerFault from a JSON string
vm_metadata_manager_fault_instance = VmMetadataManagerFault.from_json(json)
# print the JSON string representation of the object
print VmMetadataManagerFault.to_json()

# convert the object into a dict
vm_metadata_manager_fault_dict = vm_metadata_manager_fault_instance.to_dict()
# create an instance of VmMetadataManagerFault from a dict
vm_metadata_manager_fault_form_dict = vm_metadata_manager_fault.from_dict(vm_metadata_manager_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


