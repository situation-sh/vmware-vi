# DiskNotSupported

The host does not support the backings for the disks specified by the virtual machine.  For example, this fault is thrown if a virtual machine is created from a template that specifies backings that the host does not have. Similarly, this fault is thrown if a virtual machine is registered on a host that does not support the specified backings. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **int** | The ID of disk that is not supported.  | 

## Example

```python
from vmware_vi.models.disk_not_supported import DiskNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DiskNotSupported from a JSON string
disk_not_supported_instance = DiskNotSupported.from_json(json)
# print the JSON string representation of the object
print DiskNotSupported.to_json()

# convert the object into a dict
disk_not_supported_dict = disk_not_supported_instance.to_dict()
# create an instance of DiskNotSupported from a dict
disk_not_supported_form_dict = disk_not_supported.from_dict(disk_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


