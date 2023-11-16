# QueryTargetCapabilitiesRequestType

The parameters of *EnvironmentBrowser.QueryTargetCapabilities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_target_capabilities_request_type import QueryTargetCapabilitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTargetCapabilitiesRequestType from a JSON string
query_target_capabilities_request_type_instance = QueryTargetCapabilitiesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryTargetCapabilitiesRequestType.to_json()

# convert the object into a dict
query_target_capabilities_request_type_dict = query_target_capabilities_request_type_instance.to_dict()
# create an instance of QueryTargetCapabilitiesRequestType from a dict
query_target_capabilities_request_type_form_dict = query_target_capabilities_request_type.from_dict(query_target_capabilities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


