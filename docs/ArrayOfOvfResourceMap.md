# ArrayOfOvfResourceMap

A boxed array of *OvfResourceMap*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfResourceMap]**](OvfResourceMap.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_resource_map import ArrayOfOvfResourceMap

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfResourceMap from a JSON string
array_of_ovf_resource_map_instance = ArrayOfOvfResourceMap.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfResourceMap.to_json()

# convert the object into a dict
array_of_ovf_resource_map_dict = array_of_ovf_resource_map_instance.to_dict()
# create an instance of ArrayOfOvfResourceMap from a dict
array_of_ovf_resource_map_form_dict = array_of_ovf_resource_map.from_dict(array_of_ovf_resource_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


