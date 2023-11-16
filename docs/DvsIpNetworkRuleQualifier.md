# DvsIpNetworkRuleQualifier

This class defines the IP Rule Qualifier.  Here IP addresses of source and destination will be used for classifying packets.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_address** | [**IpAddress**](IpAddress.md) |  | [optional] 
**destination_address** | [**IpAddress**](IpAddress.md) |  | [optional] 
**protocol** | [**IntExpression**](IntExpression.md) |  | [optional] 
**source_ip_port** | [**DvsIpPort**](DvsIpPort.md) |  | [optional] 
**destination_ip_port** | [**DvsIpPort**](DvsIpPort.md) |  | [optional] 
**tcp_flags** | [**IntExpression**](IntExpression.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_ip_network_rule_qualifier import DvsIpNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of DvsIpNetworkRuleQualifier from a JSON string
dvs_ip_network_rule_qualifier_instance = DvsIpNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print DvsIpNetworkRuleQualifier.to_json()

# convert the object into a dict
dvs_ip_network_rule_qualifier_dict = dvs_ip_network_rule_qualifier_instance.to_dict()
# create an instance of DvsIpNetworkRuleQualifier from a dict
dvs_ip_network_rule_qualifier_form_dict = dvs_ip_network_rule_qualifier.from_dict(dvs_ip_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


