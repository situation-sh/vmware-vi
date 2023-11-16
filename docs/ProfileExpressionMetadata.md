# ProfileExpressionMetadata

DataObject to represent the metadata associated with a SimpleExpression.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_id** | [**ExtendedElementDescription**](ExtendedElementDescription.md) |  | 
**parameter** | [**List[ProfileParameterMetadata]**](ProfileParameterMetadata.md) | Parameters that can be specified for this SimpleExpression  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_expression_metadata import ProfileExpressionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileExpressionMetadata from a JSON string
profile_expression_metadata_instance = ProfileExpressionMetadata.from_json(json)
# print the JSON string representation of the object
print ProfileExpressionMetadata.to_json()

# convert the object into a dict
profile_expression_metadata_dict = profile_expression_metadata_instance.to_dict()
# create an instance of ProfileExpressionMetadata from a dict
profile_expression_metadata_form_dict = profile_expression_metadata.from_dict(profile_expression_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


