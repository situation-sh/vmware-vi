# ArrayOfProfileMetadata

A boxed array of *ProfileMetadata*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileMetadata]**](ProfileMetadata.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_metadata import ArrayOfProfileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileMetadata from a JSON string
array_of_profile_metadata_instance = ArrayOfProfileMetadata.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileMetadata.to_json()

# convert the object into a dict
array_of_profile_metadata_dict = array_of_profile_metadata_instance.to_dict()
# create an instance of ArrayOfProfileMetadata from a dict
array_of_profile_metadata_form_dict = array_of_profile_metadata.from_dict(array_of_profile_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

