# VsanHostDecommissionMode

A *VsanHostDecommissionMode* defines an action to take upon decommissioning a host from use with the VSAN service.  If the VSAN service DecommissionMode is omitted in a call to *HostSystem.EnterMaintenanceMode_Task*, the default action chosen will be *ensureObjectAccessibility*.  See also *HostSystem.EnterMaintenanceMode_Task*, *HostMaintenanceSpec.vsanMode*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_action** | **str** | Specifies an action to take with regard to the VSAN service upon putting a host into maintenance mode.  See also *VsanHostDecommissionModeObjectAction_enum*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_decommission_mode import VsanHostDecommissionMode

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDecommissionMode from a JSON string
vsan_host_decommission_mode_instance = VsanHostDecommissionMode.from_json(json)
# print the JSON string representation of the object
print VsanHostDecommissionMode.to_json()

# convert the object into a dict
vsan_host_decommission_mode_dict = vsan_host_decommission_mode_instance.to_dict()
# create an instance of VsanHostDecommissionMode from a dict
vsan_host_decommission_mode_form_dict = vsan_host_decommission_mode.from_dict(vsan_host_decommission_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


