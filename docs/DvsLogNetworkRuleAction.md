# DvsLogNetworkRuleAction

This class defines network rule action to just log the rule.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_log_network_rule_action import DvsLogNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsLogNetworkRuleAction from a JSON string
dvs_log_network_rule_action_instance = DvsLogNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsLogNetworkRuleAction.to_json()

# convert the object into a dict
dvs_log_network_rule_action_dict = dvs_log_network_rule_action_instance.to_dict()
# create an instance of DvsLogNetworkRuleAction from a dict
dvs_log_network_rule_action_form_dict = dvs_log_network_rule_action.from_dict(dvs_log_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


