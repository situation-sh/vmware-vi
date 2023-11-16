# NonPersistentDisksNotSupported

The virtual machine has nonpersistent virtual disk.  This is an error for any powered-on migration which involves moving virtual disks.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.non_persistent_disks_not_supported import NonPersistentDisksNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of NonPersistentDisksNotSupported from a JSON string
non_persistent_disks_not_supported_instance = NonPersistentDisksNotSupported.from_json(json)
# print the JSON string representation of the object
print NonPersistentDisksNotSupported.to_json()

# convert the object into a dict
non_persistent_disks_not_supported_dict = non_persistent_disks_not_supported_instance.to_dict()
# create an instance of NonPersistentDisksNotSupported from a dict
non_persistent_disks_not_supported_form_dict = non_persistent_disks_not_supported.from_dict(non_persistent_disks_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


