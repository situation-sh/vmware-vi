# VsanHostClusterStatus

The *VsanHostClusterStatus* data object contains a host's cluster status information for the VSAN service.  This data object is used to represent read-only state whose values may change during operation.  See also *HostVsanSystem.QueryHostStatus*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | VSAN service cluster UUID.  ***Since:*** vSphere API 5.5  | [optional] 
**node_uuid** | **str** | VSAN node UUID for this host.  ***Since:*** vSphere API 5.5  | [optional] 
**health** | **str** | VSAN health state for this host.  See also *VsanHostHealthState_enum*.  ***Since:*** vSphere API 5.5  | 
**node_state** | [**VsanHostClusterStatusState**](VsanHostClusterStatusState.md) |  | 
**member_uuid** | **List[str]** | List of UUIDs for VSAN nodes known to this host.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_cluster_status import VsanHostClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostClusterStatus from a JSON string
vsan_host_cluster_status_instance = VsanHostClusterStatus.from_json(json)
# print the JSON string representation of the object
print VsanHostClusterStatus.to_json()

# convert the object into a dict
vsan_host_cluster_status_dict = vsan_host_cluster_status_instance.to_dict()
# create an instance of VsanHostClusterStatus from a dict
vsan_host_cluster_status_form_dict = vsan_host_cluster_status.from_dict(vsan_host_cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


