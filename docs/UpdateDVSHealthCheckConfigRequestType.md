# UpdateDVSHealthCheckConfigRequestType

The parameters of *DistributedVirtualSwitch.UpdateDVSHealthCheckConfig_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_check_config** | [**List[DVSHealthCheckConfig]**](DVSHealthCheckConfig.md) | The health check configuration.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.update_dvs_health_check_config_request_type import UpdateDVSHealthCheckConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDVSHealthCheckConfigRequestType from a JSON string
update_dvs_health_check_config_request_type_instance = UpdateDVSHealthCheckConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDVSHealthCheckConfigRequestType.to_json()

# convert the object into a dict
update_dvs_health_check_config_request_type_dict = update_dvs_health_check_config_request_type_instance.to_dict()
# create an instance of UpdateDVSHealthCheckConfigRequestType from a dict
update_dvs_health_check_config_request_type_form_dict = update_dvs_health_check_config_request_type.from_dict(update_dvs_health_check_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


