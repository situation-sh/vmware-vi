# ProfilePolicyMetadata

The *ProfilePolicyMetadata* data object represents the metadata information for a *ProfilePolicy*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedElementDescription**](ExtendedElementDescription.md) |  | 
**possible_option** | [**List[ProfilePolicyOptionMetadata]**](ProfilePolicyOptionMetadata.md) | Possible policy options that can be set for a policy of the given kind.  *HostProfile*s and subprofiles will contain selected policy options from this list. See *PolicyOption*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_policy_metadata import ProfilePolicyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePolicyMetadata from a JSON string
profile_policy_metadata_instance = ProfilePolicyMetadata.from_json(json)
# print the JSON string representation of the object
print ProfilePolicyMetadata.to_json()

# convert the object into a dict
profile_policy_metadata_dict = profile_policy_metadata_instance.to_dict()
# create an instance of ProfilePolicyMetadata from a dict
profile_policy_metadata_form_dict = profile_policy_metadata.from_dict(profile_policy_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


