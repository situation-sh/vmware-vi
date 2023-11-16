# VspanSameSessionPortConflict

Thrown if a dvPort appears in both the source and destination ports of the same Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session_key** | **str** | The key of the Distributed Port Mirroring session in which a dvPort appears in both the source and destination ports  ***Since:*** vSphere API 5.0  | 
**port_key** | **str** | The key of the port that appears in both the source and destination ports of the same Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_same_session_port_conflict import VspanSameSessionPortConflict

# TODO update the JSON string below
json = "{}"
# create an instance of VspanSameSessionPortConflict from a JSON string
vspan_same_session_port_conflict_instance = VspanSameSessionPortConflict.from_json(json)
# print the JSON string representation of the object
print VspanSameSessionPortConflict.to_json()

# convert the object into a dict
vspan_same_session_port_conflict_dict = vspan_same_session_port_conflict_instance.to_dict()
# create an instance of VspanSameSessionPortConflict from a dict
vspan_same_session_port_conflict_form_dict = vspan_same_session_port_conflict.from_dict(vspan_same_session_port_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


