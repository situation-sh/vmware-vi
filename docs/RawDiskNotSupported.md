# RawDiskNotSupported

The virtual machine has a raw disk attached that is not supported.  This is often used as a subfault for DisallowedMigrationDeviceAttached or DisallowedSnapshotDeviceAttached. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.raw_disk_not_supported import RawDiskNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of RawDiskNotSupported from a JSON string
raw_disk_not_supported_instance = RawDiskNotSupported.from_json(json)
# print the JSON string representation of the object
print RawDiskNotSupported.to_json()

# convert the object into a dict
raw_disk_not_supported_dict = raw_disk_not_supported_instance.to_dict()
# create an instance of RawDiskNotSupported from a dict
raw_disk_not_supported_form_dict = raw_disk_not_supported.from_dict(raw_disk_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


