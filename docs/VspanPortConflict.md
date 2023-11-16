# VspanPortConflict

Thrown if a DistributedVirtualPort appears in both the transmitted source and destination ports of any Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session_key1** | **str** | The key of the Distributed Port Mirroring session that is in conflict  ***Since:*** vSphere API 5.0  | 
**vspan_session_key2** | **str** | The key of the Distributed Port Mirroring session that is in conflict  ***Since:*** vSphere API 5.0  | 
**port_key** | **str** | The key of the port that is both the transmitted source and destination.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_port_conflict import VspanPortConflict

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPortConflict from a JSON string
vspan_port_conflict_instance = VspanPortConflict.from_json(json)
# print the JSON string representation of the object
print VspanPortConflict.to_json()

# convert the object into a dict
vspan_port_conflict_dict = vspan_port_conflict_instance.to_dict()
# create an instance of VspanPortConflict from a dict
vspan_port_conflict_form_dict = vspan_port_conflict.from_dict(vspan_port_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


