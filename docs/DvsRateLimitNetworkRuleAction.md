# DvsRateLimitNetworkRuleAction

This class defines network rule action to ratelimit packets.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packets_per_second** | **int** | Rate limit value specified in packets per second.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.dvs_rate_limit_network_rule_action import DvsRateLimitNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsRateLimitNetworkRuleAction from a JSON string
dvs_rate_limit_network_rule_action_instance = DvsRateLimitNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsRateLimitNetworkRuleAction.to_json()

# convert the object into a dict
dvs_rate_limit_network_rule_action_dict = dvs_rate_limit_network_rule_action_instance.to_dict()
# create an instance of DvsRateLimitNetworkRuleAction from a dict
dvs_rate_limit_network_rule_action_form_dict = dvs_rate_limit_network_rule_action.from_dict(dvs_rate_limit_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


