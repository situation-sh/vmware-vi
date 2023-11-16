# ArrayOfProfileExpressionMetadata

A boxed array of *ProfileExpressionMetadata*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileExpressionMetadata]**](ProfileExpressionMetadata.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_expression_metadata import ArrayOfProfileExpressionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileExpressionMetadata from a JSON string
array_of_profile_expression_metadata_instance = ArrayOfProfileExpressionMetadata.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileExpressionMetadata.to_json()

# convert the object into a dict
array_of_profile_expression_metadata_dict = array_of_profile_expression_metadata_instance.to_dict()
# create an instance of ArrayOfProfileExpressionMetadata from a dict
array_of_profile_expression_metadata_form_dict = array_of_profile_expression_metadata.from_dict(array_of_profile_expression_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


