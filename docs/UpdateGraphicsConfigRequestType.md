# UpdateGraphicsConfigRequestType

The parameters of *HostGraphicsManager.UpdateGraphicsConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostGraphicsConfig**](HostGraphicsConfig.md) |  | 

## Example

```python
from vmware_vi.models.update_graphics_config_request_type import UpdateGraphicsConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGraphicsConfigRequestType from a JSON string
update_graphics_config_request_type_instance = UpdateGraphicsConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateGraphicsConfigRequestType.to_json()

# convert the object into a dict
update_graphics_config_request_type_dict = update_graphics_config_request_type_instance.to_dict()
# create an instance of UpdateGraphicsConfigRequestType from a dict
update_graphics_config_request_type_form_dict = update_graphics_config_request_type.from_dict(update_graphics_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


