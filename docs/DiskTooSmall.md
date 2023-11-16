# DiskTooSmall

Fault used for disks which are too small for usage by VSAN.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_too_small import DiskTooSmall

# TODO update the JSON string below
json = "{}"
# create an instance of DiskTooSmall from a JSON string
disk_too_small_instance = DiskTooSmall.from_json(json)
# print the JSON string representation of the object
print DiskTooSmall.to_json()

# convert the object into a dict
disk_too_small_dict = disk_too_small_instance.to_dict()
# create an instance of DiskTooSmall from a dict
disk_too_small_form_dict = disk_too_small.from_dict(disk_too_small_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


