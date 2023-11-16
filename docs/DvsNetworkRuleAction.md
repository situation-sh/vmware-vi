# DvsNetworkRuleAction

This class is the base class for network rule action.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_network_rule_action import DvsNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsNetworkRuleAction from a JSON string
dvs_network_rule_action_instance = DvsNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsNetworkRuleAction.to_json()

# convert the object into a dict
dvs_network_rule_action_dict = dvs_network_rule_action_instance.to_dict()
# create an instance of DvsNetworkRuleAction from a dict
dvs_network_rule_action_form_dict = dvs_network_rule_action.from_dict(dvs_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


