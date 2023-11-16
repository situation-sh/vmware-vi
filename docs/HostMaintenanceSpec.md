# HostMaintenanceSpec

The *HostMaintenanceSpec* data object may be used to specify actions to be taken by a host upon entering maintenance mode.  If the *HostMaintenanceSpec* or any of its fields are omitted in a call to *HostSystem.EnterMaintenanceMode_Task*, default actions will be chosen as documented for each field's type.  See also *HostSystem.EnterMaintenanceMode_Task*, *VsanHostDecommissionMode*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vsan_mode** | [**VsanHostDecommissionMode**](VsanHostDecommissionMode.md) |  | [optional] 
**purpose** | **str** | Maintenance mode reason code.  See *HostMaintenanceSpecPurpose_enum* for valid values.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_maintenance_spec import HostMaintenanceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostMaintenanceSpec from a JSON string
host_maintenance_spec_instance = HostMaintenanceSpec.from_json(json)
# print the JSON string representation of the object
print HostMaintenanceSpec.to_json()

# convert the object into a dict
host_maintenance_spec_dict = host_maintenance_spec_instance.to_dict()
# create an instance of HostMaintenanceSpec from a dict
host_maintenance_spec_form_dict = host_maintenance_spec.from_dict(host_maintenance_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


