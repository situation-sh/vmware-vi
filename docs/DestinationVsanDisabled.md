# DestinationVsanDisabled

Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into a *ClusterComputeResource* which is disabled for VSAN.  See also *CannotMoveVsanEnabledHost*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_cluster** | **str** | Name of the disabled destination *ClusterComputeResource*.  See also *ManagedEntity.name*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.destination_vsan_disabled import DestinationVsanDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationVsanDisabled from a JSON string
destination_vsan_disabled_instance = DestinationVsanDisabled.from_json(json)
# print the JSON string representation of the object
print DestinationVsanDisabled.to_json()

# convert the object into a dict
destination_vsan_disabled_dict = destination_vsan_disabled_instance.to_dict()
# create an instance of DestinationVsanDisabled from a dict
destination_vsan_disabled_form_dict = destination_vsan_disabled.from_dict(destination_vsan_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


