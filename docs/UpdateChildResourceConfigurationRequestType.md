# UpdateChildResourceConfigurationRequestType

The parameters of *ResourcePool.UpdateChildResourceConfiguration*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**List[ResourceConfigSpec]**](ResourceConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_child_resource_configuration_request_type import UpdateChildResourceConfigurationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChildResourceConfigurationRequestType from a JSON string
update_child_resource_configuration_request_type_instance = UpdateChildResourceConfigurationRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateChildResourceConfigurationRequestType.to_json()

# convert the object into a dict
update_child_resource_configuration_request_type_dict = update_child_resource_configuration_request_type_instance.to_dict()
# create an instance of UpdateChildResourceConfigurationRequestType from a dict
update_child_resource_configuration_request_type_form_dict = update_child_resource_configuration_request_type.from_dict(update_child_resource_configuration_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


