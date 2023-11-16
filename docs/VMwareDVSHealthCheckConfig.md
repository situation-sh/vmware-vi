# VMwareDVSHealthCheckConfig

This class defines health check configuration for VMware vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_mware_dvs_health_check_config import VMwareDVSHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSHealthCheckConfig from a JSON string
v_mware_dvs_health_check_config_instance = VMwareDVSHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDVSHealthCheckConfig.to_json()

# convert the object into a dict
v_mware_dvs_health_check_config_dict = v_mware_dvs_health_check_config_instance.to_dict()
# create an instance of VMwareDVSHealthCheckConfig from a dict
v_mware_dvs_health_check_config_form_dict = v_mware_dvs_health_check_config.from_dict(v_mware_dvs_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


