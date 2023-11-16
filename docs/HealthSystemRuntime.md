# HealthSystemRuntime

The system health runtime information  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_health_info** | [**HostSystemHealthInfo**](HostSystemHealthInfo.md) |  | [optional] 
**hardware_status_info** | [**HostHardwareStatusInfo**](HostHardwareStatusInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.health_system_runtime import HealthSystemRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of HealthSystemRuntime from a JSON string
health_system_runtime_instance = HealthSystemRuntime.from_json(json)
# print the JSON string representation of the object
print HealthSystemRuntime.to_json()

# convert the object into a dict
health_system_runtime_dict = health_system_runtime_instance.to_dict()
# create an instance of HealthSystemRuntime from a dict
health_system_runtime_form_dict = health_system_runtime.from_dict(health_system_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


