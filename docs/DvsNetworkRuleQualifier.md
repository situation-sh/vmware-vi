# DvsNetworkRuleQualifier

This class is the base class for identifying network traffic.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the Qualifier  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_network_rule_qualifier import DvsNetworkRuleQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of DvsNetworkRuleQualifier from a JSON string
dvs_network_rule_qualifier_instance = DvsNetworkRuleQualifier.from_json(json)
# print the JSON string representation of the object
print DvsNetworkRuleQualifier.to_json()

# convert the object into a dict
dvs_network_rule_qualifier_dict = dvs_network_rule_qualifier_instance.to_dict()
# create an instance of DvsNetworkRuleQualifier from a dict
dvs_network_rule_qualifier_form_dict = dvs_network_rule_qualifier.from_dict(dvs_network_rule_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


