# ArrayOfHostDiskDimensions

A boxed array of *HostDiskDimensions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskDimensions]**](HostDiskDimensions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_dimensions import ArrayOfHostDiskDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskDimensions from a JSON string
array_of_host_disk_dimensions_instance = ArrayOfHostDiskDimensions.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskDimensions.to_json()

# convert the object into a dict
array_of_host_disk_dimensions_dict = array_of_host_disk_dimensions_instance.to_dict()
# create an instance of ArrayOfHostDiskDimensions from a dict
array_of_host_disk_dimensions_form_dict = array_of_host_disk_dimensions.from_dict(array_of_host_disk_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


