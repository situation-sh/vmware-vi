# DvsTrafficFilterConfig

This class defines Traffic Filter configuration.  ** Supported Qualifier and Actions ** <table border=\"1\"width=\"100%\"> <tr> <th>Traffic Filter Config</th> <th>Supported classes</th> </tr> <tr> <td>Qualifiers supported</td> <td>*SingleIp*, *IpRange*, *SingleMac*, *MacRange*, *DvsSingleIpPort*, *DvsSystemTrafficNetworkRuleQualifier* </td> </tr> <tr> <td>Actions Supported</td> <td>*DvsDropNetworkRuleAction*, *DvsAcceptNetworkRuleAction*, *DvsPuntNetworkRuleAction*, *DvsCopyNetworkRuleAction*, *DvsMacRewriteNetworkRuleAction*, *DvsGreEncapNetworkRuleAction*, *DvsLogNetworkRuleAction*, *DvsUpdateTagNetworkRuleAction*, *DvsRateLimitNetworkRuleAction* </td> </tr>  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_ruleset** | [**DvsTrafficRuleset**](DvsTrafficRuleset.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_traffic_filter_config import DvsTrafficFilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DvsTrafficFilterConfig from a JSON string
dvs_traffic_filter_config_instance = DvsTrafficFilterConfig.from_json(json)
# print the JSON string representation of the object
print DvsTrafficFilterConfig.to_json()

# convert the object into a dict
dvs_traffic_filter_config_dict = dvs_traffic_filter_config_instance.to_dict()
# create an instance of DvsTrafficFilterConfig from a dict
dvs_traffic_filter_config_form_dict = dvs_traffic_filter_config.from_dict(dvs_traffic_filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


