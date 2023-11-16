# VsanHostMembershipInfo

The *VsanHostMembershipInfo* data object contains VSAN cluster membership information for a single host, as observed from a given host.  This data object is used to represent read-only state whose values may change during operation.  See also *HostRuntimeInfo.vsanRuntimeInfo*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uuid** | **str** | VSAN node UUID for the host of this MembershipInfo.  See also *VsanHostClusterStatus.nodeUuid*.  ***Since:*** vSphere API 5.5  | 
**hostname** | **str** | Hostname for the host of this MembershipInfo.  May be the empty string \&quot;\&quot; if the hostname is unavailable.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_membership_info import VsanHostMembershipInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostMembershipInfo from a JSON string
vsan_host_membership_info_instance = VsanHostMembershipInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostMembershipInfo.to_json()

# convert the object into a dict
vsan_host_membership_info_dict = vsan_host_membership_info_instance.to_dict()
# create an instance of VsanHostMembershipInfo from a dict
vsan_host_membership_info_form_dict = vsan_host_membership_info.from_dict(vsan_host_membership_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


