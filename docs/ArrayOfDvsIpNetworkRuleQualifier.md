# ArrayOfDvsIpNetworkRuleQualifier

A boxed array of *DvsIpNetworkRuleQualifier*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsIpNetworkRuleQualifier]**](DvsIpNetworkRuleQualifier.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_ip_network_rule_qualifier import ArrayOfDvsIpNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsIpNetworkRuleQualifier from a JSON string
array_of_dvs_ip_network_rule_qualifier_instance = ArrayOfDvsIpNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsIpNetworkRuleQualifier.to_json()

# convert the object into a dict
array_of_dvs_ip_network_rule_qualifier_dict = array_of_dvs_ip_network_rule_qualifier_instance.to_dict()
# create an instance of ArrayOfDvsIpNetworkRuleQualifier from a dict
array_of_dvs_ip_network_rule_qualifier_form_dict = array_of_dvs_ip_network_rule_qualifier.from_dict(array_of_dvs_ip_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


