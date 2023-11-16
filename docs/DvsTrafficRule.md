# DvsTrafficRule

This class defines a single rule that will be applied to network traffic.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the rule  ***Since:*** vSphere API 5.5  | [optional] 
**description** | **str** | Description of the rule  ***Since:*** vSphere API 5.5  | [optional] 
**sequence** | **int** | Sequence of this rule.  i.e, the order in which this rule appears in the ruleset.  ***Since:*** vSphere API 5.5  | [optional] 
**qualifier** | [**List[DvsNetworkRuleQualifier]**](DvsNetworkRuleQualifier.md) | List of Network rule qualifiers.  &#39;AND&#39; of this array of network rule qualifiers is applied as one network traffic rule. If the TrafficRule belongs to *DvsFilterPolicy* : There can be a maximum of 1 *DvsIpNetworkRuleQualifier*, 1 *DvsMacNetworkRuleQualifier* and 1 *DvsSystemTrafficNetworkRuleQualifier* for a total of 3 *DvsTrafficRule.qualifier*  ***Since:*** vSphere API 5.5  | [optional] 
**action** | [**DvsNetworkRuleAction**](DvsNetworkRuleAction.md) |  | [optional] 
**direction** | **str** | Whether this rule needs to be applied to incoming packets, to outgoing packets or both.  See *DvsNetworkRuleDirectionType_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_traffic_rule import DvsTrafficRule

# TODO update the JSON string below
json = "{}"
# create an instance of DvsTrafficRule from a JSON string
dvs_traffic_rule_instance = DvsTrafficRule.from_json(json)
# print the JSON string representation of the object
print DvsTrafficRule.to_json()

# convert the object into a dict
dvs_traffic_rule_dict = dvs_traffic_rule_instance.to_dict()
# create an instance of DvsTrafficRule from a dict
dvs_traffic_rule_form_dict = dvs_traffic_rule.from_dict(dvs_traffic_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


