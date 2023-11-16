# VMwareDVSTeamingHealthCheckResult

This class defines teaming health check result of a host that joined the VMware vSphered Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teaming_status** | **str** | Teaming check status.  See *VMwareDVSTeamingMatchStatus_enum* for valid values.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_teaming_health_check_result import VMwareDVSTeamingHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSTeamingHealthCheckResult from a JSON string
v_mware_dvs_teaming_health_check_result_instance = VMwareDVSTeamingHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print VMwareDVSTeamingHealthCheckResult.to_json()

# convert the object into a dict
v_mware_dvs_teaming_health_check_result_dict = v_mware_dvs_teaming_health_check_result_instance.to_dict()
# create an instance of VMwareDVSTeamingHealthCheckResult from a dict
v_mware_dvs_teaming_health_check_result_form_dict = v_mware_dvs_teaming_health_check_result.from_dict(v_mware_dvs_teaming_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


