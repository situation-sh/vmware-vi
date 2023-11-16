# HostUnresolvedVmfsResignatureSpec

Specification to resignature an Unresolved VMFS volume.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extent_device_path** | **List[str]** | List of device path each specifying VMFS extents.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_unresolved_vmfs_resignature_spec import HostUnresolvedVmfsResignatureSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostUnresolvedVmfsResignatureSpec from a JSON string
host_unresolved_vmfs_resignature_spec_instance = HostUnresolvedVmfsResignatureSpec.from_json(json)
# print the JSON string representation of the object
print HostUnresolvedVmfsResignatureSpec.to_json()

# convert the object into a dict
host_unresolved_vmfs_resignature_spec_dict = host_unresolved_vmfs_resignature_spec_instance.to_dict()
# create an instance of HostUnresolvedVmfsResignatureSpec from a dict
host_unresolved_vmfs_resignature_spec_form_dict = host_unresolved_vmfs_resignature_spec.from_dict(host_unresolved_vmfs_resignature_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


