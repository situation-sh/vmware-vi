# ArrayOfHostConfigChange

A boxed array of *HostConfigChange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigChange]**](HostConfigChange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_change import ArrayOfHostConfigChange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigChange from a JSON string
array_of_host_config_change_instance = ArrayOfHostConfigChange.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigChange.to_json()

# convert the object into a dict
array_of_host_config_change_dict = array_of_host_config_change_instance.to_dict()
# create an instance of ArrayOfHostConfigChange from a dict
array_of_host_config_change_form_dict = array_of_host_config_change.from_dict(array_of_host_config_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


