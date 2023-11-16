# HostMemberRuntimeInfo

The *HostMemberRuntimeInfo* data object contains healthcheck and status information about a host member of a distributed virtual switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | **str** | Host proxy switch status.  See *HostComponentState* for valid values. This property replaces the deprecated *DistributedVirtualSwitchHostMember*.*DistributedVirtualSwitchHostMember.status*.  ***Since:*** vSphere API 5.1  | [optional] 
**status_detail** | **str** | Additional information regarding the current membership status of the host.  This property replaces the deprecated *DistributedVirtualSwitchHostMember*.*DistributedVirtualSwitchHostMember.statusDetail*.  ***Since:*** vSphere API 5.1  | [optional] 
**nsxt_status** | **str** | NSX-T component status.  ***Since:*** vSphere API 7.0  | [optional] 
**nsxt_status_detail** | **str** | Additional information regarding the NSX-T component status.  ***Since:*** vSphere API 7.0  | [optional] 
**health_check_result** | [**List[HostMemberHealthCheckResult]**](HostMemberHealthCheckResult.md) | Health check result for the host that joined the distributed virtual switch.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.host_member_runtime_info import HostMemberRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemberRuntimeInfo from a JSON string
host_member_runtime_info_instance = HostMemberRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print HostMemberRuntimeInfo.to_json()

# convert the object into a dict
host_member_runtime_info_dict = host_member_runtime_info_instance.to_dict()
# create an instance of HostMemberRuntimeInfo from a dict
host_member_runtime_info_form_dict = host_member_runtime_info.from_dict(host_member_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


