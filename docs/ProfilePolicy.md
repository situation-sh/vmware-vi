# ProfilePolicy

The *ProfilePolicy* data object represents a policy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the policy.  ***Since:*** vSphere API 4.0  | 
**policy_option** | [**PolicyOption**](PolicyOption.md) |  | 

## Example

```python
from vmware_vi.models.profile_policy import ProfilePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePolicy from a JSON string
profile_policy_instance = ProfilePolicy.from_json(json)
# print the JSON string representation of the object
print ProfilePolicy.to_json()

# convert the object into a dict
profile_policy_dict = profile_policy_instance.to_dict()
# create an instance of ProfilePolicy from a dict
profile_policy_form_dict = profile_policy.from_dict(profile_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


