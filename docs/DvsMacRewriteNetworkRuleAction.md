# DvsMacRewriteNetworkRuleAction

This class defines network rule action to MAC Rewrite.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rewrite_mac** | **str** | Rewrite Destination MAC with this MAC address.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.dvs_mac_rewrite_network_rule_action import DvsMacRewriteNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsMacRewriteNetworkRuleAction from a JSON string
dvs_mac_rewrite_network_rule_action_instance = DvsMacRewriteNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsMacRewriteNetworkRuleAction.to_json()

# convert the object into a dict
dvs_mac_rewrite_network_rule_action_dict = dvs_mac_rewrite_network_rule_action_instance.to_dict()
# create an instance of DvsMacRewriteNetworkRuleAction from a dict
dvs_mac_rewrite_network_rule_action_form_dict = dvs_mac_rewrite_network_rule_action.from_dict(dvs_mac_rewrite_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


