# HostMemberUplinkHealthCheckResult

This class defines healthcheck result of a specified Uplink port in vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uplink_port_key** | **str** | The uplink port key.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_member_uplink_health_check_result import HostMemberUplinkHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemberUplinkHealthCheckResult from a JSON string
host_member_uplink_health_check_result_instance = HostMemberUplinkHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print HostMemberUplinkHealthCheckResult.to_json()

# convert the object into a dict
host_member_uplink_health_check_result_dict = host_member_uplink_health_check_result_instance.to_dict()
# create an instance of HostMemberUplinkHealthCheckResult from a dict
host_member_uplink_health_check_result_form_dict = host_member_uplink_health_check_result.from_dict(host_member_uplink_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


