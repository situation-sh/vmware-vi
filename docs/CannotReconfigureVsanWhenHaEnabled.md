# CannotReconfigureVsanWhenHaEnabled

Fault thrown for the case that an attempt is made to reconfigure VSAN when HA is currently enabled for a given *ClusterComputeResource*.  See also *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_reconfigure_vsan_when_ha_enabled import CannotReconfigureVsanWhenHaEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of CannotReconfigureVsanWhenHaEnabled from a JSON string
cannot_reconfigure_vsan_when_ha_enabled_instance = CannotReconfigureVsanWhenHaEnabled.from_json(json)
# print the JSON string representation of the object
print CannotReconfigureVsanWhenHaEnabled.to_json()

# convert the object into a dict
cannot_reconfigure_vsan_when_ha_enabled_dict = cannot_reconfigure_vsan_when_ha_enabled_instance.to_dict()
# create an instance of CannotReconfigureVsanWhenHaEnabled from a dict
cannot_reconfigure_vsan_when_ha_enabled_form_dict = cannot_reconfigure_vsan_when_ha_enabled.from_dict(cannot_reconfigure_vsan_when_ha_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


