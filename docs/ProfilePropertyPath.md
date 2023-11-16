# ProfilePropertyPath

The *ProfilePropertyPath* data object represents the path to a profile, policy option, or specific parameter.  If <code>profilePath</code>, <code>policyId</code>, and <code>parameterId</code> are all specified, the combination of the three identifies a particular parameter. If only <code>profilePath</code> and <code>policyId</code> are specified, the combination identifies a specific profile policy option. If just the <code>profilePath</code> is specified, the data object identifies a profile instance.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_path** | **str** | Complete path to the leaf profile, relative to the root of the host profile document.  ***Since:*** vSphere API 4.0  | 
**policy_id** | **str** | Policy identifier.  ***Since:*** vSphere API 4.0  | [optional] 
**parameter_id** | **str** | Key for a parameter in the policy specified by &lt;code&gt;policyId&lt;/code&gt;.  See *PolicyOption*.*PolicyOption.parameter* and *KeyAnyValue.key*.  ***Since:*** vSphere API 5.1  | [optional] 
**policy_option_id** | **str** | Policy option identifier.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.profile_property_path import ProfilePropertyPath

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePropertyPath from a JSON string
profile_property_path_instance = ProfilePropertyPath.from_json(json)
# print the JSON string representation of the object
print ProfilePropertyPath.to_json()

# convert the object into a dict
profile_property_path_dict = profile_property_path_instance.to_dict()
# create an instance of ProfilePropertyPath from a dict
profile_property_path_form_dict = profile_property_path.from_dict(profile_property_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


