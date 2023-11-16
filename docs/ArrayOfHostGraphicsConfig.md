# ArrayOfHostGraphicsConfig

A boxed array of *HostGraphicsConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostGraphicsConfig]**](HostGraphicsConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_graphics_config import ArrayOfHostGraphicsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostGraphicsConfig from a JSON string
array_of_host_graphics_config_instance = ArrayOfHostGraphicsConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostGraphicsConfig.to_json()

# convert the object into a dict
array_of_host_graphics_config_dict = array_of_host_graphics_config_instance.to_dict()
# create an instance of ArrayOfHostGraphicsConfig from a dict
array_of_host_graphics_config_form_dict = array_of_host_graphics_config.from_dict(array_of_host_graphics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


