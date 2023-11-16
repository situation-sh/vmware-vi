# ArrayOfHostNetworkTrafficShapingPolicy

A boxed array of *HostNetworkTrafficShapingPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkTrafficShapingPolicy]**](HostNetworkTrafficShapingPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_traffic_shaping_policy import ArrayOfHostNetworkTrafficShapingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkTrafficShapingPolicy from a JSON string
array_of_host_network_traffic_shaping_policy_instance = ArrayOfHostNetworkTrafficShapingPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkTrafficShapingPolicy.to_json()

# convert the object into a dict
array_of_host_network_traffic_shaping_policy_dict = array_of_host_network_traffic_shaping_policy_instance.to_dict()
# create an instance of ArrayOfHostNetworkTrafficShapingPolicy from a dict
array_of_host_network_traffic_shaping_policy_form_dict = array_of_host_network_traffic_shaping_policy.from_dict(array_of_host_network_traffic_shaping_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


