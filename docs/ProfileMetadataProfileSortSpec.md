# ProfileMetadataProfileSortSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy used to sort instances of the profile  ***Since:*** vSphere API 5.0  | 
**parameter** | **str** | The parameter to be used for sorting.  Note that if the policy to be used for sorting has multiple possible policy options, all possible policy options defined for that policy type must have this parameter.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.profile_metadata_profile_sort_spec import ProfileMetadataProfileSortSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetadataProfileSortSpec from a JSON string
profile_metadata_profile_sort_spec_instance = ProfileMetadataProfileSortSpec.from_json(json)
# print the JSON string representation of the object
print ProfileMetadataProfileSortSpec.to_json()

# convert the object into a dict
profile_metadata_profile_sort_spec_dict = profile_metadata_profile_sort_spec_instance.to_dict()
# create an instance of ProfileMetadataProfileSortSpec from a dict
profile_metadata_profile_sort_spec_form_dict = profile_metadata_profile_sort_spec.from_dict(profile_metadata_profile_sort_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


