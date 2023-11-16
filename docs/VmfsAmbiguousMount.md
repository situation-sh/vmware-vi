# VmfsAmbiguousMount

An 'VmfsAmbiguousMount' fault occurs when ESX is unable to resolve the extents of a VMFS volume unambiguously.  This is thrown only when a VMFS volume has multiple extents and multiple copies of VMFS volumes are available. VMFS layer will not be able to determine how to re-construct the VMFS volume as multiple choices are available.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmfs_ambiguous_mount import VmfsAmbiguousMount

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsAmbiguousMount from a JSON string
vmfs_ambiguous_mount_instance = VmfsAmbiguousMount.from_json(json)
# print the JSON string representation of the object
print VmfsAmbiguousMount.to_json()

# convert the object into a dict
vmfs_ambiguous_mount_dict = vmfs_ambiguous_mount_instance.to_dict()
# create an instance of VmfsAmbiguousMount from a dict
vmfs_ambiguous_mount_form_dict = vmfs_ambiguous_mount.from_dict(vmfs_ambiguous_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


