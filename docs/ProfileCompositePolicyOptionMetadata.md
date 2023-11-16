# ProfileCompositePolicyOptionMetadata

The *ProfileCompositePolicyOptionMetadata* data object represents the metadata information for a composite *PolicyOption*.  The user will retrieve metadata information about a composite policy and then combine policy options to produce the composite policy option.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **List[str]** | List of optional policy option identifiers that could be combined in this composite policy option.  The policy options should already be part of the possible policy options for the policy. See the *ProfilePolicyMetadata*.*ProfilePolicyMetadata.possibleOption* list.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_composite_policy_option_metadata import ProfileCompositePolicyOptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileCompositePolicyOptionMetadata from a JSON string
profile_composite_policy_option_metadata_instance = ProfileCompositePolicyOptionMetadata.from_json(json)
# print the JSON string representation of the object
print ProfileCompositePolicyOptionMetadata.to_json()

# convert the object into a dict
profile_composite_policy_option_metadata_dict = profile_composite_policy_option_metadata_instance.to_dict()
# create an instance of ProfileCompositePolicyOptionMetadata from a dict
profile_composite_policy_option_metadata_form_dict = profile_composite_policy_option_metadata.from_dict(profile_composite_policy_option_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


