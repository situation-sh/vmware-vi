# DvsGreEncapNetworkRuleAction

This class defines network rule action to GRE Encapsulate a packet.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encapsulation_ip** | [**SingleIp**](SingleIp.md) |  | 

## Example

```python
from vmware_vi.models.dvs_gre_encap_network_rule_action import DvsGreEncapNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsGreEncapNetworkRuleAction from a JSON string
dvs_gre_encap_network_rule_action_instance = DvsGreEncapNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsGreEncapNetworkRuleAction.to_json()

# convert the object into a dict
dvs_gre_encap_network_rule_action_dict = dvs_gre_encap_network_rule_action_instance.to_dict()
# create an instance of DvsGreEncapNetworkRuleAction from a dict
dvs_gre_encap_network_rule_action_form_dict = dvs_gre_encap_network_rule_action.from_dict(dvs_gre_encap_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


