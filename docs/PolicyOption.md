# PolicyOption

The *PolicyOption* data object represents one or more configuration values.  A policy option is one of the configuration options from the *ProfilePolicyMetadata*.*ProfilePolicyMetadata.possibleOption* list.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the policy option.  This value matches one of the keys from the list of possible options in the policy metadata (*ProfilePolicyMetadata*.*ProfilePolicyMetadata.possibleOption*\\[\\].*ProfilePolicyOptionMetadata.id*.*ElementDescription.key*).  ***Since:*** vSphere API 4.0  | 
**parameter** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Parameters for the policy option.  This list must include all parameters that are not marked as optional in the policy option metadata parameter list (*ProfilePolicyMetadata*.*ProfilePolicyMetadata.possibleOption*\\[\\].*ProfilePolicyOptionMetadata.parameter*\\[\\].*ProfileParameterMetadata.optional*).  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.policy_option import PolicyOption

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyOption from a JSON string
policy_option_instance = PolicyOption.from_json(json)
# print the JSON string representation of the object
print PolicyOption.to_json()

# convert the object into a dict
policy_option_dict = policy_option_instance.to_dict()
# create an instance of PolicyOption from a dict
policy_option_form_dict = policy_option.from_dict(policy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


