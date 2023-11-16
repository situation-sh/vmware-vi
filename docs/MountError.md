# MountError

Customization failed because the customization process was unable to mount a remote virtual disk file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk_index** | **int** | Index into the virtual machine&#39;s device list, representing the key value that identifies the virtual device that is the presumed boot disk.  | 

## Example

```python
from vmware_vi.models.mount_error import MountError

# TODO update the JSON string below
json = "{}"
# create an instance of MountError from a JSON string
mount_error_instance = MountError.from_json(json)
# print the JSON string representation of the object
print MountError.to_json()

# convert the object into a dict
mount_error_dict = mount_error_instance.to_dict()
# create an instance of MountError from a dict
mount_error_form_dict = mount_error.from_dict(mount_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


