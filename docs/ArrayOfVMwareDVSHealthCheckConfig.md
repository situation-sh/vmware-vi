# ArrayOfVMwareDVSHealthCheckConfig

A boxed array of *VMwareDVSHealthCheckConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareDVSHealthCheckConfig]**](VMwareDVSHealthCheckConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_dvs_health_check_config import ArrayOfVMwareDVSHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareDVSHealthCheckConfig from a JSON string
array_of_v_mware_dvs_health_check_config_instance = ArrayOfVMwareDVSHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareDVSHealthCheckConfig.to_json()

# convert the object into a dict
array_of_v_mware_dvs_health_check_config_dict = array_of_v_mware_dvs_health_check_config_instance.to_dict()
# create an instance of ArrayOfVMwareDVSHealthCheckConfig from a dict
array_of_v_mware_dvs_health_check_config_form_dict = array_of_v_mware_dvs_health_check_config.from_dict(array_of_v_mware_dvs_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


