# CannotMoveVsanEnabledHost

Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into an unsuitable *ClusterComputeResource*.  The destination vim.ClusterComputeResource may be disabled for VSAN, or may be using VSAN with a different cluster UUID.  See also *ClusterComputeResource.AddHost_Task*, *ClusterComputeResource.MoveHostInto_Task*, *ClusterComputeResource.MoveInto_Task*, *VsanClusterUuidMismatch*, *DestinationVsanDisabled*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_move_vsan_enabled_host import CannotMoveVsanEnabledHost

# TODO update the JSON string below
json = "{}"
# create an instance of CannotMoveVsanEnabledHost from a JSON string
cannot_move_vsan_enabled_host_instance = CannotMoveVsanEnabledHost.from_json(json)
# print the JSON string representation of the object
print CannotMoveVsanEnabledHost.to_json()

# convert the object into a dict
cannot_move_vsan_enabled_host_dict = cannot_move_vsan_enabled_host_instance.to_dict()
# create an instance of CannotMoveVsanEnabledHost from a dict
cannot_move_vsan_enabled_host_form_dict = cannot_move_vsan_enabled_host.from_dict(cannot_move_vsan_enabled_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


