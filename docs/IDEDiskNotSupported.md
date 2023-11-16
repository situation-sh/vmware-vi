# IDEDiskNotSupported

Deprecated as of VI API 2.5, use *DeviceControllerNotSupported*.  The virtual machine uses a virtual disk with an IDE controller, but this is not supported on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ide_disk_not_supported import IDEDiskNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of IDEDiskNotSupported from a JSON string
ide_disk_not_supported_instance = IDEDiskNotSupported.from_json(json)
# print the JSON string representation of the object
print IDEDiskNotSupported.to_json()

# convert the object into a dict
ide_disk_not_supported_dict = ide_disk_not_supported_instance.to_dict()
# create an instance of IDEDiskNotSupported from a dict
ide_disk_not_supported_form_dict = ide_disk_not_supported.from_dict(ide_disk_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


