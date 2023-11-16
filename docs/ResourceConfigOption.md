# ResourceConfigOption

This data object type is a default value and value range specification for *ResourceConfigSpec* object.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_allocation_option** | [**ResourceAllocationOption**](ResourceAllocationOption.md) |  | 
**memory_allocation_option** | [**ResourceAllocationOption**](ResourceAllocationOption.md) |  | 

## Example

```python
from vmware_vi.models.resource_config_option import ResourceConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConfigOption from a JSON string
resource_config_option_instance = ResourceConfigOption.from_json(json)
# print the JSON string representation of the object
print ResourceConfigOption.to_json()

# convert the object into a dict
resource_config_option_dict = resource_config_option_instance.to_dict()
# create an instance of ResourceConfigOption from a dict
resource_config_option_form_dict = resource_config_option.from_dict(resource_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


