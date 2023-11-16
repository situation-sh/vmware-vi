# QueryManagedByRequestType

The parameters of *ExtensionManager.QueryManagedBy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of the extension to find managed entities for.  | 

## Example

```python
from vmware_vi.models.query_managed_by_request_type import QueryManagedByRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryManagedByRequestType from a JSON string
query_managed_by_request_type_instance = QueryManagedByRequestType.from_json(json)
# print the JSON string representation of the object
print QueryManagedByRequestType.to_json()

# convert the object into a dict
query_managed_by_request_type_dict = query_managed_by_request_type_instance.to_dict()
# create an instance of QueryManagedByRequestType from a dict
query_managed_by_request_type_form_dict = query_managed_by_request_type.from_dict(query_managed_by_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


