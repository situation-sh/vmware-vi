# VmfsMountFault

This is a base class for all VMFS volume mount related faults.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Vmfs volume uuid  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vmfs_mount_fault import VmfsMountFault

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsMountFault from a JSON string
vmfs_mount_fault_instance = VmfsMountFault.from_json(json)
# print the JSON string representation of the object
print VmfsMountFault.to_json()

# convert the object into a dict
vmfs_mount_fault_dict = vmfs_mount_fault_instance.to_dict()
# create an instance of VmfsMountFault from a dict
vmfs_mount_fault_form_dict = vmfs_mount_fault.from_dict(vmfs_mount_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


