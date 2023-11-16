# UnregisterHealthUpdateProviderRequestType

The parameters of *HealthUpdateManager.UnregisterHealthUpdateProvider*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 

## Example

```python
from vmware_vi.models.unregister_health_update_provider_request_type import UnregisterHealthUpdateProviderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterHealthUpdateProviderRequestType from a JSON string
unregister_health_update_provider_request_type_instance = UnregisterHealthUpdateProviderRequestType.from_json(json)
# print the JSON string representation of the object
print UnregisterHealthUpdateProviderRequestType.to_json()

# convert the object into a dict
unregister_health_update_provider_request_type_dict = unregister_health_update_provider_request_type_instance.to_dict()
# create an instance of UnregisterHealthUpdateProviderRequestType from a dict
unregister_health_update_provider_request_type_form_dict = unregister_health_update_provider_request_type.from_dict(unregister_health_update_provider_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


