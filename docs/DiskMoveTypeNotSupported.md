# DiskMoveTypeNotSupported

Specifying non-standard disk movement types is not supported.  See also *VirtualMachineRelocateSpec.diskMoveType*, *VirtualMachineRelocateSpecDiskLocator.diskMoveType*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_move_type_not_supported import DiskMoveTypeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DiskMoveTypeNotSupported from a JSON string
disk_move_type_not_supported_instance = DiskMoveTypeNotSupported.from_json(json)
# print the JSON string representation of the object
print DiskMoveTypeNotSupported.to_json()

# convert the object into a dict
disk_move_type_not_supported_dict = disk_move_type_not_supported_instance.to_dict()
# create an instance of DiskMoveTypeNotSupported from a dict
disk_move_type_not_supported_form_dict = disk_move_type_not_supported.from_dict(disk_move_type_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


