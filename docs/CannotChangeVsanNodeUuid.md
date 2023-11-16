# CannotChangeVsanNodeUuid

Fault thrown for cases that a VSAN node UUID may not be changed.  For example, the VSAN node UUID for a host may not be changed so long as that host is enabled for VSAN.  See also *HostVsanSystem.UpdateVsan_Task*, *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_change_vsan_node_uuid import CannotChangeVsanNodeUuid

# TODO update the JSON string below
json = "{}"
# create an instance of CannotChangeVsanNodeUuid from a JSON string
cannot_change_vsan_node_uuid_instance = CannotChangeVsanNodeUuid.from_json(json)
# print the JSON string representation of the object
print CannotChangeVsanNodeUuid.to_json()

# convert the object into a dict
cannot_change_vsan_node_uuid_dict = cannot_change_vsan_node_uuid_instance.to_dict()
# create an instance of CannotChangeVsanNodeUuid from a dict
cannot_change_vsan_node_uuid_form_dict = cannot_change_vsan_node_uuid.from_dict(cannot_change_vsan_node_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


