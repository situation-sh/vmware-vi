# HostNetworkTrafficShapingPolicy

This data object type describes traffic shaping policy. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The flag to indicate whether or not traffic shaper is enabled on the port.  | [optional] 
**average_bandwidth** | **int** | The average bandwidth in bits per second if shaping is enabled on the port.  | [optional] 
**peak_bandwidth** | **int** | The peak bandwidth during bursts in bits per second if traffic shaping is enabled on the port.  | [optional] 
**burst_size** | **int** | The maximum burst size allowed in bytes if shaping is enabled on the port.  | [optional] 

## Example

```python
from vmware_vi.models.host_network_traffic_shaping_policy import HostNetworkTrafficShapingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkTrafficShapingPolicy from a JSON string
host_network_traffic_shaping_policy_instance = HostNetworkTrafficShapingPolicy.from_json(json)
# print the JSON string representation of the object
print HostNetworkTrafficShapingPolicy.to_json()

# convert the object into a dict
host_network_traffic_shaping_policy_dict = host_network_traffic_shaping_policy_instance.to_dict()
# create an instance of HostNetworkTrafficShapingPolicy from a dict
host_network_traffic_shaping_policy_form_dict = host_network_traffic_shaping_policy.from_dict(host_network_traffic_shaping_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


