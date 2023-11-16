# QueryExpressionMetadataRequestType

The parameters of *ProfileComplianceManager.QueryExpressionMetadata*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_name** | **List[str]** | Names of the Expressions for which metadata is requested. If expressionNames are not specified, metadata for all known expressions is returned  | [optional] 
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_expression_metadata_request_type import QueryExpressionMetadataRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryExpressionMetadataRequestType from a JSON string
query_expression_metadata_request_type_instance = QueryExpressionMetadataRequestType.from_json(json)
# print the JSON string representation of the object
print QueryExpressionMetadataRequestType.to_json()

# convert the object into a dict
query_expression_metadata_request_type_dict = query_expression_metadata_request_type_instance.to_dict()
# create an instance of QueryExpressionMetadataRequestType from a dict
query_expression_metadata_request_type_form_dict = query_expression_metadata_request_type.from_dict(query_expression_metadata_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


