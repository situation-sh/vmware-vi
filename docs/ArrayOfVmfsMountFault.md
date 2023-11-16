# ArrayOfVmfsMountFault

A boxed array of *VmfsMountFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsMountFault]**](VmfsMountFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_mount_fault import ArrayOfVmfsMountFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsMountFault from a JSON string
array_of_vmfs_mount_fault_instance = ArrayOfVmfsMountFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsMountFault.to_json()

# convert the object into a dict
array_of_vmfs_mount_fault_dict = array_of_vmfs_mount_fault_instance.to_dict()
# create an instance of ArrayOfVmfsMountFault from a dict
array_of_vmfs_mount_fault_form_dict = array_of_vmfs_mount_fault.from_dict(array_of_vmfs_mount_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


