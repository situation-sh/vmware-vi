# ArrayOfProfileCompositePolicyOptionMetadata

A boxed array of *ProfileCompositePolicyOptionMetadata*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileCompositePolicyOptionMetadata]**](ProfileCompositePolicyOptionMetadata.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_composite_policy_option_metadata import ArrayOfProfileCompositePolicyOptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileCompositePolicyOptionMetadata from a JSON string
array_of_profile_composite_policy_option_metadata_instance = ArrayOfProfileCompositePolicyOptionMetadata.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileCompositePolicyOptionMetadata.to_json()

# convert the object into a dict
array_of_profile_composite_policy_option_metadata_dict = array_of_profile_composite_policy_option_metadata_instance.to_dict()
# create an instance of ArrayOfProfileCompositePolicyOptionMetadata from a dict
array_of_profile_composite_policy_option_metadata_form_dict = array_of_profile_composite_policy_option_metadata.from_dict(array_of_profile_composite_policy_option_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


