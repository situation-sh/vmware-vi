# ProfileParameterMetadataParameterRelationMetadata

This class to define a relation between the parameter and a profile or a parameter, or a constant list of values.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation_types** | **List[str]** | The types of this relation.  ***Since:*** vSphere API 6.7  | [optional] 
**values** | [**List[Any]**](Any.md) | The valid value list.  ***Since:*** vSphere API 6.7  | [optional] 
**path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | [optional] 
**min_count** | **int** | The minimal count of values to map to.  ***Since:*** vSphere API 6.7  | 
**max_count** | **int** | The maximum count of values to map to.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.profile_parameter_metadata_parameter_relation_metadata import ProfileParameterMetadataParameterRelationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileParameterMetadataParameterRelationMetadata from a JSON string
profile_parameter_metadata_parameter_relation_metadata_instance = ProfileParameterMetadataParameterRelationMetadata.from_json(json)
# print the JSON string representation of the object
print ProfileParameterMetadataParameterRelationMetadata.to_json()

# convert the object into a dict
profile_parameter_metadata_parameter_relation_metadata_dict = profile_parameter_metadata_parameter_relation_metadata_instance.to_dict()
# create an instance of ProfileParameterMetadataParameterRelationMetadata from a dict
profile_parameter_metadata_parameter_relation_metadata_form_dict = profile_parameter_metadata_parameter_relation_metadata.from_dict(profile_parameter_metadata_parameter_relation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


