# ArrayOfHostConfigManager

A boxed array of *HostConfigManager*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigManager]**](HostConfigManager.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_manager import ArrayOfHostConfigManager

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigManager from a JSON string
array_of_host_config_manager_instance = ArrayOfHostConfigManager.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigManager.to_json()

# convert the object into a dict
array_of_host_config_manager_dict = array_of_host_config_manager_instance.to_dict()
# create an instance of ArrayOfHostConfigManager from a dict
array_of_host_config_manager_form_dict = array_of_host_config_manager.from_dict(array_of_host_config_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


