# ArrayOfDvsTrafficFilterConfig

A boxed array of *DvsTrafficFilterConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsTrafficFilterConfig]**](DvsTrafficFilterConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_traffic_filter_config import ArrayOfDvsTrafficFilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsTrafficFilterConfig from a JSON string
array_of_dvs_traffic_filter_config_instance = ArrayOfDvsTrafficFilterConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsTrafficFilterConfig.to_json()

# convert the object into a dict
array_of_dvs_traffic_filter_config_dict = array_of_dvs_traffic_filter_config_instance.to_dict()
# create an instance of ArrayOfDvsTrafficFilterConfig from a dict
array_of_dvs_traffic_filter_config_form_dict = array_of_dvs_traffic_filter_config.from_dict(array_of_dvs_traffic_filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


