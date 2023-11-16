# ArrayOfDiskChangeInfo

A boxed array of *DiskChangeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiskChangeInfo]**](DiskChangeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_disk_change_info import ArrayOfDiskChangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiskChangeInfo from a JSON string
array_of_disk_change_info_instance = ArrayOfDiskChangeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiskChangeInfo.to_json()

# convert the object into a dict
array_of_disk_change_info_dict = array_of_disk_change_info_instance.to_dict()
# create an instance of ArrayOfDiskChangeInfo from a dict
array_of_disk_change_info_form_dict = array_of_disk_change_info.from_dict(array_of_disk_change_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


