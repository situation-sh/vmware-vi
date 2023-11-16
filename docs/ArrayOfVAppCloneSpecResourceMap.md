# ArrayOfVAppCloneSpecResourceMap

A boxed array of *VAppCloneSpecResourceMap*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppCloneSpecResourceMap]**](VAppCloneSpecResourceMap.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_clone_spec_resource_map import ArrayOfVAppCloneSpecResourceMap

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppCloneSpecResourceMap from a JSON string
array_of_v_app_clone_spec_resource_map_instance = ArrayOfVAppCloneSpecResourceMap.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppCloneSpecResourceMap.to_json()

# convert the object into a dict
array_of_v_app_clone_spec_resource_map_dict = array_of_v_app_clone_spec_resource_map_instance.to_dict()
# create an instance of ArrayOfVAppCloneSpecResourceMap from a dict
array_of_v_app_clone_spec_resource_map_form_dict = array_of_v_app_clone_spec_resource_map.from_dict(array_of_v_app_clone_spec_resource_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


