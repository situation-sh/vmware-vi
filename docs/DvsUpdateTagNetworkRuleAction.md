# DvsUpdateTagNetworkRuleAction

This class defines network rule action to tag packets(qos,dscp) or clear tags(clear qos, dscp tags) on packets.  One or both of qos and dscp may be specified.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_tag** | **int** | QOS tag.  IEEE 802.1p supports 3 bit Priority Code Point (PCP). The valid values are between 0-7. Please refer the IEEE 802.1p documentation for more details about what each value represents. If qosTag is set to 0 then the tag on the packets will be cleared.  ***Since:*** vSphere API 5.5  | [optional] 
**dscp_tag** | **int** | DSCP tag.  The valid values for DSCP tag can be found in &#39;Differentiated Services Field Codepoints&#39; section of IANA website. The information can also be got from reading all of the below RFC: RFC 2474, RFC 2597, RFC 3246, RFC 5865. If the dscpTag is set to 0 then the dscp tag on packets will be cleared.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_update_tag_network_rule_action import DvsUpdateTagNetworkRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of DvsUpdateTagNetworkRuleAction from a JSON string
dvs_update_tag_network_rule_action_instance = DvsUpdateTagNetworkRuleAction.from_json(json)
# print the JSON string representation of the object
print DvsUpdateTagNetworkRuleAction.to_json()

# convert the object into a dict
dvs_update_tag_network_rule_action_dict = dvs_update_tag_network_rule_action_instance.to_dict()
# create an instance of DvsUpdateTagNetworkRuleAction from a dict
dvs_update_tag_network_rule_action_form_dict = dvs_update_tag_network_rule_action.from_dict(dvs_update_tag_network_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


