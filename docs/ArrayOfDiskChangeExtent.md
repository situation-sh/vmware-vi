# ArrayOfDiskChangeExtent

A boxed array of *DiskChangeExtent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiskChangeExtent]**](DiskChangeExtent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_disk_change_extent import ArrayOfDiskChangeExtent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiskChangeExtent from a JSON string
array_of_disk_change_extent_instance = ArrayOfDiskChangeExtent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiskChangeExtent.to_json()

# convert the object into a dict
array_of_disk_change_extent_dict = array_of_disk_change_extent_instance.to_dict()
# create an instance of ArrayOfDiskChangeExtent from a dict
array_of_disk_change_extent_form_dict = array_of_disk_change_extent.from_dict(array_of_disk_change_extent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


