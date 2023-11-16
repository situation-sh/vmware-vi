# DisableRulesetRequestType

The parameters of *HostFirewallSystem.DisableRuleset*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from vmware_vi.models.disable_ruleset_request_type import DisableRulesetRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisableRulesetRequestType from a JSON string
disable_ruleset_request_type_instance = DisableRulesetRequestType.from_json(json)
# print the JSON string representation of the object
print DisableRulesetRequestType.to_json()

# convert the object into a dict
disable_ruleset_request_type_dict = disable_ruleset_request_type_instance.to_dict()
# create an instance of DisableRulesetRequestType from a dict
disable_ruleset_request_type_form_dict = disable_ruleset_request_type.from_dict(disable_ruleset_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


