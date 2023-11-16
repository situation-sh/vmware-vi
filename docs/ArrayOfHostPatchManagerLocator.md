# ArrayOfHostPatchManagerLocator

A boxed array of *HostPatchManagerLocator*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPatchManagerLocator]**](HostPatchManagerLocator.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_patch_manager_locator import ArrayOfHostPatchManagerLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPatchManagerLocator from a JSON string
array_of_host_patch_manager_locator_instance = ArrayOfHostPatchManagerLocator.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPatchManagerLocator.to_json()

# convert the object into a dict
array_of_host_patch_manager_locator_dict = array_of_host_patch_manager_locator_instance.to_dict()
# create an instance of ArrayOfHostPatchManagerLocator from a dict
array_of_host_patch_manager_locator_form_dict = array_of_host_patch_manager_locator.from_dict(array_of_host_patch_manager_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


