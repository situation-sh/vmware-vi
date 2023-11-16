# UpdateRulesetRequestType

The parameters of *HostFirewallSystem.UpdateRuleset*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**spec** | [**HostFirewallRulesetRulesetSpec**](HostFirewallRulesetRulesetSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_ruleset_request_type import UpdateRulesetRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesetRequestType from a JSON string
update_ruleset_request_type_instance = UpdateRulesetRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateRulesetRequestType.to_json()

# convert the object into a dict
update_ruleset_request_type_dict = update_ruleset_request_type_instance.to_dict()
# create an instance of UpdateRulesetRequestType from a dict
update_ruleset_request_type_form_dict = update_ruleset_request_type.from_dict(update_ruleset_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


