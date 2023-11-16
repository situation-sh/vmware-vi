# DVSTrafficShapingPolicy

This data object type describes traffic shaping policy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**average_bandwidth** | [**LongPolicy**](LongPolicy.md) |  | [optional] 
**peak_bandwidth** | [**LongPolicy**](LongPolicy.md) |  | [optional] 
**burst_size** | [**LongPolicy**](LongPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_traffic_shaping_policy import DVSTrafficShapingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSTrafficShapingPolicy from a JSON string
dvs_traffic_shaping_policy_instance = DVSTrafficShapingPolicy.from_json(json)
# print the JSON string representation of the object
print DVSTrafficShapingPolicy.to_json()

# convert the object into a dict
dvs_traffic_shaping_policy_dict = dvs_traffic_shaping_policy_instance.to_dict()
# create an instance of DVSTrafficShapingPolicy from a dict
dvs_traffic_shaping_policy_form_dict = dvs_traffic_shaping_policy.from_dict(dvs_traffic_shaping_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


