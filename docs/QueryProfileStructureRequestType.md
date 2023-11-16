# QueryProfileStructureRequestType

The parameters of *HostProfileManager.QueryProfileStructure*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_profile_structure_request_type import QueryProfileStructureRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryProfileStructureRequestType from a JSON string
query_profile_structure_request_type_instance = QueryProfileStructureRequestType.from_json(json)
# print the JSON string representation of the object
print QueryProfileStructureRequestType.to_json()

# convert the object into a dict
query_profile_structure_request_type_dict = query_profile_structure_request_type_instance.to_dict()
# create an instance of QueryProfileStructureRequestType from a dict
query_profile_structure_request_type_form_dict = query_profile_structure_request_type.from_dict(query_profile_structure_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


