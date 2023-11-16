# ArrayOfDVSTrafficShapingPolicy

A boxed array of *DVSTrafficShapingPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSTrafficShapingPolicy]**](DVSTrafficShapingPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_traffic_shaping_policy import ArrayOfDVSTrafficShapingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSTrafficShapingPolicy from a JSON string
array_of_dvs_traffic_shaping_policy_instance = ArrayOfDVSTrafficShapingPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSTrafficShapingPolicy.to_json()

# convert the object into a dict
array_of_dvs_traffic_shaping_policy_dict = array_of_dvs_traffic_shaping_policy_instance.to_dict()
# create an instance of ArrayOfDVSTrafficShapingPolicy from a dict
array_of_dvs_traffic_shaping_policy_form_dict = array_of_dvs_traffic_shaping_policy.from_dict(array_of_dvs_traffic_shaping_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


