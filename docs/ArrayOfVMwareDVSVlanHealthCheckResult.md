# ArrayOfVMwareDVSVlanHealthCheckResult

A boxed array of *VMwareDVSVlanHealthCheckResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareDVSVlanHealthCheckResult]**](VMwareDVSVlanHealthCheckResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_dvs_vlan_health_check_result import ArrayOfVMwareDVSVlanHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareDVSVlanHealthCheckResult from a JSON string
array_of_v_mware_dvs_vlan_health_check_result_instance = ArrayOfVMwareDVSVlanHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareDVSVlanHealthCheckResult.to_json()

# convert the object into a dict
array_of_v_mware_dvs_vlan_health_check_result_dict = array_of_v_mware_dvs_vlan_health_check_result_instance.to_dict()
# create an instance of ArrayOfVMwareDVSVlanHealthCheckResult from a dict
array_of_v_mware_dvs_vlan_health_check_result_form_dict = array_of_v_mware_dvs_vlan_health_check_result.from_dict(array_of_v_mware_dvs_vlan_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


