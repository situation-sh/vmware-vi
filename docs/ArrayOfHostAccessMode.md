# ArrayOfHostAccessMode

A boxed array of *HostAccessMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAccessModeEnum]**](HostAccessModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_access_mode import ArrayOfHostAccessMode

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAccessMode from a JSON string
array_of_host_access_mode_instance = ArrayOfHostAccessMode.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAccessMode.to_json()

# convert the object into a dict
array_of_host_access_mode_dict = array_of_host_access_mode_instance.to_dict()
# create an instance of ArrayOfHostAccessMode from a dict
array_of_host_access_mode_form_dict = array_of_host_access_mode.from_dict(array_of_host_access_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


