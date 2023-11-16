# ArrayOfHostAutoStartManagerConfig

A boxed array of *HostAutoStartManagerConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAutoStartManagerConfig]**](HostAutoStartManagerConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_auto_start_manager_config import ArrayOfHostAutoStartManagerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAutoStartManagerConfig from a JSON string
array_of_host_auto_start_manager_config_instance = ArrayOfHostAutoStartManagerConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAutoStartManagerConfig.to_json()

# convert the object into a dict
array_of_host_auto_start_manager_config_dict = array_of_host_auto_start_manager_config_instance.to_dict()
# create an instance of ArrayOfHostAutoStartManagerConfig from a dict
array_of_host_auto_start_manager_config_form_dict = array_of_host_auto_start_manager_config.from_dict(array_of_host_auto_start_manager_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


