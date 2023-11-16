# HostMemberHealthCheckResult

This class defines healthcheck result of the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | The summary of health check result.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.host_member_health_check_result import HostMemberHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemberHealthCheckResult from a JSON string
host_member_health_check_result_instance = HostMemberHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print HostMemberHealthCheckResult.to_json()

# convert the object into a dict
host_member_health_check_result_dict = host_member_health_check_result_instance.to_dict()
# create an instance of HostMemberHealthCheckResult from a dict
host_member_health_check_result_form_dict = host_member_health_check_result.from_dict(host_member_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


