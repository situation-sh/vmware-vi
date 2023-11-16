# DvsPuntNetworkRuleAction

This class defines network rule action to punt.  i.e, forward packets to an associated slow-path service Virtual Machine.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_punt_network_rule_action import DvsPuntNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPuntNetworkRuleAction from a JSON string
dvs_punt_network_rule_action_instance = DvsPuntNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsPuntNetworkRuleAction.to_json()

# convert the object into a dict
dvs_punt_network_rule_action_dict = dvs_punt_network_rule_action_instance.to_dict()
# create an instance of DvsPuntNetworkRuleAction from a dict
dvs_punt_network_rule_action_form_dict = dvs_punt_network_rule_action.from_dict(dvs_punt_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


