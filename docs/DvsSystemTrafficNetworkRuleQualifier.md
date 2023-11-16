# DvsSystemTrafficNetworkRuleQualifier

This class defines the System Traffic Qualifier.  Here the type of traffic will be used for classifying packets.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_of_system_traffic** | [**StringExpression**](StringExpression.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_system_traffic_network_rule_qualifier import DvsSystemTrafficNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of DvsSystemTrafficNetworkRuleQualifier from a JSON string
dvs_system_traffic_network_rule_qualifier_instance = DvsSystemTrafficNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print DvsSystemTrafficNetworkRuleQualifier.to_json()

# convert the object into a dict
dvs_system_traffic_network_rule_qualifier_dict = dvs_system_traffic_network_rule_qualifier_instance.to_dict()
# create an instance of DvsSystemTrafficNetworkRuleQualifier from a dict
dvs_system_traffic_network_rule_qualifier_form_dict = dvs_system_traffic_network_rule_qualifier.from_dict(dvs_system_traffic_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


