# ProfilePolicyOptionMetadata

The *ProfilePolicyOptionMetadata* data object contains the metadata information for a *PolicyOption*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedElementDescription**](ExtendedElementDescription.md) |  | 
**parameter** | [**List[ProfileParameterMetadata]**](ProfileParameterMetadata.md) | Metadata about the parameters for the policy option.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_policy_option_metadata import ProfilePolicyOptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePolicyOptionMetadata from a JSON string
profile_policy_option_metadata_instance = ProfilePolicyOptionMetadata.from_json(json)
# print the JSON string representation of the object
print ProfilePolicyOptionMetadata.to_json()

# convert the object into a dict
profile_policy_option_metadata_dict = profile_policy_option_metadata_instance.to_dict()
# create an instance of ProfilePolicyOptionMetadata from a dict
profile_policy_option_metadata_form_dict = profile_policy_option_metadata.from_dict(profile_policy_option_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


