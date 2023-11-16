# EnableRulesetRequestType

The parameters of *HostFirewallSystem.EnableRuleset*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from vmware_vi.models.enable_ruleset_request_type import EnableRulesetRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableRulesetRequestType from a JSON string
enable_ruleset_request_type_instance = EnableRulesetRequestType.from_json(json)
# print the JSON string representation of the object
print EnableRulesetRequestType.to_json()

# convert the object into a dict
enable_ruleset_request_type_dict = enable_ruleset_request_type_instance.to_dict()
# create an instance of EnableRulesetRequestType from a dict
enable_ruleset_request_type_form_dict = enable_ruleset_request_type.from_dict(enable_ruleset_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


