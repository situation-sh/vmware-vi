# VmfsAlreadyMounted

A VmfsAlreadyMounted fault indicates that VMFS volume with same UUID is already mounted on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmfs_already_mounted import VmfsAlreadyMounted

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsAlreadyMounted from a JSON string
vmfs_already_mounted_instance = VmfsAlreadyMounted.from_json(json)
# print the JSON string representation of the object
print VmfsAlreadyMounted.to_json()

# convert the object into a dict
vmfs_already_mounted_dict = vmfs_already_mounted_instance.to_dict()
# create an instance of VmfsAlreadyMounted from a dict
vmfs_already_mounted_form_dict = vmfs_already_mounted.from_dict(vmfs_already_mounted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


