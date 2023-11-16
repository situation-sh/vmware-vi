# DvsMacNetworkRuleQualifier

This class defines the MAC Rule Qualifier.  Here MAC addresses of source and destination will be used for classifying packets.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_address** | [**MacAddress**](MacAddress.md) |  | [optional] 
**destination_address** | [**MacAddress**](MacAddress.md) |  | [optional] 
**protocol** | [**IntExpression**](IntExpression.md) |  | [optional] 
**vlan_id** | [**IntExpression**](IntExpression.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_mac_network_rule_qualifier import DvsMacNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of DvsMacNetworkRuleQualifier from a JSON string
dvs_mac_network_rule_qualifier_instance = DvsMacNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print DvsMacNetworkRuleQualifier.to_json()

# convert the object into a dict
dvs_mac_network_rule_qualifier_dict = dvs_mac_network_rule_qualifier_instance.to_dict()
# create an instance of DvsMacNetworkRuleQualifier from a dict
dvs_mac_network_rule_qualifier_form_dict = dvs_mac_network_rule_qualifier.from_dict(dvs_mac_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


