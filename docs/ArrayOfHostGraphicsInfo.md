# ArrayOfHostGraphicsInfo

A boxed array of *HostGraphicsInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostGraphicsInfo]**](HostGraphicsInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_graphics_info import ArrayOfHostGraphicsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostGraphicsInfo from a JSON string
array_of_host_graphics_info_instance = ArrayOfHostGraphicsInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostGraphicsInfo.to_json()

# convert the object into a dict
array_of_host_graphics_info_dict = array_of_host_graphics_info_instance.to_dict()
# create an instance of ArrayOfHostGraphicsInfo from a dict
array_of_host_graphics_info_form_dict = array_of_host_graphics_info.from_dict(array_of_host_graphics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


