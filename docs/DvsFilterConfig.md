# DvsFilterConfig

This class defines Network Filter configuration.  ** Supported Qualifier and Actions ** <table border=\"1\"width=\"100%\"> <tr> <th>Network Filter Config</th> <th>Supported classes</th> </tr> <tr> <td>Qualifiers supported</td> <td>*SingleIp*, *IpRange*, *SingleMac*, *MacRange*, *DvsSingleIpPort*, *DvsSystemTrafficNetworkRuleQualifier* </td> </tr> <tr> <td>Actions Supported</td> <td>*DvsDropNetworkRuleAction*, *DvsAcceptNetworkRuleAction*, *DvsPuntNetworkRuleAction*, *DvsCopyNetworkRuleAction*, *DvsMacRewriteNetworkRuleAction*, *DvsGreEncapNetworkRuleAction*, *DvsLogNetworkRuleAction*, *DvsUpdateTagNetworkRuleAction*, *DvsRateLimitNetworkRuleAction* </td> </tr>  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of Network Filter Config.  ***Since:*** vSphere API 5.5  | [optional] 
**agent_name** | **str** | The name of the network traffic filter agent.  ***Since:*** vSphere API 5.5  | [optional] 
**slot_number** | **str** | The slot number of the network filter agent.  ***Since:*** vSphere API 5.5  | [optional] 
**parameters** | [**DvsFilterParameter**](DvsFilterParameter.md) |  | [optional] 
**on_failure** | **str** | This property specifies whether to allow all traffic or to deny all traffic when a Network Filter fails to configure.  Please see *DvsFilterOnFailure_enum* for more details.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_filter_config import DvsFilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DvsFilterConfig from a JSON string
dvs_filter_config_instance = DvsFilterConfig.from_json(json)
# print the JSON string representation of the object
print DvsFilterConfig.to_json()

# convert the object into a dict
dvs_filter_config_dict = dvs_filter_config_instance.to_dict()
# create an instance of DvsFilterConfig from a dict
dvs_filter_config_form_dict = dvs_filter_config.from_dict(dvs_filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


