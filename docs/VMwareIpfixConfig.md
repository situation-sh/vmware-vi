# VMwareIpfixConfig

Configuration for IPFIX monitoring of distributed virtual switch traffic.  IPFIX monitoring must be enabled to use this capability. See *VMwareDVSPortSetting*.*VMwareDVSPortSetting.ipfixEnabled*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collector_ip_address** | **str** | IP address for the ipfix collector, using IPv4 or IPv6.  IPv6 is supported in vSphere Distributed Switch Version 6.0 or later. This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch.  ***Since:*** vSphere API 5.0  | [optional] 
**collector_port** | **int** | Port for the ipfix collector.  This must be set before ipfix monitoring can be enabled for the switch, or for any portgroup or port of the switch. Legal value range is 0-65535.  ***Since:*** vSphere API 5.0  | [optional] 
**observation_domain_id** | **int** | Observation Domain Id for the ipfix collector.  Observation Domain Id is supported in vSphere Distributed Switch Version 6.0 or later. Legal value range is 0-((2^32)-1)  ***Since:*** vSphere API 6.0  | [optional] 
**active_flow_timeout** | **int** | The number of seconds after which \&quot;active\&quot; flows are forced to be exported to the collector.  Legal value range is 60-3600. Default: 60.  ***Since:*** vSphere API 5.0  | 
**idle_flow_timeout** | **int** | The number of seconds after which \&quot;idle\&quot; flows are forced to be exported to the collector.  Legal value range is 10-600. Default: 15.  ***Since:*** vSphere API 5.0  | 
**sampling_rate** | **int** | The ratio of total number of packets to the number of packets analyzed.  Set to 0 to disable sampling. Legal value range is 0-16384. Default: 4096.  ***Since:*** vSphere API 5.0  | 
**internal_flows_only** | **bool** | Whether to limit analysis to traffic that has both source and destination served by the same host.  Default: false.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.v_mware_ipfix_config import VMwareIpfixConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareIpfixConfig from a JSON string
v_mware_ipfix_config_instance = VMwareIpfixConfig.from_json(json)
# print the JSON string representation of the object
print VMwareIpfixConfig.to_json()

# convert the object into a dict
v_mware_ipfix_config_dict = v_mware_ipfix_config_instance.to_dict()
# create an instance of VMwareIpfixConfig from a dict
v_mware_ipfix_config_form_dict = v_mware_ipfix_config.from_dict(v_mware_ipfix_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


