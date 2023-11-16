# HasProviderRequestType

The parameters of *HealthUpdateManager.HasProvider*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The provider id.  | 

## Example

```python
from vmware_vi.models.has_provider_request_type import HasProviderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HasProviderRequestType from a JSON string
has_provider_request_type_instance = HasProviderRequestType.from_json(json)
# print the JSON string representation of the object
print HasProviderRequestType.to_json()

# convert the object into a dict
has_provider_request_type_dict = has_provider_request_type_instance.to_dict()
# create an instance of HasProviderRequestType from a dict
has_provider_request_type_form_dict = has_provider_request_type.from_dict(has_provider_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


