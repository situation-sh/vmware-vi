# ApplyProfile

The *ApplyProfile* data object is the base class for all data objects that define profile configuration data.  <code>ApplyProfile</code> defines ESX configuration data storage and it supports recursive profile definition for the profile plug-in architecture.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether the profile is enabled.  ***Since:*** vSphere API 4.0  | 
**policy** | [**List[ProfilePolicy]**](ProfilePolicy.md) | The list of policies comprising the profile.  A *ProfilePolicy* stores one or more configuration data values in a *PolicyOption*. The policy option is one of the configuration options from the *ProfilePolicyMetadata*.*ProfilePolicyMetadata.possibleOption* list.  ***Since:*** vSphere API 4.0  | [optional] 
**profile_type_name** | **str** | Identifies the profile type.  ***Since:*** vSphere API 5.0  | [optional] 
**profile_version** | **str** | Profile engine version.  ***Since:*** vSphere API 5.0  | [optional] 
**var_property** | [**List[ProfileApplyProfileProperty]**](ProfileApplyProfileProperty.md) | List of subprofiles for this profile.  This list can change depending on which profile plug-ins are available in the system. Subprofiles can be nested to arbitrary depths to represent host capabilities.  ***Since:*** vSphere API 5.0  | [optional] 
**favorite** | **bool** | Indicates whether this profile is marked as \&quot;favorite\&quot;.  ***Since:*** vSphere API 6.5  | [optional] 
**to_be_merged** | **bool** | Indicates whether this profile is marked as to-be-merged.  ***Since:*** vSphere API 6.5  | [optional] 
**to_replace_with** | **bool** | Indicates whether the selected array elements, with the current as one of them, replace the profile array in the target host profile.  ***Since:*** vSphere API 6.5  | [optional] 
**to_be_deleted** | **bool** | Indicates whether this profile is marked as to-be-deleted.  ***Since:*** vSphere API 6.5  | [optional] 
**copy_enable_status** | **bool** | Indicates that the member variable &lt;code&gt;enabled&lt;/code&gt; of this profile will be copied from source profile to target profiles at host profile composition.  ***Since:*** vSphere API 6.5  | [optional] 
**hidden** | **bool** | Indicates whether this profile will be displayed or not.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.apply_profile import ApplyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyProfile from a JSON string
apply_profile_instance = ApplyProfile.from_json(json)
# print the JSON string representation of the object
print ApplyProfile.to_json()

# convert the object into a dict
apply_profile_dict = apply_profile_instance.to_dict()
# create an instance of ApplyProfile from a dict
apply_profile_form_dict = apply_profile.from_dict(apply_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


