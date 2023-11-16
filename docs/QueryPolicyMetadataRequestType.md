# QueryPolicyMetadataRequestType

The parameters of *ProfileManager.QueryPolicyMetadata*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_name** | **List[str]** | Retrieve metadata for the specified policyNames. If policyName is not specified, metadata for all policies will be returned.  | [optional] 
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_policy_metadata_request_type import QueryPolicyMetadataRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPolicyMetadataRequestType from a JSON string
query_policy_metadata_request_type_instance = QueryPolicyMetadataRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPolicyMetadataRequestType.to_json()

# convert the object into a dict
query_policy_metadata_request_type_dict = query_policy_metadata_request_type_instance.to_dict()
# create an instance of QueryPolicyMetadataRequestType from a dict
query_policy_metadata_request_type_form_dict = query_policy_metadata_request_type.from_dict(query_policy_metadata_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


