# UpdateSystemResourcesRequestType

The parameters of *HostSystem.UpdateSystemResources*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_info** | [**HostSystemResourceInfo**](HostSystemResourceInfo.md) |  | 

## Example

```python
from vmware_vi.models.update_system_resources_request_type import UpdateSystemResourcesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSystemResourcesRequestType from a JSON string
update_system_resources_request_type_instance = UpdateSystemResourcesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateSystemResourcesRequestType.to_json()

# convert the object into a dict
update_system_resources_request_type_dict = update_system_resources_request_type_instance.to_dict()
# create an instance of UpdateSystemResourcesRequestType from a dict
update_system_resources_request_type_form_dict = update_system_resources_request_type.from_dict(update_system_resources_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


