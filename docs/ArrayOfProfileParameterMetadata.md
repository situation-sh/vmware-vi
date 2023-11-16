# ArrayOfProfileParameterMetadata

A boxed array of *ProfileParameterMetadata*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileParameterMetadata]**](ProfileParameterMetadata.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_parameter_metadata import ArrayOfProfileParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileParameterMetadata from a JSON string
array_of_profile_parameter_metadata_instance = ArrayOfProfileParameterMetadata.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileParameterMetadata.to_json()

# convert the object into a dict
array_of_profile_parameter_metadata_dict = array_of_profile_parameter_metadata_instance.to_dict()
# create an instance of ArrayOfProfileParameterMetadata from a dict
array_of_profile_parameter_metadata_form_dict = array_of_profile_parameter_metadata.from_dict(array_of_profile_parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


