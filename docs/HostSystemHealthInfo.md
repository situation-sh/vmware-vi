# HostSystemHealthInfo

This data object provides information about the health of the phyical system.  The data is retrieved from numeric sensor probes.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numeric_sensor_info** | [**List[HostNumericSensorInfo]**](HostNumericSensorInfo.md) | Health information provided by the power probes.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_system_health_info import HostSystemHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemHealthInfo from a JSON string
host_system_health_info_instance = HostSystemHealthInfo.from_json(json)
# print the JSON string representation of the object
print HostSystemHealthInfo.to_json()

# convert the object into a dict
host_system_health_info_dict = host_system_health_info_instance.to_dict()
# create an instance of HostSystemHealthInfo from a dict
host_system_health_info_form_dict = host_system_health_info.from_dict(host_system_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


