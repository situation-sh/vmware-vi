# HostDiskDimensions

This data object type describes multiple coordinate systems used to refer to a location or size on a disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_disk_dimensions import HostDiskDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskDimensions from a JSON string
host_disk_dimensions_instance = HostDiskDimensions.from_json(json)
# print the JSON string representation of the object
print HostDiskDimensions.to_json()

# convert the object into a dict
host_disk_dimensions_dict = host_disk_dimensions_instance.to_dict()
# create an instance of HostDiskDimensions from a dict
host_disk_dimensions_form_dict = host_disk_dimensions.from_dict(host_disk_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


