# ArrayOfDvsNetworkRuleQualifier

A boxed array of *DvsNetworkRuleQualifier*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsNetworkRuleQualifier]**](DvsNetworkRuleQualifier.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_network_rule_qualifier import ArrayOfDvsNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsNetworkRuleQualifier from a JSON string
array_of_dvs_network_rule_qualifier_instance = ArrayOfDvsNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsNetworkRuleQualifier.to_json()

# convert the object into a dict
array_of_dvs_network_rule_qualifier_dict = array_of_dvs_network_rule_qualifier_instance.to_dict()
# create an instance of ArrayOfDvsNetworkRuleQualifier from a dict
array_of_dvs_network_rule_qualifier_form_dict = array_of_dvs_network_rule_qualifier.from_dict(array_of_dvs_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


