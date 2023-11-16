# DVSHealthCheckConfig

The *DVSHealthCheckConfig* data object defines vSphere Distributed Switch health check configuration.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | True if enable health check.  ***Since:*** vSphere API 5.1  | [optional] 
**interval** | **int** | Interval of health check, in minutes.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.dvs_health_check_config import DVSHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DVSHealthCheckConfig from a JSON string
dvs_health_check_config_instance = DVSHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print DVSHealthCheckConfig.to_json()

# convert the object into a dict
dvs_health_check_config_dict = dvs_health_check_config_instance.to_dict()
# create an instance of DVSHealthCheckConfig from a dict
dvs_health_check_config_form_dict = dvs_health_check_config.from_dict(dvs_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


