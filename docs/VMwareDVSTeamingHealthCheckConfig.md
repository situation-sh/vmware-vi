# VMwareDVSTeamingHealthCheckConfig

This class defines the teaming health check configuration.  Teaming health check is used to check whether the teaming policy configuration of the vSphere Distributed Switch matches the physical switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_mware_dvs_teaming_health_check_config import VMwareDVSTeamingHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSTeamingHealthCheckConfig from a JSON string
v_mware_dvs_teaming_health_check_config_instance = VMwareDVSTeamingHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDVSTeamingHealthCheckConfig.to_json()

# convert the object into a dict
v_mware_dvs_teaming_health_check_config_dict = v_mware_dvs_teaming_health_check_config_instance.to_dict()
# create an instance of VMwareDVSTeamingHealthCheckConfig from a dict
v_mware_dvs_teaming_health_check_config_form_dict = v_mware_dvs_teaming_health_check_config.from_dict(v_mware_dvs_teaming_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


