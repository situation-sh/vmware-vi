# ArrayOfDvsNetworkRuleAction

A boxed array of *DvsNetworkRuleAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsNetworkRuleAction]**](DvsNetworkRuleAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_network_rule_action import ArrayOfDvsNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsNetworkRuleAction from a JSON string
array_of_dvs_network_rule_action_instance = ArrayOfDvsNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsNetworkRuleAction.to_json()

# convert the object into a dict
array_of_dvs_network_rule_action_dict = array_of_dvs_network_rule_action_instance.to_dict()
# create an instance of ArrayOfDvsNetworkRuleAction from a dict
array_of_dvs_network_rule_action_form_dict = array_of_dvs_network_rule_action.from_dict(array_of_dvs_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


